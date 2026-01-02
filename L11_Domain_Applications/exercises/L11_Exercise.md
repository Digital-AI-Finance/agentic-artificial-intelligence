# Exercise L11: Building a Production-Ready Domain Agent

**Week 11 - Domain Applications**

## Overview

Design and implement a complete agent for a specific domain, demonstrating practical application of agentic AI concepts with production-quality code, comprehensive testing, and domain-specific safety considerations.

## Learning Objectives

- **Primary (Apply)**: Implement a domain-specific agent with tool integration
- **Secondary (Create)**: Design domain-appropriate verification and safety mechanisms
- **Tertiary (Evaluate)**: Assess agent performance against domain-specific benchmarks

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- Understanding of ReAct, tool use, and agent architectures
- Familiarity with the chosen domain

## Problem Statement

Production domain agents require more than basic ReAct loops. They need:
- Domain-specific tool integration with proper error handling
- Compliance awareness and audit trails
- Verification mechanisms appropriate to domain risk
- Graceful degradation when tools fail

This exercise develops skills in building agents ready for real-world deployment.

---

## Domain Options

Choose ONE domain for your implementation:

### Option A: Code Generation Agent (Recommended for CS students)

Build an agent that follows the AlphaCodium flow engineering pattern.

### Option B: Financial Analysis Agent

Build an agent that performs research with compliance awareness.

### Option C: Research Assistant Agent

Build an agent that synthesizes academic literature.

### Option D: Customer Support Agent

Build an agent that handles support tickets with escalation.

---

## Part 1: Domain Analysis (20 points)

Before coding, document your chosen domain:

### 1a: Task Taxonomy (5 points)

```markdown
## Domain: [Your Choice]

### Primary Tasks
1. [Task 1]: [Description]
   - Input: [What the agent receives]
   - Output: [What the agent produces]
   - Success criteria: [How to verify success]

2. [Task 2]: [Description]
   ...

### Secondary Tasks
1. [Supporting task]: [Description]
   ...

### Out-of-Scope Tasks
- [Task the agent should refuse]: [Why]
- ...
```

### 1b: Tool Requirements (5 points)

```markdown
## Required Tools

| Tool | Purpose | API/Library | Error Modes |
|------|---------|-------------|-------------|
| [Tool 1] | [What it does] | [How to access] | [What can fail] |
| [Tool 2] | ... | ... | ... |
| ... | ... | ... | ... |

## Tool Dependencies
- [Tool A] requires [Tool B] to run first because [reason]
- ...
```

### 1c: Constraints and Regulations (5 points)

```markdown
## Domain Constraints

### Hard Constraints (Must Never Violate)
- [Constraint 1]: [Description and rationale]
- [Constraint 2]: ...

### Soft Constraints (Should Follow)
- [Guideline 1]: [Description]
- [Guideline 2]: ...

### Regulatory Requirements
- [Regulation]: [How agent must comply]
- ...
```

### 1d: Failure Mode Analysis (5 points)

```markdown
## Failure Modes

| Failure | Detection | Recovery | Escalation |
|---------|-----------|----------|------------|
| [Mode 1] | [How to detect] | [How to recover] | [When to escalate] |
| [Mode 2] | ... | ... | ... |
```

---

## Part 2: Tool Implementation (30 points)

Implement at least 3 domain-specific tools with proper error handling.

### 2a: Tool Schema Definition (10 points)

```python
from dataclasses import dataclass
from typing import Protocol, Any
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class ToolStatus(Enum):
    SUCCESS = "success"
    PARTIAL = "partial"      # Some results, but incomplete
    FAILURE = "failure"      # Tool failed
    RATE_LIMITED = "rate_limited"
    UNAUTHORIZED = "unauthorized"

@dataclass
class ToolResult:
    """Standardized tool result with status and metadata."""
    status: ToolStatus
    data: Any
    error_message: str | None = None
    metadata: dict | None = None

    @property
    def is_success(self) -> bool:
        return self.status in (ToolStatus.SUCCESS, ToolStatus.PARTIAL)

    def to_context(self) -> str:
        """Convert to string for LLM context."""
        if self.status == ToolStatus.SUCCESS:
            return f"Tool Result:\n{self.data}"
        elif self.status == ToolStatus.PARTIAL:
            return f"Partial Result (some data may be missing):\n{self.data}"
        else:
            return f"Tool Error: {self.error_message}"

class Tool(Protocol):
    """Protocol for domain tools."""
    name: str
    description: str

    def execute(self, **kwargs) -> ToolResult:
        """Execute the tool with given parameters."""
        ...

    def validate_params(self, **kwargs) -> tuple[bool, str]:
        """Validate parameters before execution."""
        ...
```

