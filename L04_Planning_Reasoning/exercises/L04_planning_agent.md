# Exercise L04: Build a Planning Agent with Reflection

**Week 4 - Planning and Reasoning**

## Overview

Implement a planning agent that decomposes complex tasks hierarchically, learns from execution failures through reflection, and uses Plan-and-Solve prompting strategies.

## Learning Objectives

- **Primary (Create)**: Build an agent with hierarchical task decomposition and dependency tracking
- **Secondary (Apply)**: Implement the Reflexion pattern for iterative self-improvement
- **Tertiary (Evaluate)**: Compare planning-based vs direct approaches on reasoning tasks

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- Understanding of basic prompting techniques (CoT)
- Graph concepts (DAGs, topological sort)

## Problem Statement

LLMs struggle with complex, multi-step tasks for several reasons:
- Token limits prevent holding entire solutions in context
- No feedback on intermediate errors until final execution
- Lack of systematic exploration of solution space

Planning architectures address these by:
- Breaking tasks into manageable sub-tasks
- Executing incrementally with error checking
- Learning from failures through reflection

This exercise develops skills in building self-improving planning agents.

### Task 1: Hierarchical Task Decomposition (35 points)

Implement a task decomposition system that breaks goals into sub-tasks with dependencies:

**1a: Task Graph Schema (10 points)**
```python
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"  # Dependencies not met

@dataclass
class SubTask:
    id: int
    description: str
    dependencies: list[int] = field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[str] = None
    error: Optional[str] = None

@dataclass
class TaskPlan:
    goal: str
    sub_tasks: list[SubTask]
    execution_order: list[int]  # Topological sort of task IDs

    def is_ready(self, task_id: int) -> bool:
        """Check if a task's dependencies are all completed."""
        task = self.get_task(task_id)
        for dep_id in task.dependencies:
            dep = self.get_task(dep_id)
            if dep.status != TaskStatus.COMPLETED:
                return False
        return True

    def get_task(self, task_id: int) -> SubTask:
        """Get task by ID."""
        for task in self.sub_tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task {task_id} not found")
```

**1b: Decomposition with LLM (15 points)**
```python
def decompose_task(goal: str, llm_client) -> TaskPlan:
    """
    Use LLM to decompose a high-level goal into sub-tasks.

    Args:
        goal: High-level goal description
        llm_client: LLM client for generation

    Returns:
        TaskPlan with sub-tasks and execution order
    """
    decomposition_prompt = f"""Break down this goal into 3-7 concrete sub-tasks.
For each sub-task, identify which other sub-tasks must be completed first.

Goal: {goal}

Return as JSON:
{{
    "sub_tasks": [
        {{"id": 1, "description": "...", "dependencies": []}},
        {{"id": 2, "description": "...", "dependencies": [1]}},
        ...
    ]
}}

Rules:
- Each sub-task should be independently completable
- Dependencies form a valid DAG (no cycles)
- First task(s) should have no dependencies
- Final task should produce the goal outcome
"""

    response = llm_client.complete(decomposition_prompt)
    plan_json = json.loads(response)

    sub_tasks = [
        SubTask(
            id=t["id"],
            description=t["description"],
            dependencies=t.get("dependencies", [])
        )
        for t in plan_json["sub_tasks"]
    ]

    # Compute execution order via topological sort
    execution_order = topological_sort(sub_tasks)

    return TaskPlan(
        goal=goal,
        sub_tasks=sub_tasks,
        execution_order=execution_order
    )

def topological_sort(tasks: list[SubTask]) -> list[int]:
    """Return task IDs in valid execution order."""
    from collections import deque

    # Build adjacency list and in-degree count
    in_degree = {t.id: 0 for t in tasks}
    graph = {t.id: [] for t in tasks}

    for task in tasks:
        for dep in task.dependencies:
            graph[dep].append(task.id)
            in_degree[task.id] += 1

    # Kahn's algorithm
    queue = deque([t_id for t_id, deg in in_degree.items() if deg == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(tasks):
        raise ValueError("Cycle detected in task dependencies")

    return order
```

