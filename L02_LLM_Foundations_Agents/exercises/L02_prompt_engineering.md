# Exercise L02: Prompt Engineering Challenge

**Week 2 - LLM Foundations for Agents**

## Overview
Design and evaluate prompting strategies for agent reasoning tasks.

## Task 1: Implement Prompting Strategies (40 points)

Implement the following prompting strategies:
1. **Zero-shot**: Direct question, no examples
2. **Few-shot**: 2-3 examples before question
3. **Zero-shot CoT**: Add "Let's think step by step"
4. **Few-shot CoT**: Examples with reasoning traces

Test on 5 math word problems (GSM8K-style).

## Task 2: Self-Consistency Analysis (30 points)

1. Implement self-consistency with k=5 samples
2. Measure accuracy vs. single-sample CoT
3. Analyze: When does self-consistency help most?

## Task 3: Design Agent System Prompt (30 points)

Design a system prompt for a ReAct agent that:
- Defines the agent's role clearly
- Lists available tools
- Specifies output format
- Includes reasoning instructions

## Evaluation Rubric (100 points)

| Criterion | Points |
|-----------|--------|
| Prompting implementations | 40 |
| Self-consistency analysis | 30 |
| System prompt quality | 30 |

## Submission
- Jupyter notebook with all implementations
- Written analysis (300-500 words)
