# Exercise L10: Designing Agent Evaluation Frameworks

**Week 10 - Agent Evaluation**

## Overview

Design and implement a comprehensive evaluation framework for AI agents, including task-specific metrics, behavioral assessment, LLM-as-Judge evaluation, and comparative benchmarking.

## Learning Objectives

- **Primary (Create)**: Design custom evaluation protocols for agent systems
- **Secondary (Analyze)**: Compare agent performance across multiple dimensions
- **Tertiary (Evaluate)**: Assess reliability and validity of evaluation methods

## Prerequisites

- Understanding of agent architectures
- OpenAI/Anthropic API access
- Python 3.10+, pandas, scipy

## Problem Statement

Evaluating agents is fundamentally different from evaluating LLMs:
- Multiple valid paths to the same goal
- Environment state affects outcomes
- Multi-step execution means errors compound
- Cost and efficiency matter alongside accuracy

This exercise develops skills in rigorous, multi-dimensional agent evaluation.

### Task 1: Metric Framework Design (25 points)

Design a comprehensive evaluation framework with metrics across four dimensions:

**Dimension 1: Task Completion**
```python
class TaskMetrics:
    success_rate: float      # Binary: task completed or not
    partial_credit: float    # Graded: percentage of subtasks completed
    pass_at_k: float         # Success rate with k attempts allowed
```

**Dimension 2: Efficiency**
```python
class EfficiencyMetrics:
    step_count: int          # Number of actions taken
    token_usage: int         # Total tokens consumed
    latency_seconds: float   # Wall-clock time
    api_cost_usd: float      # Estimated API cost
```

**Dimension 3: Quality**
```python
class QualityMetrics:
    accuracy: float          # Correctness of final output
    coherence: float         # Logical consistency of reasoning
    relevance: float         # Alignment with task requirements
```

**Dimension 4: Safety**
```python
class SafetyMetrics:
    harmful_outputs: int     # Count of harmful/unsafe outputs
    policy_violations: int   # Count of guideline violations
    hallucination_rate: float # Fraction of hallucinated claims
```

**Deliverable**: Complete metric class with calculation methods.

### Task 2: Benchmark Task Suite (25 points)

Create a benchmark suite with 15 tasks across 3 difficulty levels:

**Easy (5 tasks):**
| Task | Input | Expected Output | Evaluation |
|------|-------|-----------------|------------|
| E1: Simple calculation | "What is 15% of $320?" | "$48" | Exact match |
| E2: Fact lookup | "What is the capital of Japan?" | "Tokyo" | Exact match |
| E3: Format conversion | "Convert 72F to Celsius" | "22.2C" | Numeric tolerance |
| E4: Simple code | "Write Python to reverse a string" | Working code | Unit tests |
| E5: Summary | "Summarize this paragraph in 1 sentence" | Concise summary | LLM judge |

**Medium (5 tasks):**
| Task | Input | Expected Output | Evaluation |
|------|-------|-----------------|------------|
| M1: Multi-step calculation | Tax calculation with deductions | Correct amount | Exact match |
| M2: Multi-hop reasoning | "Who is the spouse of X's brother?" | Correct name | Exact match |
| M3: Code with tests | "Implement binary search with tests" | Passing tests | Unit tests |
| M4: Research synthesis | "Compare X and Y approaches" | Balanced comparison | LLM judge |
| M5: Planning | "Plan a 3-day itinerary for..." | Valid plan | LLM judge + constraints |

**Hard (5 tasks):**
| Task | Input | Expected Output | Evaluation |
|------|-------|-----------------|------------|
| H1: Complex code | "Implement LRU cache" | Passing tests | Unit tests |
| H2: Multi-agent coordination | "Have agents debate X" | Quality debate | LLM judge |
| H3: Long-horizon planning | "Plan a project with dependencies" | Valid DAG | Constraint checking |
| H4: Ambiguous requirements | Under-specified task | Clarification + solution | Human eval |
| H5: Adversarial input | Task with misleading context | Correct despite noise | Ground truth |

**Format for each task:**
```json
{
  "id": "E1",
  "difficulty": "easy",
  "input": "What is 15% of $320?",
  "expected_output": "$48",
  "evaluation_method": "exact_match",
  "evaluation_params": {"tolerance": 0.01},
  "tags": ["math", "single-step"]
}
```

### Task 3: LLM-as-Judge Implementation (30 points)

Implement automated evaluation using LLM as judge:

**3a: Pairwise Comparison (15 points)**
```python
def pairwise_compare(response_a: str, response_b: str, criteria: list[str]) -> dict:
    """
    Compare two responses, return which is better and why.

    Returns:
    {
        "winner": "A" | "B" | "tie",
        "confidence": 0.0-1.0,
        "reasoning": "...",
        "criteria_scores": {"accuracy": "A", "clarity": "B", ...}
    }
    """
    pass
```

**Important**: Randomize order and run both orderings to detect position bias.

**3b: Direct Scoring (15 points)**
```python
def score_response(response: str, task: dict, rubric: dict) -> dict:
    """
    Score a response on a 1-10 scale across multiple criteria.

    Returns:
    {
        "overall_score": 7.5,
        "criteria_scores": {
            "accuracy": 8,
            "completeness": 7,
            "clarity": 8,
            "efficiency": 7
        },
        "reasoning": "..."
    }
    """
    pass
```

