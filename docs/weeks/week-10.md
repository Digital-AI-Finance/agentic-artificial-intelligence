---
layout: week
title: "Week 10: Agent Evaluation"
week_number: 10
nav_order: 10
parent: Weeks
---

## Key Concepts

**Agent Evaluation Challenges**:
- Trajectory dependence: Many valid paths to same goal
- Partial credit: How to score incomplete solutions?
- Environment variance: Results depend on environment state
- Cost: Each evaluation run costs time and API calls

**Major Benchmarks**:
- **AgentBench**: 8 environments (OS, database, web, games)
- **SWE-bench**: Real GitHub issues from Python repositories
- **WebArena**: Realistic web environments (shopping, forums)
- **GAIA**: General AI Assistant multi-modal tasks

**LLM-as-Judge**: Using an LLM to automatically evaluate agent outputs. Flexible but has biases (position, self-preference, verbosity).

## Exercise

Design an evaluation framework for a specific agent type:
1. Define clear success criteria (binary or graded scoring)
2. Create a representative task suite covering difficulty range
3. Implement LLM-as-Judge evaluation with structured rubrics
4. Establish baselines (random, human, prior models)
5. Compare multiple agent architectures with statistical significance

## Discussion Questions

1. How do you prevent benchmark overfitting when developing agents?
2. When is LLM-as-Judge reliable? What are its failure modes?
3. What makes a good human baseline for agent evaluation?
4. How should we balance success rate vs efficiency vs cost?
5. Are current benchmarks representative of real-world agent use cases?

## Additional Resources

- [AgentBench](https://github.com/THUDM/AgentBench)
- [WebArena](https://webarena.dev/)
- [SWE-bench](https://www.swebench.com/)
- [GAIA Benchmark](https://huggingface.co/gaia-benchmark)