### 2b: Tool Implementations (20 points)

Implement at least 3 tools. Here's an example for a code agent:

```python
import subprocess
import tempfile
from pathlib import Path

class CodeExecutionTool:
    """Execute Python code in a sandboxed environment."""

    name = "execute_code"
    description = "Execute Python code and return output. Use for testing and validation."

    def __init__(self, timeout: int = 30, max_output_chars: int = 10000):
        self.timeout = timeout
        self.max_output_chars = max_output_chars

    def validate_params(self, code: str, **kwargs) -> tuple[bool, str]:
        """Validate code before execution."""
        if not code or not code.strip():
            return False, "Code cannot be empty"

        # Check for dangerous operations
        dangerous_patterns = [
            "os.system", "subprocess.call", "eval(", "exec(",
            "open(", "__import__", "importlib"
        ]
        for pattern in dangerous_patterns:
            if pattern in code:
                return False, f"Dangerous pattern detected: {pattern}"

        return True, ""

    def execute(self, code: str, test_input: str = "") -> ToolResult:
        """Execute code in isolated environment."""
        valid, error = self.validate_params(code=code)
        if not valid:
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message=error
            )

        try:
            with tempfile.NamedTemporaryFile(
                mode='w', suffix='.py', delete=False
            ) as f:
                f.write(code)
                temp_path = f.name

            result = subprocess.run(
                ['python', temp_path],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                input=test_input
            )

            Path(temp_path).unlink()  # Clean up

            if result.returncode == 0:
                output = result.stdout[:self.max_output_chars]
                return ToolResult(
                    status=ToolStatus.SUCCESS,
                    data={"output": output, "return_code": 0},
                    metadata={"execution_time": "completed"}
                )
            else:
                return ToolResult(
                    status=ToolStatus.FAILURE,
                    data=None,
                    error_message=result.stderr[:1000]
                )

        except subprocess.TimeoutExpired:
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message=f"Execution timed out after {self.timeout}s"
            )
        except Exception as e:
            logger.exception("Code execution failed")
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message=str(e)
            )


class TestRunnerTool:
    """Run tests against code implementation."""

    name = "run_tests"
    description = "Run pytest tests against implementation. Returns pass/fail status."

    def __init__(self, timeout: int = 60):
        self.timeout = timeout

    def validate_params(self, test_code: str, implementation: str, **kwargs) -> tuple[bool, str]:
        if not test_code.strip():
            return False, "Test code cannot be empty"
        if not implementation.strip():
            return False, "Implementation cannot be empty"
        return True, ""

    def execute(self, test_code: str, implementation: str) -> ToolResult:
        """Run tests and return results."""
        valid, error = self.validate_params(test_code=test_code, implementation=implementation)
        if not valid:
            return ToolResult(status=ToolStatus.FAILURE, data=None, error_message=error)

        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                # Write implementation
                impl_path = Path(tmpdir) / "solution.py"
                impl_path.write_text(implementation)

                # Write tests
                test_path = Path(tmpdir) / "test_solution.py"
                test_content = f"from solution import *\n\n{test_code}"
                test_path.write_text(test_content)

                # Run pytest
                result = subprocess.run(
                    ['python', '-m', 'pytest', str(test_path), '-v', '--tb=short'],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                    cwd=tmpdir
                )

                # Parse results
                passed = result.returncode == 0
                output = result.stdout + result.stderr

                return ToolResult(
                    status=ToolStatus.SUCCESS if passed else ToolStatus.PARTIAL,
                    data={
                        "passed": passed,
                        "output": output[:5000],
                        "return_code": result.returncode
                    },
                    metadata={"test_framework": "pytest"}
                )

        except subprocess.TimeoutExpired:
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message=f"Tests timed out after {self.timeout}s"
            )
        except Exception as e:
            logger.exception("Test execution failed")
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message=str(e)
            )


class CodeSearchTool:
    """Search for code patterns and examples."""

    name = "search_code"
    description = "Search for code patterns, examples, or documentation."

    def __init__(self, codebase_path: Path | None = None):
        self.codebase_path = codebase_path

    def validate_params(self, query: str, **kwargs) -> tuple[bool, str]:
        if not query or len(query) < 3:
            return False, "Query must be at least 3 characters"
        return True, ""

    def execute(self, query: str, file_pattern: str = "*.py", max_results: int = 10) -> ToolResult:
        """Search codebase for patterns."""
        valid, error = self.validate_params(query=query)
        if not valid:
            return ToolResult(status=ToolStatus.FAILURE, data=None, error_message=error)

        if not self.codebase_path:
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message="No codebase path configured"
            )

        try:
            import subprocess
            result = subprocess.run(
                ['grep', '-r', '-n', '-l', query, '--include', file_pattern],
                capture_output=True,
                text=True,
                cwd=self.codebase_path,
                timeout=30
            )

            files = result.stdout.strip().split('\n')[:max_results]
            files = [f for f in files if f]  # Remove empty

            return ToolResult(
                status=ToolStatus.SUCCESS if files else ToolStatus.PARTIAL,
                data={"matching_files": files, "query": query},
                metadata={"pattern": file_pattern}
            )

        except Exception as e:
            return ToolResult(
                status=ToolStatus.FAILURE,
                data=None,
                error_message=str(e)
            )
```

