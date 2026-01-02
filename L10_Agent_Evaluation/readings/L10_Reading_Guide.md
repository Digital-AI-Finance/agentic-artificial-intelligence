# Reading Guide: Agent Evaluation and Benchmarking

**Week 10 - Agent Evaluation**

## Primary Reading

### AgentBench: Evaluating LLMs as Agents

- **Title**: AgentBench: Evaluating LLMs as Agents
- **Authors**: Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, et al.
- **Year**: 2023
- **Venue**: ICLR 2024
- **arXiv**: https://arxiv.org/abs/2308.03688
- **Code**: https://github.com/THUDM/AgentBench

## Paper Classification

- **Type**: Benchmark paper (establishes evaluation framework)
- **Impact**: Standard benchmark for LLM agent evaluation
- **Prerequisites**: Understanding of agent architectures, basic evaluation metrics

## Why This Paper Matters

Evaluating agents is fundamentally different from evaluating LLMs:

1. **Multi-turn Interactions**: Success depends on sequences of actions
2. **Environment Coupling**: Results depend on execution environment
3. **Partial Observability**: Agents must handle incomplete information
4. **Multi-dimensional Skills**: Different tasks test different capabilities

AgentBench provides the first comprehensive framework for evaluating LLM agents across diverse environments.

---

## Secondary Readings

### WebArena: A Realistic Web Environment for Building Autonomous Agents

- **Authors**: Shuyan Zhou, Frank F. Xu, Hao Zhu, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2307.13854
- **Code**: https://github.com/web-arena-x/webarena

#### Focus Areas
- Realistic web task design
- Success criteria specification
- Human performance baselines
- Error taxonomy for web agents

### GAIA: A Benchmark for General AI Assistants

- **Authors**: Gregoire Mialon, Roberto Dessi, Maria Lomeli, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2311.12983

#### Focus Areas
- Multi-modal reasoning tasks
- Difficulty calibration methodology
- Tool use requirements
- Human vs. AI performance gaps

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

- **Authors**: Carlos E. Jimenez, John Yang, Alexander Wettig, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2310.06770
- **Code**: https://github.com/princeton-nlp/SWE-bench

#### Focus Areas
- Real-world software engineering tasks
- Repository-level code understanding
- Pass@k metrics for code generation
- Error analysis methodology

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: Why is agent evaluation difficult?
   - Actions have side effects
   - Environment state matters
   - Success criteria are complex
   - Partial credit is hard to assign

2. **Prior Work**: How were agents evaluated before?
   - Single-task benchmarks (arithmetic, QA)
   - Simulated environments (AlfWorld, TextWorld)
   - Human evaluation (expensive, inconsistent)

3. **Your Hypothesis**: What makes a good agent benchmark?

### During Reading: AgentBench

#### Section 1-2: Introduction and Background

- [ ] What are the eight evaluation environments?
- [ ] How were these environments selected?
- [ ] What capabilities does each environment test?

**Key Insight**: Different environments reveal different failure modes - no single benchmark suffices.

#### Section 3: Benchmark Design

**The Eight Environments**:

| Environment | Domain | Key Skills Tested |
|-------------|--------|-------------------|
| Operating System | System | Shell commands, file manipulation |
| Database | SQL | Query construction, data reasoning |
| Knowledge Graph | SPARQL | Graph traversal, semantic queries |
| Digital Card Game | Games | Strategy, long-horizon planning |
| Lateral Thinking | Puzzles | Creative reasoning, lateral thinking |
| House-Holding | Embodied | Object manipulation, navigation |
| Web Shopping | Web | UI interaction, search strategies |
| Web Browsing | Web | Information extraction, navigation |

- [ ] How is each environment implemented?
- [ ] What are the success criteria for each?
- [ ] How many tasks per environment?

#### Section 4: Evaluation Protocol

**Key Metrics**:

| Metric | Description | Use Case |
|--------|-------------|----------|
| Success Rate | Binary task completion | Overall performance |
| Partial Score | Progress toward goal | Understanding failures |
| Steps to Success | Efficiency measure | Comparing strategies |
| Error Rate | Types of failures | Diagnosing weaknesses |

```python
# AgentBench evaluation structure
def evaluate_agent(agent, environment, tasks):
    results = []
    for task in tasks:
        env = environment.reset(task)
        trajectory = []

        for step in range(max_steps):
            observation = env.observe()
            action = agent.act(observation)
            trajectory.append((observation, action))
            reward, done = env.step(action)

            if done:
                break

        results.append({
            "task_id": task.id,
            "success": env.is_success(),
            "steps": len(trajectory),
            "trajectory": trajectory
        })

    return aggregate_results(results)
```

