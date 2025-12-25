# Reading Guide: Chain-of-Thought Paper

**Week 2 - LLM Foundations for Agents**

## Paper Details
- **Title**: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Authors**: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- **Year**: 2022
- **Venue**: NeurIPS 2022
- **arXiv**: https://arxiv.org/abs/2201.11903

## Why This Paper Matters
Chain-of-Thought prompting is foundational for LLM agents. It shows that explicitly generating reasoning traces dramatically improves multi-step problem solving.

## Critical Reading Guide

### Before Reading
1. What limitations do LLMs have on math/reasoning tasks?
2. How might showing intermediate steps help?

### During Reading
1. What is the key insight of CoT?
2. What types of tasks benefit most?
3. What model sizes are needed?

### After Reading
1. How does CoT relate to agent "thinking" steps?
2. What are the limitations not discussed?

## Discussion Questions
1. Is CoT emergent in large models or just pattern matching?
2. How would you adapt CoT for tool-using agents?
3. What's the cost-accuracy trade-off?

## Key Takeaways
- CoT = intermediate reasoning steps in prompts
- Works best on math, logic, multi-step reasoning
- Requires sufficiently large models (100B+)
- Foundation for agent reasoning systems