---

## Part 3: Agent Architecture (30 points)

Design and implement the agent workflow.

### 3a: Flow Engineering Pattern (15 points)

Implement a structured multi-stage pipeline (AlphaCodium style):

```python
from dataclasses import dataclass, field
from typing import Callable
from enum import Enum

class StageStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

@dataclass
class StageResult:
    status: StageStatus
    output: Any
    error: str | None = None
    duration_seconds: float = 0.0

@dataclass
class PipelineState:
    """Maintains state across pipeline stages."""
    task: str
    stage_results: dict[str, StageResult] = field(default_factory=dict)
    context: dict = field(default_factory=dict)

    def add_result(self, stage_name: str, result: StageResult):
        self.stage_results[stage_name] = result
        if result.output:
            self.context[stage_name] = result.output

    def get_context_for_stage(self, stage_name: str) -> str:
        """Build context string for a stage from previous results."""
        context_parts = [f"Original Task: {self.task}"]
        for name, result in self.stage_results.items():
            if result.status == StageStatus.COMPLETED:
                context_parts.append(f"\n## {name} Output:\n{result.output}")
        return "\n".join(context_parts)


class FlowEngineeringPipeline:
    """Multi-stage pipeline for complex tasks."""

    def __init__(self, llm_client, tools: dict[str, Tool]):
        self.llm = llm_client
        self.tools = tools
        self.stages: list[tuple[str, Callable]] = []

    def add_stage(self, name: str, handler: Callable[[PipelineState], StageResult]):
        """Add a processing stage."""
        self.stages.append((name, handler))

    def run(self, task: str) -> PipelineState:
        """Execute the pipeline."""
        state = PipelineState(task=task)

        for stage_name, handler in self.stages:
            logger.info(f"Starting stage: {stage_name}")
            start = time.time()

            try:
                result = handler(state)
                result.duration_seconds = time.time() - start
                state.add_result(stage_name, result)

                if result.status == StageStatus.FAILED:
                    logger.error(f"Stage {stage_name} failed: {result.error}")
                    break  # Stop pipeline on failure

            except Exception as e:
                logger.exception(f"Stage {stage_name} raised exception")
                state.add_result(stage_name, StageResult(
                    status=StageStatus.FAILED,
                    output=None,
                    error=str(e)
                ))
                break

        return state


class CodeAgentPipeline(FlowEngineeringPipeline):
    """Code generation pipeline following AlphaCodium pattern."""

    def __init__(self, llm_client, tools: dict[str, Tool]):
        super().__init__(llm_client, tools)
        self._setup_stages()

    def _setup_stages(self):
        """Define the code generation stages."""

        # Stage 1: Problem Understanding
        self.add_stage("understand_problem", self._stage_understand)

        # Stage 2: Generate Test Cases
        self.add_stage("generate_tests", self._stage_tests)

        # Stage 3: Initial Implementation
        self.add_stage("initial_implementation", self._stage_implement)

        # Stage 4: Test and Iterate
        self.add_stage("test_and_refine", self._stage_refine)

        # Stage 5: Final Validation
        self.add_stage("validate", self._stage_validate)

    def _stage_understand(self, state: PipelineState) -> StageResult:
        """Analyze and understand the problem."""
        prompt = f"""Analyze this programming task and extract:
1. Input specification
2. Output specification
3. Constraints
4. Edge cases to consider

Task: {state.task}

Provide structured analysis:"""

        response = self.llm.complete(prompt)

        return StageResult(
            status=StageStatus.COMPLETED,
            output=response
        )

    def _stage_tests(self, state: PipelineState) -> StageResult:
        """Generate test cases from problem understanding."""
        context = state.get_context_for_stage("generate_tests")

        prompt = f"""{context}

Based on the analysis above, generate pytest test cases.
Include:
- Basic functionality tests
- Edge case tests
- Error handling tests

Generate valid Python pytest code:"""

        test_code = self.llm.complete(prompt)

        return StageResult(
            status=StageStatus.COMPLETED,
            output=test_code
        )

    def _stage_implement(self, state: PipelineState) -> StageResult:
        """Generate initial implementation."""
        context = state.get_context_for_stage("initial_implementation")

        prompt = f"""{context}

Implement a solution that will pass the tests above.
Focus on correctness first, then optimize if needed.

Python implementation:"""

        code = self.llm.complete(prompt)

        return StageResult(
            status=StageStatus.COMPLETED,
            output=code
        )

    def _stage_refine(self, state: PipelineState) -> StageResult:
        """Run tests and refine implementation."""
        test_tool = self.tools.get("run_tests")
        if not test_tool:
            return StageResult(
                status=StageStatus.SKIPPED,
                output=None,
                error="Test runner not available"
            )

        test_code = state.context.get("generate_tests", "")
        implementation = state.context.get("initial_implementation", "")

        max_iterations = 3
        for iteration in range(max_iterations):
            result = test_tool.execute(test_code=test_code, implementation=implementation)

            if result.is_success and result.data.get("passed"):
                return StageResult(
                    status=StageStatus.COMPLETED,
                    output=implementation
                )

            # Get LLM to fix based on test output
            fix_prompt = f"""The implementation failed tests.

Test Output:
{result.data.get('output', result.error_message)}

Current Implementation:
{implementation}

Fix the implementation:"""

            implementation = self.llm.complete(fix_prompt)

        # Return best effort after max iterations
        return StageResult(
            status=StageStatus.PARTIAL if implementation else StageStatus.FAILED,
            output=implementation,
            error="Max iterations reached without passing all tests"
        )

    def _stage_validate(self, state: PipelineState) -> StageResult:
        """Final validation of the solution."""
        implementation = state.context.get("test_and_refine",
                                           state.context.get("initial_implementation"))

        exec_tool = self.tools.get("execute_code")
        if exec_tool and implementation:
            result = exec_tool.execute(code=implementation)
            if result.is_success:
                return StageResult(
                    status=StageStatus.COMPLETED,
                    output={
                        "code": implementation,
                        "validation": "Passed execution check"
                    }
                )

        return StageResult(
            status=StageStatus.COMPLETED,
            output={"code": implementation, "validation": "Skipped"}
        )
```