- [ ] How are trajectories recorded?
- [ ] What constitutes partial success?
- [ ] How is consistency measured (multiple runs)?

#### Section 5: Results

**Key Results** (GPT-4 as best performer at time of publication):

| Environment | GPT-4 | Claude | Llama-2 |
|-------------|-------|--------|---------|
| OS | 42% | 35% | 12% |
| Database | 32% | 28% | 8% |
| Web Shopping | 29% | 22% | 5% |
| Overall | 28% | 23% | 7% |

- [ ] Which environments show the largest capability gaps?
- [ ] What patterns emerge across model sizes?
- [ ] Where do all models struggle?

#### Section 6: Analysis

**Failure Mode Taxonomy**:

| Failure Type | Description | Frequency |
|--------------|-------------|-----------|
| Syntax errors | Invalid command format | 15% |
| Logic errors | Wrong reasoning | 35% |
| State tracking | Lost track of progress | 20% |
| Tool misuse | Wrong tool for task | 18% |
| Hallucination | Non-existent actions | 12% |

- [ ] What are the most common failure modes?
- [ ] How do failure modes vary by environment?
- [ ] What distinguishes good from great models?

### During Reading: WebArena

#### Key Concepts

**Realistic Web Environment**:
- Real websites (shopping, forums, maps, GitLab)
- Dynamic content (not static HTML)
- Multi-step navigation required
- Human baseline comparison

**Success Criteria Types**:
| Type | Example | Verification |
|------|---------|--------------|
| URL match | Navigate to product page | Check final URL |
| Content match | Find specific information | Parse page content |
| State change | Add item to cart | Check cart state |
| Action sequence | Complete checkout | Verify order |

- [ ] How are web tasks designed?
- [ ] What makes web agent evaluation realistic?
- [ ] How do human baselines compare?

### After Reading

Reflect on these questions:

1. **Benchmark Design Principles**

   | Principle | Why Important |
   |-----------|---------------|
   | Diversity | Tests multiple capabilities |
   | Difficulty gradient | Enables fine-grained comparison |
   | Realistic tasks | Ensures practical relevance |
   | Reproducibility | Allows fair comparison |
   | Human baselines | Provides calibration |

2. **Evaluation Challenges**

   | Challenge | Approach |
   |-----------|----------|
   | Non-determinism | Multiple runs + aggregation |
   | Partial success | Continuous scoring |
   | Environment variance | Standardized configs |
   | Metric gaming | Hold-out test sets |

3. **Gaps in Current Benchmarks**
   - Long-horizon tasks (days/weeks)
   - Multi-agent coordination
   - Safety/harm evaluation
   - Real-world deployment metrics

---

## Discussion Questions (Seminar)

Prepare to discuss:

### Conceptual
1. How do we design benchmarks that measure general capabilities vs. task-specific skills?
2. What makes a good evaluation metric for agents?
3. Should benchmarks focus on capability ceilings or average performance?

### Technical
1. How do you prevent training data contamination in agent benchmarks?
2. How should we handle stochastic environments?
3. What's the right balance between automated and human evaluation?
4. How do you evaluate agents that learn during deployment?

### Practical
1. How well do benchmark results predict real-world deployment performance?
2. What's the cost of running comprehensive agent evaluations?
3. How do you compare agents across different model scales fairly?

### Research
1. What evaluation paradigms are missing for agentic AI?
2. How might we benchmark emergent capabilities?
3. Should evaluation include efficiency (cost, latency)?

---

## Key Takeaways to Remember

1. **Multi-Environment is Essential**: Single benchmarks miss important failure modes.

2. **Metrics Beyond Success Rate**:
   - Steps to success (efficiency)
   - Partial progress (capability gradient)
   - Failure type distribution (diagnostic value)

3. **Human Baselines Matter**: Without them, we can't calibrate difficulty.

4. **Benchmarks Age**: As models improve, benchmarks saturate.

5. **Realistic > Synthetic**: Real tasks reveal issues that toy problems hide.

6. **Evaluation Matrix**:
   | What to Measure | Benchmark |
   |-----------------|-----------|
   | General agentic ability | AgentBench |
   | Web navigation | WebArena |
   | General assistance | GAIA |
   | Software engineering | SWE-bench |
   | Tool use | ToolBench |

---

## Supplementary Readings

