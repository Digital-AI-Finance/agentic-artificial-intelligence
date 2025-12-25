# Exercise L04: Build a Planning Agent

**Week 4 - Planning and Reasoning**

## Overview
Implement a planning agent that decomposes complex tasks and learns from failures using reflection.

## Task 1: Hierarchical Task Decomposition (35 points)

Implement a task decomposition system:

```python
def decompose_task(goal: str) -> dict:
    """
    Decompose a high-level goal into sub-tasks.

    Returns:
        {
            "goal": str,
            "sub_tasks": [
                {"id": 1, "task": str, "dependencies": []},
                {"id": 2, "task": str, "dependencies": [1]},
                ...
            ],
            "execution_order": [1, 2, 3, ...]
        }
    """
    pass
```

**Requirements:**
- Handle goals with 3-5 sub-tasks
- Track dependencies between sub-tasks
- Generate valid execution order (topological sort)
- Test with: "Plan a birthday party", "Deploy a web application"

## Task 2: Reflexion Agent (40 points)

Implement a Reflexion agent for code generation:

```python
class CodingReflexionAgent:
    def __init__(self, max_attempts: int = 3):
        self.memory = []
        self.max_attempts = max_attempts

    def solve(self, problem: str, test_cases: list) -> dict:
        """
        Attempt to solve a coding problem with reflection.

        Returns:
            {
                "success": bool,
                "solution": str,
                "attempts": int,
                "reflections": list
            }
        """
        pass

    def generate_code(self, problem: str, context: str) -> str:
        """Generate code solution."""
        pass

    def evaluate(self, code: str, test_cases: list) -> tuple:
        """Run test cases and return (passed, failed_info)."""
        pass

    def reflect(self, code: str, error: str) -> str:
        """Generate verbal reflection on failure."""
        pass
```

**Requirements:**
- Implement the full Reflexion loop
- Store reflections in episodic memory
- Use reflections to improve subsequent attempts
- Measure pass@k metrics

## Task 3: Plan-and-Solve Prompting (25 points)

Create prompts that implement Plan-and-Solve:

1. Design a planning prompt template
2. Design an execution prompt template
3. Test on 3 math word problems
4. Compare with direct prompting (no planning)

**Deliverable:** Jupyter notebook with:
- Planning prompts
- Execution prompts
- Comparison results
- Analysis of when planning helps

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Task Decomposition | 35 | Correct dependencies, valid order |
| Reflexion Implementation | 40 | Complete loop, memory management |
| Plan-and-Solve | 25 | Working prompts, fair comparison |

## Submission

1. Jupyter notebook with all implementations
2. Test results for each component
3. Written analysis (300-400 words) comparing approaches

## Bonus Challenge (+15 points)

Implement LATS (Language Agent Tree Search):
- Monte Carlo Tree Search for reasoning
- Value function for node evaluation
- Comparison with Reflexion on same tasks
