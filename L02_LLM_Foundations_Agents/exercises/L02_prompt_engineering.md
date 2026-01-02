# Exercise L02: Prompt Engineering and Reasoning Strategies

**Week 2 - LLM Foundations for Agents**

## Overview

In this exercise, you will implement and compare different prompting strategies for agent reasoning tasks, understanding how prompt design affects LLM reasoning capabilities.

## Learning Objectives

- **Primary (Apply)**: Implement CoT, ToT, and Self-Consistency prompting
- **Secondary (Analyze)**: Compare accuracy vs cost trade-offs across strategies
- **Tertiary (Evaluate)**: Select optimal prompting strategy for task type

## Prerequisites

- OpenAI API access (or Anthropic/local model)
- Python 3.10+
- Basic understanding of LLM APIs

## Problem Statement

Prompting strategies significantly affect LLM reasoning performance. Research shows:
- Chain-of-Thought (CoT) improves accuracy on reasoning tasks by 10-30%
- Self-Consistency can further improve by aggregating multiple reasoning paths
- Different strategies have different cost/accuracy trade-offs

### Task 1: Implement Prompting Strategies (30 points)

Implement four prompting strategies and test on reasoning tasks:

**Strategies to implement:**

| Strategy | Description | Implementation |
|----------|-------------|----------------|
| Zero-shot | Direct question, no examples | Basic prompt |
| Few-shot | 2-3 examples before question | Include demonstrations |
| Zero-shot CoT | Add "Let's think step by step" | Append trigger phrase |
| Few-shot CoT | Examples with reasoning traces | Demonstrations + CoT |

**Test Dataset (5 problems):**

```
Problem 1: A bakery sells cupcakes for $3 each. They sold 45 cupcakes on Monday
and 62 cupcakes on Tuesday. How much money did they make in total?

Problem 2: Sarah has 156 stickers. She gives 1/3 to her brother and 1/4 of
the remainder to her friend. How many stickers does she have left?

Problem 3: A train travels at 80 mph. Another train leaves the same station
2 hours later at 100 mph. How long until the second train catches up?

Problem 4: There are 3 red balls and 5 blue balls in a bag. If you draw 2 balls
without replacement, what is the probability both are blue?

Problem 5: A store has a 25% off sale. With an additional 10% member discount
on the reduced price, what is the total percentage off the original price?
```

**Deliverable**: Python functions for each strategy with correct answer tracking.

### Task 2: Self-Consistency Analysis (30 points)

Implement self-consistency decoding and analyze when it provides the most benefit:

**Requirements:**
1. Sample k=5 responses at temperature=0.7
2. Aggregate answers using majority voting
3. Compare accuracy against single-sample CoT at temperature=0
4. Analyze variance across samples

**Analysis Questions:**
- On which problem types does self-consistency help most?
- What is the cost overhead (5x API calls)?
- Is the accuracy improvement worth the cost?

**Format your analysis:**
```
Problem Type: [math/logic/reasoning]
Single CoT Accuracy: X%
Self-Consistency Accuracy: Y%
Improvement: Z%
Variance Analysis: [describe]
Cost Consideration: [break-even analysis]
```

### Task 3: Tree-of-Thoughts Exploration (15 points)

Implement a simplified Tree-of-Thoughts approach:

1. Generate 3 initial reasoning paths
2. Evaluate each path with a scoring prompt
3. Expand the best path
4. Compare final answer with CoT

**Evaluation prompt template:**
```
Rate this reasoning step on a scale of 1-5 for:
- Logical correctness
- Progress toward solution
- Clarity of explanation

Reasoning step: {step}
Rating (1-5):
```

### Task 4: Design Agent System Prompt (25 points)

Design a system prompt for a ReAct agent with the following requirements:

**Must include:**
1. Clear role definition (who is the agent?)
2. Available tools with descriptions
3. Output format specification (Thought/Action/Observation)
4. Reasoning instructions (when to think vs act)
5. Error handling guidance (what to do if stuck)

**Example tools to include:**
| Tool | Description | Parameters |
|------|-------------|------------|
| search | Search the web for information | query: string |
| calculator | Perform mathematical calculations | expression: string |
| lookup | Look up a fact in knowledge base | topic: string |

**Evaluation criteria:**
- Completeness (all required sections)
- Clarity (unambiguous instructions)
- Effectiveness (would it produce good agent behavior?)

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| Prompting Implementation | Python notebook | All 4 strategies implemented |
| Accuracy Results | Table/Chart | Comparison across strategies |
| Self-Consistency Analysis | Markdown | 300-500 word analysis |
| System Prompt | Markdown | Complete prompt with all sections |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Task 1: Prompting Strategies | 30 | Correct implementation of all 4 strategies |
| Task 2: Self-Consistency | 30 | Working implementation + meaningful analysis |
| Task 3: Tree-of-Thoughts | 15 | Basic ToT implementation |
| Task 4: System Prompt | 25 | Complete, clear, effective prompt |

### Detailed Rubric

**Task 1 (30 points)**
- 6 points per strategy (4 strategies = 24)
- 6 points for accuracy tracking and comparison

**Task 2 (30 points)**
- 15 points for working implementation
- 15 points for insightful analysis

**Task 3 (15 points)**
- 10 points for implementation
- 5 points for comparison with CoT

**Task 4 (25 points)**
- 5 points per required section (5 sections)

## Resources

- Wei et al. (2022). "Chain-of-Thought Prompting" - arXiv:2201.11903
- Yao et al. (2023). "Tree of Thoughts" - arXiv:2305.10601
- Wang et al. (2023). "Self-Consistency" - arXiv:2203.11171

## Submission

- **Format**: Jupyter notebook (.ipynb) + Markdown analysis
- **Filename**: `L02_exercise_[your_name].ipynb`
- **Due**: End of Week 2

## Hints

- Use temperature=0 for deterministic strategies, temperature=0.7 for sampling
- Parse numeric answers carefully (handle "The answer is 42" vs "42")
- For self-consistency, use regex to extract final answers
- Start with simpler problems before moving to complex ones

## Sample Output Format

```python
# Example output for Task 1
results = {
    "zero_shot": {"accuracy": 0.40, "avg_tokens": 150},
    "few_shot": {"accuracy": 0.60, "avg_tokens": 350},
    "zero_shot_cot": {"accuracy": 0.60, "avg_tokens": 280},
    "few_shot_cot": {"accuracy": 0.80, "avg_tokens": 520}
}
```

## Time Estimate
- Minimum: 3 hours
- Expected: 5 hours
- Maximum: 8 hours