| Paper | Relationship |
|-------|-------------|
| ALFWorld (Shridhar et al., 2021) | Foundational embodied agent benchmark |
| Mind2Web (Deng et al., 2023) | Large-scale web navigation benchmark |
| ToolBench (Qin et al., 2024) | Tool use evaluation across 16k APIs |
| MetaGPT (Hong et al., 2023) | Multi-agent software development |
| OSWorld (Xie et al., 2024) | Computer use benchmark |

---

## Benchmark Comparison

| Benchmark | Domains | Tasks | Metrics | Human Baseline |
|-----------|---------|-------|---------|----------------|
| AgentBench | 8 environments | 1000+ | Success rate | Partial |
| WebArena | Web (4 sites) | 812 | Task completion | Yes (78%) |
| GAIA | General | 466 | Accuracy | Yes (92%) |
| SWE-bench | Code | 2294 | Pass@k | Yes (varies) |
| OSWorld | Desktop | 369 | Success rate | Yes (72%) |
| ToolBench | APIs | 16000+ | Success rate | No |

---

## LLM-as-Judge Methodology

```python
# LLM-as-Judge for agent evaluation
def llm_judge_evaluation(
    task: str,
    trajectory: list[tuple],
    ground_truth: str,
    judge_model: LLM
) -> dict:
    prompt = f"""Evaluate this agent's performance on the task.

Task: {task}
Expected outcome: {ground_truth}

Agent trajectory:
{format_trajectory(trajectory)}

Rate on these dimensions (1-5):
1. Task completion: Did the agent achieve the goal?
2. Efficiency: Was the path optimal?
3. Reasoning quality: Were actions well-justified?
4. Error recovery: Did the agent handle mistakes well?

Provide scores and brief justifications."""

    evaluation = judge_model.generate(prompt)
    return parse_evaluation(evaluation)

# Calibration against human judgments
def calibrate_judge(judge_model, human_annotations):
    """Ensure LLM judge correlates with human judgments."""
    llm_scores = [judge_model.evaluate(t) for t in test_trajectories]
    human_scores = human_annotations
    correlation = compute_correlation(llm_scores, human_scores)
    return correlation  # Should be > 0.7 for reliable judge
```

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read AgentBench paper (focus on methodology and results)
- [ ] Skimmed WebArena Section 3 (environment design)
- [ ] Reviewed SWE-bench results table
- [ ] Understood the eight AgentBench environments
- [ ] Compared metrics across benchmarks
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to agent architectures from previous weeks

## Notes Template

```markdown
## Agent Evaluation Reading Notes

**Date**: [your date]

### AgentBench Summary
- Eight environments: [list them]
- Key finding: [best model, overall success rate]
- Main failure modes: [list top 3]

### WebArena Summary
- What makes it realistic: [key features]
- Human baseline: [performance %]
- Gap to close: [human - best model]

### Benchmark Comparison
| Benchmark | Focus | Tasks | Best Result |
|-----------|-------|-------|-------------|
| AgentBench | | | |
| WebArena | | | |
| SWE-bench | | | |

### Key Evaluation Challenges
1. [Challenge 1]
2. [Challenge 2]
3. [Challenge 3]

### Metrics Discussion
| Metric | Pros | Cons |
|--------|------|------|
| Success rate | | |
| Pass@k | | |
| LLM-as-judge | | |

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Course
[How does evaluation inform agent design?]
```

## Key Vocabulary

- **Benchmark**: Standardized evaluation suite with tasks and metrics
- **Environment**: Simulated or real world where agent operates
- **Success rate**: Percentage of tasks completed successfully
- **Pass@k**: Probability that any of k attempts succeeds
- **Trajectory**: Sequence of observations and actions
- **Human baseline**: Human performance on benchmark tasks
- **LLM-as-Judge**: Using LLMs to evaluate other LLM outputs
- **Partial credit**: Scoring based on progress toward goal
- **Benchmark saturation**: When top models achieve near-perfect scores
- **Contamination**: Training data leaking into evaluation sets

## Practical Exercise

Design an evaluation suite for a customer service agent:

1. **Task Categories**: What types of tasks should be included?
2. **Success Criteria**: How do you define success for each?
3. **Metrics**: What should be measured?
4. **Human Baseline**: How would you collect human performance?

| Task Type | Example | Success Criterion | Metric |
|-----------|---------|-------------------|--------|
| Information lookup | "What's my order status?" | Correct status returned | Accuracy |
| Problem resolution | "I was charged twice" | Issue resolved | Resolution rate |
| Product recommendation | "What laptop fits my needs?" | Relevant suggestion | User satisfaction |
| Complaint handling | "Your service is terrible" | De-escalation | Sentiment change |
