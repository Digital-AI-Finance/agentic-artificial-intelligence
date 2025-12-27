# Week 10 Reading Guide: Agent Evaluation and Benchmarking

## Primary Reading

### AgentBench: Evaluating LLMs as Agents
**Authors**: Liu, X., Yu, H., Zhang, H., et al.
**Year**: 2023
**arXiv**: 2308.03688

#### Key Concepts
- Multi-dimensional agent evaluation
- 8 distinct environments (OS, DB, web, games)
- Comprehensive model comparison
- Failure mode analysis

#### Critical Reading Questions
1. How do the evaluation dimensions transfer across environments?
2. What patterns distinguish successful vs. unsuccessful agents?
3. How do you prevent benchmark overfitting?

---

## Secondary Readings

### WebArena: A Realistic Web Environment for Building Autonomous Agents
**Authors**: Zhou, S., Xu, F. F., Zhu, H., et al.
**Year**: 2024
**arXiv**: 2307.13854

#### Focus Areas
- Realistic web task design
- Success criteria specification
- Human performance baselines
- Error taxonomy

### GAIA: A Benchmark for General AI Assistants
**Authors**: Mialon, G., Dessi, R., Lomeli, M., et al.
**Year**: 2024
**arXiv**: 2311.12983

#### Focus Areas
- Multi-modal reasoning tasks
- Difficulty calibration
- Tool use requirements
- Human vs. AI performance gaps

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
**Authors**: Jimenez, C. E., Yang, J., Wettig, A., et al.
**Year**: 2024
**arXiv**: 2310.06770

#### Focus Areas
- Real-world software engineering tasks
- Repository-level understanding
- Pass@k metrics
- Error analysis

---

## Discussion Questions

### For Seminar
1. **Generalization**: How do we design benchmarks that measure general capabilities vs. task-specific skills?

2. **Metrics**: What makes a good evaluation metric for agents? When do success rates fail to capture important differences?

3. **Human Baselines**: How should we interpret agent performance relative to human baselines?

4. **Contamination**: How do you prevent training data contamination in agent benchmarks?

5. **Real-World Transfer**: How well do benchmark results predict real-world deployment performance?

---

## Practical Exercises

### Before Class
1. Read AgentBench paper (focus on methodology and results)
2. Skim WebArena Section 3 (environment design)
3. Review SWE-bench results table

### After Class
1. Design 5 evaluation tasks for a specific domain
2. Implement LLM-as-judge for one task
3. Calculate inter-rater reliability

---

## Benchmark Comparison

| Benchmark | Domains | Metrics | Tasks | Human Baseline |
|-----------|---------|---------|-------|----------------|
| AgentBench | 8 envs | Success rate | 1000+ | Partial |
| WebArena | Web | Task completion | 812 | Yes |
| GAIA | General | Accuracy | 466 | Yes |
| SWE-bench | Code | Pass@k | 2294 | Yes |
| OSWorld | Desktop | Success rate | 369 | Yes |

---

## Related Papers

| Paper | Relationship | Notes |
|-------|--------------|-------|
| ALFWorld (Shridhar et al., 2021) | Foundational | Embodied agent benchmark |
| Mind2Web (Deng et al., 2023) | Web | Web navigation benchmark |
| ToolBench (Qin et al., 2024) | Tools | Tool use evaluation |
| MetaGPT (Hong et al., 2023) | Multi-agent | Software development |

---

## Evaluation Metrics Reference

| Metric | Description | Pros | Cons |
|--------|-------------|------|------|
| Success Rate | Binary task completion | Simple, interpretable | No partial credit |
| Pass@k | Any of k attempts passes | Accounts for variance | Expensive |
| F1 Score | Precision/recall balance | Multi-label tasks | Requires ground truth |
| Human Eval | Expert judgment | Captures nuance | Expensive, subjective |
| LLM-as-Judge | Model-based scoring | Scalable | May have biases |

---

## Key Takeaways
1. Agent evaluation requires multi-dimensional assessment
2. Realistic environments are crucial for valid evaluation
3. Human baselines provide important calibration
4. No single benchmark captures all capabilities
5. Evaluation should include failure mode analysis