**1c: Plan Execution Engine (10 points)**
```python
class PlanExecutor:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.execution_log = []

    def execute_plan(self, plan: TaskPlan) -> dict:
        """Execute tasks in dependency order."""
        context = {"goal": plan.goal, "completed_tasks": {}}

        for task_id in plan.execution_order:
            task = plan.get_task(task_id)

            if not plan.is_ready(task_id):
                task.status = TaskStatus.BLOCKED
                continue

            task.status = TaskStatus.IN_PROGRESS
            try:
                result = self._execute_task(task, context)
                task.status = TaskStatus.COMPLETED
                task.result = result
                context["completed_tasks"][task_id] = result
                self.execution_log.append({
                    "task_id": task_id,
                    "status": "completed",
                    "result": result
                })
            except Exception as e:
                task.status = TaskStatus.FAILED
                task.error = str(e)
                self.execution_log.append({
                    "task_id": task_id,
                    "status": "failed",
                    "error": str(e)
                })

        return {
            "success": all(t.status == TaskStatus.COMPLETED for t in plan.sub_tasks),
            "completed": sum(1 for t in plan.sub_tasks if t.status == TaskStatus.COMPLETED),
            "total": len(plan.sub_tasks),
            "log": self.execution_log
        }

    def _execute_task(self, task: SubTask, context: dict) -> str:
        """Execute a single task using LLM."""
        prompt = f"""Complete this task given the context.

Goal: {context['goal']}
Current task: {task.description}
Completed tasks: {json.dumps(context['completed_tasks'], indent=2)}

Provide the result of completing this task:"""

        return self.llm.complete(prompt)
```

**Test Goals:**
| Goal | Expected Sub-tasks | Complexity |
|------|-------------------|------------|
| "Plan a birthday party" | Venue, invitations, food, decorations, entertainment | Medium |
| "Deploy a web application" | Code review, tests, build, staging, production | Medium |
| "Write a research paper" | Literature review, outline, draft sections, revise, submit | High |

### Task 2: Reflexion Agent (40 points)

Implement a Reflexion agent for code generation that learns from failures:

**2a: Core Reflexion Loop (25 points)**
```python
@dataclass
class ReflexionMemory:
    problem: str
    attempt_number: int
    code: str
    test_results: dict
    reflection: str
    timestamp: float

class CodingReflexionAgent:
    def __init__(self, llm_client, max_attempts: int = 3):
        self.llm = llm_client
        self.max_attempts = max_attempts
        self.episodic_memory: list[ReflexionMemory] = []

    def solve(self, problem: str, test_cases: list[dict]) -> dict:
        """
        Attempt to solve a coding problem with reflection on failures.

        Args:
            problem: Problem description
            test_cases: List of {"input": ..., "expected": ...}

        Returns:
            {
                "success": bool,
                "solution": str,
                "attempts": int,
                "reflections": list[str],
                "pass_rate": float
            }
        """
        reflections = []
        context = ""  # Accumulated reflections

        for attempt in range(1, self.max_attempts + 1):
            # Generate code with context from previous reflections
            code = self.generate_code(problem, context)

            # Evaluate against test cases
            passed, failed_info = self.evaluate(code, test_cases)

            if passed:
                return {
                    "success": True,
                    "solution": code,
                    "attempts": attempt,
                    "reflections": reflections,
                    "pass_rate": 1.0
                }

            # Generate reflection on failure
            reflection = self.reflect(problem, code, failed_info)
            reflections.append(reflection)

            # Store in episodic memory
            self.episodic_memory.append(ReflexionMemory(
                problem=problem,
                attempt_number=attempt,
                code=code,
                test_results=failed_info,
                reflection=reflection,
                timestamp=time.time()
            ))

            # Update context for next attempt
            context = self._build_context(reflections)

        # Return best attempt (most tests passed)
        return {
            "success": False,
            "solution": code,
            "attempts": self.max_attempts,
            "reflections": reflections,
            "pass_rate": failed_info.get("pass_rate", 0)
        }

    def generate_code(self, problem: str, context: str) -> str:
        """Generate code solution."""
        prompt = f"""Solve this coding problem.

Problem: {problem}

{f'Previous attempts failed. Learn from these reflections:{chr(10)}{context}' if context else ''}

Write a Python function that solves the problem. Only output the code, no explanation.
"""
        return self.llm.complete(prompt)

    def evaluate(self, code: str, test_cases: list[dict]) -> tuple[bool, dict]:
        """Run test cases and return (all_passed, failed_info)."""
        passed = 0
        failed = []

        for i, test in enumerate(test_cases):
            try:
                # Execute code (in sandbox in production!)
                local_vars = {}
                exec(code, {}, local_vars)

                # Find the function
                func = list(local_vars.values())[0]
                result = func(test["input"])

                if result == test["expected"]:
                    passed += 1
                else:
                    failed.append({
                        "test_index": i,
                        "input": test["input"],
                        "expected": test["expected"],
                        "actual": result
                    })
            except Exception as e:
                failed.append({
                    "test_index": i,
                    "input": test["input"],
                    "error": str(e)
                })

        all_passed = passed == len(test_cases)
        return all_passed, {
            "passed": passed,
            "total": len(test_cases),
            "pass_rate": passed / len(test_cases),
            "failed_tests": failed
        }

    def reflect(self, problem: str, code: str, error_info: dict) -> str:
        """Generate verbal reflection on failure."""
        prompt = f"""You attempted to solve this problem but some tests failed.
Analyze what went wrong and how to fix it.

Problem: {problem}

Your code:
```python
{code}
```

Failed tests:
{json.dumps(error_info['failed_tests'], indent=2)}

Write a brief reflection (2-3 sentences) about:
1. What the bug is
2. Why it occurred
3. How to fix it in the next attempt
"""
        return self.llm.complete(prompt)

    def _build_context(self, reflections: list[str]) -> str:
        """Build context string from reflections."""
        return "\n\n".join([
            f"Reflection {i+1}: {r}"
            for i, r in enumerate(reflections)
        ])
```

**2b: Test Problems (15 points)**

Implement and test on these problems:

| Problem | Difficulty | Test Cases |
|---------|------------|------------|
| Two Sum | Easy | 5 cases |
| Valid Parentheses | Easy | 5 cases |
| Reverse Linked List | Medium | 4 cases |
| Binary Search | Easy | 5 cases |
| Merge Intervals | Medium | 4 cases |

```python
test_problems = [
    {
        "problem": "Write a function that returns indices of two numbers that add up to target",
        "test_cases": [
            {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
            {"input": ([3, 2, 4], 6), "expected": [1, 2]},
            {"input": ([3, 3], 6), "expected": [0, 1]},
        ]
    },
    {
        "problem": "Write a function that checks if parentheses string is valid",
        "test_cases": [
            {"input": "()", "expected": True},
            {"input": "()[]{}", "expected": True},
            {"input": "(]", "expected": False},
            {"input": "([)]", "expected": False},
            {"input": "{[]}", "expected": True},
        ]
    },
]
```

### Task 3: Plan-and-Solve Prompting (25 points)

Implement and compare Plan-and-Solve with direct prompting:

**3a: Prompting Templates (10 points)**
```python
class PlanAndSolvePrompts:
    @staticmethod
    def planning_prompt(problem: str) -> str:
        return f"""Let's first understand the problem and devise a plan to solve it.

Problem: {problem}

Please create a step-by-step plan:
1. Identify the key variables and constraints
2. Break down the solution into clear steps
3. Consider edge cases

Plan:"""

    @staticmethod
    def execution_prompt(problem: str, plan: str) -> str:
        return f"""Now execute the plan to solve the problem.

Problem: {problem}

Plan:
{plan}

Let's follow the plan step by step:"""

    @staticmethod
    def direct_prompt(problem: str) -> str:
        return f"""Solve this problem.

Problem: {problem}

Answer:"""
```

**3b: Comparison Study (15 points)**

Test on these math word problems:

```python
math_problems = [
    {
        "problem": "A store sells apples for $2 each. John buys 15 apples and gives $50. How much change does he get?",
        "answer": 20
    },
    {
        "problem": "A train travels at 60 mph. Another train leaves 2 hours later at 90 mph. How long until the second train catches up?",
        "answer": 4  # hours
    },
    {
        "problem": "A tank fills at 5 gallons/min and drains at 2 gallons/min. Starting empty, how long to fill 90 gallons?",
        "answer": 30  # minutes
    },
]
```

**Comparison Metrics:**
| Metric | Direct | Plan-and-Solve |
|--------|--------|----------------|
| Accuracy (% correct) | | |
| Avg tokens used | | |
| Error types | | |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| task_decomposition.py | Python | Decomposition + execution |
| reflexion_agent.py | Python | Complete Reflexion implementation |
| plan_and_solve.py | Python | Prompting comparison |
| demo.ipynb | Jupyter | Interactive demonstrations |
| analysis.md | Markdown | 400-500 word comparison |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Task Decomposition | 35 | Correct dependencies, valid execution |
| Reflexion Implementation | 40 | Complete loop, learning behavior |
| Plan-and-Solve | 25 | Working prompts, fair comparison |

### Detailed Rubric

**Task Decomposition (35 points)**
- 10 points: Task graph schema is correct
- 15 points: LLM decomposition works reliably
- 10 points: Execution engine handles dependencies

**Reflexion (40 points)**
- 15 points: Generate-evaluate-reflect loop works
- 15 points: Memory accumulates and improves attempts
- 10 points: Test problems show improvement over attempts

**Plan-and-Solve (25 points)**
- 10 points: Both prompting strategies implemented
- 10 points: Fair comparison on same problems
- 5 points: Analysis explains when planning helps

## Resources

- Shinn et al. (2023). "Reflexion" - arXiv:2303.11366
- Wang et al. (2023). "Plan-and-Solve Prompting" - arXiv:2305.04091
- Zhou et al. (2024). "Language Agent Tree Search" - arXiv:2310.04406
- Yao et al. (2023). "ReAct" - arXiv:2210.03629

## Submission

- **Format**: Python files + Jupyter notebook + Markdown analysis
- **Filename**: `L04_exercise_[your_name]/`
- **Due**: End of Week 4

## Hints

- Start with simple goals for task decomposition (3-4 sub-tasks)
- For Reflexion, use easy LeetCode problems first
- Sandbox code execution carefully (use subprocess or Docker)
- Log everything during debugging - Reflexion is hard to trace
- Plan-and-Solve helps most on multi-step math problems

## Bonus Challenge (+15 points)

Implement LATS (Language Agent Tree Search):
```python
class LATS:
    def __init__(self, llm_client, n_samples: int = 5, depth: int = 3):
        self.llm = llm_client
        self.n_samples = n_samples
        self.depth = depth

    def search(self, problem: str) -> dict:
        """Use MCTS to find best solution."""
        # Implement:
        # 1. Sample n candidate solutions
        # 2. Score each with value function
        # 3. Expand most promising
        # 4. Repeat to depth
        pass

    def value_function(self, problem: str, partial_solution: str) -> float:
        """Score how promising a partial solution is."""
        pass
```

Compare LATS vs Reflexion on the same coding problems.

## Time Estimate
- Minimum: 5 hours
- Expected: 8 hours
- Maximum: 12 hours