**Rubric Template:**
```
Score 1-10 on each criterion:

ACCURACY (1-10): How correct is the answer?
- 1-3: Major errors or completely wrong
- 4-6: Partially correct, some errors
- 7-9: Mostly correct, minor issues
- 10: Completely correct

COMPLETENESS (1-10): Does it fully address the task?
- 1-3: Missing major components
- 4-6: Addresses core task, missing details
- 7-9: Comprehensive, minor omissions
- 10: Fully complete

CLARITY (1-10): How clear and well-structured?
- 1-3: Confusing, hard to follow
- 4-6: Understandable but could be clearer
- 7-9: Clear and well-organized
- 10: Exceptionally clear
```

### Task 4: Comparative Analysis (20 points)

Evaluate at least 2 different agent configurations and produce a rigorous comparison:

**Agents to compare (choose 2):**
- Zero-shot agent (no reasoning)
- CoT agent (chain-of-thought)
- ReAct agent (reasoning + actions)
- Self-correcting agent (with reflection)

**Analysis Requirements:**

1. **Run complete benchmark** (5 points)
   - All 15 tasks for each agent
   - 3 runs per task for variance estimation

2. **Statistical testing** (5 points)
   - Paired t-test or Wilcoxon signed-rank
   - Report p-values and confidence intervals
   - State whether differences are significant

3. **Error analysis** (5 points)
   - Categorize failure modes
   - Identify systematic weaknesses
   - Compare failure patterns between agents

4. **Cost-performance trade-off** (5 points)
   - Plot accuracy vs cost
   - Calculate cost per successful task
   - Recommend optimal configuration

**Results Table Format:**
```
| Agent  | Easy  | Medium | Hard  | Overall | Tokens | Cost  |
|--------|-------|--------|-------|---------|--------|-------|
| Zero   | 80%   | 40%    | 10%   | 43%     | 5,000  | $0.05 |
| CoT    | 100%  | 60%    | 30%   | 63%     | 12,000 | $0.12 |
| ReAct  | 100%  | 80%    | 40%   | 73%     | 20,000 | $0.20 |
```

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| evaluation_framework.py | Python | Complete metric classes |
| benchmark_tasks.json | JSON | 15 tasks with specifications |
| llm_judge.py | Python | Pairwise + direct scoring |
| results_analysis.ipynb | Jupyter | Full comparative analysis |
| evaluation_report.md | Markdown | 1000-word written analysis |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Metric Design | 20 | Comprehensive, measurable metrics |
| Task Quality | 25 | Diverse, well-specified tasks |
| Judge Implementation | 25 | Reliable automated evaluation |
| Analysis Rigor | 20 | Statistical validity, insights |
| Documentation | 10 | Clear methodology description |

### Detailed Rubric

**Metric Design (20 points)**
- 5 points: All four dimensions covered
- 5 points: Calculations are correct
- 5 points: Aggregation methods defined
- 5 points: Edge cases handled

**Task Quality (25 points)**
- 10 points: Diverse difficulty levels
- 5 points: Clear specifications
- 5 points: Appropriate evaluation methods
- 5 points: Edge cases included

**Judge Implementation (25 points)**
- 10 points: Pairwise comparison works
- 10 points: Direct scoring works
- 5 points: Bias mitigation implemented

**Analysis Rigor (20 points)**
- 5 points: Multiple runs for variance
- 5 points: Statistical tests applied
- 5 points: Error analysis meaningful
- 5 points: Cost analysis included

**Documentation (10 points)**
- 5 points: Methodology clear
- 5 points: Limitations acknowledged

## Resources

- Liu et al. (2023). "AgentBench" - arXiv:2308.03688
- Zhou et al. (2024). "WebArena" - arXiv:2307.13854
- Mialon et al. (2024). "GAIA" - arXiv:2311.12983
- Zheng et al. (2023). "Judging LLM-as-a-Judge" - arXiv:2306.05685

## Submission

- **Format**: Python files + Jupyter notebook + Markdown report
- **Filename**: `L10_exercise_[your_name]/`
- **Due**: End of Week 10

## Hints

- Start with exact-match tasks before moving to LLM-judged ones
- Position bias is real - always randomize order in pairwise comparisons
- Use structured output for more reliable LLM judgments
- Calculate inter-rater reliability if using multiple judge runs

## Sample Implementation

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class EvaluationResult:
    task_id: str
    agent_name: str
    success: bool
    partial_score: float
    metrics: dict
    llm_judge_score: float
    reasoning: str

class AgentEvaluator:
    def __init__(self, tasks: list[dict], judge_model: str = "gpt-4"):
        self.tasks = tasks
        self.judge_model = judge_model

    def evaluate_agent(self, agent, runs: int = 3) -> list[EvaluationResult]:
        """Run agent on all tasks with multiple runs."""
        pass

    def compare_agents(self, results_a, results_b) -> dict:
        """Statistical comparison of two agents."""
        pass
```

## Time Estimate
- Minimum: 5 hours
- Expected: 8 hours
- Maximum: 12 hours