### 3b: Memory and Context Management (10 points)

```python
from collections import deque
import json

class AgentMemory:
    """Manages short and long-term memory for the agent."""

    def __init__(self, short_term_limit: int = 10, long_term_path: Path | None = None):
        self.short_term: deque = deque(maxlen=short_term_limit)
        self.long_term_path = long_term_path
        self.session_context: dict = {}

    def add_interaction(self, role: str, content: str, metadata: dict | None = None):
        """Add an interaction to short-term memory."""
        entry = {
            "role": role,
            "content": content,
            "timestamp": time.time(),
            "metadata": metadata or {}
        }
        self.short_term.append(entry)

    def get_recent_context(self, n: int = 5) -> list[dict]:
        """Get the n most recent interactions."""
        return list(self.short_term)[-n:]

    def build_context_string(self, n: int = 5) -> str:
        """Build a context string from recent memory."""
        recent = self.get_recent_context(n)
        parts = []
        for entry in recent:
            parts.append(f"{entry['role'].upper()}: {entry['content']}")
        return "\n\n".join(parts)

    def save_to_long_term(self, key: str, value: Any):
        """Save important information to long-term storage."""
        if self.long_term_path:
            data = {}
            if self.long_term_path.exists():
                data = json.loads(self.long_term_path.read_text())
            data[key] = {"value": value, "timestamp": time.time()}
            self.long_term_path.write_text(json.dumps(data, indent=2))

    def retrieve_from_long_term(self, key: str) -> Any | None:
        """Retrieve from long-term storage."""
        if self.long_term_path and self.long_term_path.exists():
            data = json.loads(self.long_term_path.read_text())
            entry = data.get(key)
            return entry["value"] if entry else None
        return None
```

