# Week 10 Exercise: Designing Agent Evaluation Criteria

## Objective
Design and implement a comprehensive evaluation framework for AI agents, including task-specific metrics, behavioral assessment, and comparative benchmarking.

## Learning Outcomes
- Define measurable success criteria for agent tasks
- Implement multi-dimensional evaluation metrics
- Build LLM-as-judge evaluation systems
- Conduct meaningful agent comparisons

## Task Description

### Part 1: Metric Framework Design (25%)
Design an evaluation framework with:
1. Task completion metrics (success rate, partial credit)
2. Efficiency metrics (steps, tokens, latency)
3. Quality metrics (accuracy, coherence, relevance)
4. Safety metrics (harmful outputs, policy violations)

### Part 2: Task Suite Development (25%)
Create a benchmark suite with:
1. 5 tasks per difficulty level (easy, medium, hard)
2. Clear input/output specifications
3. Ground truth answers or evaluation criteria
4. Edge cases and adversarial examples

### Part 3: LLM-as-Judge Implementation (30%)
Build an automated evaluation system:
1. Implement pairwise comparison judging
2. Implement direct scoring (1-10 scale)
3. Handle multi-aspect evaluation
4. Calibrate judge agreement with human evaluation

### Part 4: Comparative Analysis (20%)
Evaluate at least 2 agent architectures:
1. Run complete benchmark suite
2. Statistical significance testing
3. Error analysis and failure modes
4. Performance vs. cost trade-offs

## Deliverables
1. `evaluation_framework.py` - Core evaluation code
2. `benchmark_tasks.json` - Task definitions
3. `llm_judge.py` - LLM-as-judge implementation
4. `results_analysis.ipynb` - Comparative analysis
5. `evaluation_report.md` - Written analysis

## Benchmark Task Categories
Include tasks from:
- Information retrieval
- Mathematical reasoning
- Code generation
- Multi-step planning
- Tool use

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Metric Design | 20 | Comprehensive, measurable metrics |
| Task Quality | 25 | Diverse, well-specified tasks |
| Judge Implementation | 25 | Reliable automated evaluation |
| Analysis Rigor | 20 | Statistical validity, insights |
| Documentation | 10 | Clear methodology description |

## Resources
- AgentBench (Liu et al., 2023)
- WebArena (Zhou et al., 2024)
- GAIA Benchmark (Mialon et al., 2024)
- SWE-bench (Jimenez et al., 2024)

## Time Estimate
- Minimum: 5 hours
- Expected: 8 hours
- Maximum: 12 hours