### 3c: Output Formatting and Audit Trail (5 points)

```python
@dataclass
class AgentResponse:
    """Structured agent response with audit information."""
    answer: str
    confidence: float
    sources_used: list[str]
    tools_called: list[dict]
    reasoning_trace: list[str]
    warnings: list[str] = field(default_factory=list)

    def to_user_display(self) -> str:
        """Format for user display."""
        output = [self.answer]

        if self.warnings:
            output.append("\nWarnings:")
            for w in self.warnings:
                output.append(f"  - {w}")

        if self.sources_used:
            output.append("\nSources:")
            for s in self.sources_used:
                output.append(f"  - {s}")

        return "\n".join(output)

    def to_audit_log(self) -> dict:
        """Format for audit logging."""
        return {
            "timestamp": time.time(),
            "answer": self.answer,
            "confidence": self.confidence,
            "sources": self.sources_used,
            "tools": self.tools_called,
            "reasoning": self.reasoning_trace,
            "warnings": self.warnings
        }
```

---

## Part 4: Evaluation (20 points)

### 4a: Test Scenario Design (10 points)

Create 10+ test scenarios covering:

```python
@dataclass
class TestScenario:
    name: str
    description: str
    input_task: str
    expected_behavior: str
    category: str  # "basic", "edge_case", "error_handling", "domain_specific"
    difficulty: str  # "easy", "medium", "hard"
    has_ground_truth: bool
    ground_truth: Any | None = None

# Example scenarios for code agent
CODE_AGENT_SCENARIOS = [
    # Basic functionality
    TestScenario(
        name="simple_function",
        description="Generate a simple function",
        input_task="Write a Python function that returns the factorial of a number",
        expected_behavior="Should generate working factorial function",
        category="basic",
        difficulty="easy",
        has_ground_truth=True,
        ground_truth={"test": "assert factorial(5) == 120"}
    ),
    TestScenario(
        name="with_edge_cases",
        description="Handle edge cases properly",
        input_task="Write a function to find the second largest number in a list",
        expected_behavior="Should handle empty lists and duplicates",
        category="edge_case",
        difficulty="medium",
        has_ground_truth=True,
        ground_truth={"test": "assert second_largest([1,2,3]) == 2; assert second_largest([1,1,1]) is None"}
    ),
    TestScenario(
        name="complex_algorithm",
        description="Implement a complex algorithm",
        input_task="Implement a function to check if a string has balanced parentheses, brackets, and braces",
        expected_behavior="Should correctly validate all bracket types",
        category="domain_specific",
        difficulty="hard",
        has_ground_truth=True,
        ground_truth={"test": "assert is_balanced('({[]})') == True; assert is_balanced('([)]') == False"}
    ),
    TestScenario(
        name="error_handling",
        description="Generate code with proper error handling",
        input_task="Write a function to safely parse a JSON string and return a default if it fails",
        expected_behavior="Should catch exceptions and return default",
        category="error_handling",
        difficulty="medium",
        has_ground_truth=True,
        ground_truth={"test": "assert safe_json_parse('invalid', {}) == {}; assert safe_json_parse('{\"a\":1}', {}) == {'a':1}"}
    ),
    # Add 6+ more scenarios...
]
```

### 4b: Metrics and Analysis (10 points)

```python
@dataclass
class EvaluationMetrics:
    total_scenarios: int
    passed: int
    failed: int
    partial: int

    avg_time_seconds: float
    avg_confidence: float

    by_category: dict[str, dict]
    by_difficulty: dict[str, dict]

    tool_usage: dict[str, int]
    error_types: dict[str, int]

    @property
    def success_rate(self) -> float:
        return self.passed / self.total_scenarios if self.total_scenarios > 0 else 0.0

    def summary(self) -> str:
        return f"""
Evaluation Summary
==================
Total Scenarios: {self.total_scenarios}
Passed: {self.passed} ({self.success_rate:.1%})
Failed: {self.failed}
Partial: {self.partial}

Average Time: {self.avg_time_seconds:.2f}s
Average Confidence: {self.avg_confidence:.2f}

By Category:
{json.dumps(self.by_category, indent=2)}

By Difficulty:
{json.dumps(self.by_difficulty, indent=2)}
"""


def evaluate_agent(agent, scenarios: list[TestScenario]) -> EvaluationMetrics:
    """Run full evaluation suite."""
    results = []

    for scenario in scenarios:
        start = time.time()
        try:
            response = agent.run(scenario.input_task)
            elapsed = time.time() - start

            # Determine pass/fail
            passed = False
            if scenario.has_ground_truth and scenario.ground_truth:
                # Run ground truth test
                # (Implementation depends on ground truth format)
                passed = verify_ground_truth(response, scenario.ground_truth)
            else:
                # Use heuristics for open-ended tasks
                passed = response.confidence > 0.7

            results.append({
                "scenario": scenario.name,
                "category": scenario.category,
                "difficulty": scenario.difficulty,
                "passed": passed,
                "time": elapsed,
                "confidence": response.confidence,
                "tools_used": [t["name"] for t in response.tools_called]
            })

        except Exception as e:
            results.append({
                "scenario": scenario.name,
                "category": scenario.category,
                "difficulty": scenario.difficulty,
                "passed": False,
                "time": 0,
                "confidence": 0,
                "error": str(e)
            })

    # Compute aggregate metrics
    return compute_metrics(results)
```

---

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| domain_analysis.md | Markdown | Complete Part 1 documentation |
| tools/ | Python | At least 3 tool implementations |
| agent.py | Python | Main agent with pipeline |
| test_scenarios.py | Python | 10+ test scenarios |
| evaluation.ipynb | Jupyter | Test results and analysis |
| demo.py | Python | Interactive demonstration |

---

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Domain Analysis | 20 | Comprehensive analysis with failure modes |
| Tool Quality | 25 | Robust, well-tested, error-handling |
| Agent Architecture | 25 | Flow engineering, memory, audit trail |
| Evaluation | 20 | Comprehensive scenarios and metrics |
| Documentation | 10 | Clear code comments and usage docs |

### Detailed Rubric

**Domain Analysis (20 points)**
- 5 points: Task taxonomy is complete and accurate
- 5 points: Tool requirements are well-specified
- 5 points: Constraints/regulations properly identified
- 5 points: Failure modes analyzed with recovery strategies

**Tool Quality (25 points)**
- 10 points: Tools work correctly for happy path
- 10 points: Error handling is robust
- 5 points: Tools are well-documented

**Agent Architecture (25 points)**
- 10 points: Pipeline stages are well-designed
- 10 points: Memory and context management works
- 5 points: Audit trail is comprehensive

**Evaluation (20 points)**
- 10 points: Test scenarios cover diverse cases
- 5 points: Metrics are meaningful
- 5 points: Analysis provides insights

**Documentation (10 points)**
- 5 points: Code is well-commented
- 5 points: Usage is clearly explained

---

## Resources

- Ridnik et al. (2024). "AlphaCodium: Code Generation with Flow Engineering" arXiv:2401.08500
- Jimenez et al. (2024). "SWE-bench" arXiv:2310.06770
- Li et al. (2024). "FinAgent: Multimodal Trading Agent" arXiv:2402.18485
- Yang et al. (2024). "SWE-agent" arXiv:2405.15793

---

## Submission

- **Format**: Directory with all deliverables
- **Filename**: `L11_exercise_[your_name]/`
- **Due**: End of Week 11

---

## Time Estimate

- Minimum: 8 hours
- Expected: 12 hours
- Maximum: 18 hours
