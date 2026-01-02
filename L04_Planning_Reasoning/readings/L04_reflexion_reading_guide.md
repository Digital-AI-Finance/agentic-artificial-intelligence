# Reading Guide: Reflexion - Language Agents with Verbal Reinforcement Learning

**Week 4 - Planning and Reasoning**

## Paper Details

- **Title**: Reflexion: Language Agents with Verbal Reinforcement Learning
- **Authors**: Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Year**: 2023
- **Venue**: NeurIPS 2023
- **arXiv**: https://arxiv.org/abs/2303.11366
- **Code**: https://github.com/noahshinn024/reflexion

## Paper Classification

- **Type**: Foundational (introduces verbal reinforcement learning paradigm)
- **Impact**: 1000+ citations, basis for self-improving agents
- **Prerequisites**: Understanding of RL concepts, LLM prompting, ReAct pattern

## Why This Paper Matters

Reflexion introduces a fundamentally new approach to agent learning: instead of updating model weights through gradient descent (traditional RL), agents improve through natural language self-reflection. This has profound implications:

1. **No Weight Updates**: Learning happens at inference time through memory
2. **Interpretable Learning**: Reflections are human-readable, auditable
3. **Sample Efficient**: Learns from few failures rather than millions of samples
4. **Transfer Potential**: Reflections may transfer across tasks

This paradigm underlies modern agent self-improvement and enables agents to learn from mistakes without expensive retraining.

---

## Critical Reading Guide

### Before Reading

Answer these questions to prime your reading:

1. **Problem Context**: Why is traditional RL difficult for LLM agents?
   - Weight updates require extensive compute
   - Credit assignment is hard in long trajectories
   - Sample efficiency is poor
   - Learned behaviors aren't interpretable

2. **Prior Work**: How did previous systems enable LLM learning?
   - Fine-tuning on successful demonstrations
   - RLHF with human preferences
   - In-context learning (no persistence)

3. **Your Hypothesis**: How might verbal feedback substitute for gradient updates?

### During Reading

#### Section 1-2: Introduction and Background

- [ ] What is "verbal reinforcement learning"?
- [ ] How does Reflexion differ from traditional RL?
- [ ] What are the three key components of the framework?

**Key Insight**: Natural language reflection provides a form of "semantic gradient" that guides improvement without changing weights.

#### Section 3: Reflexion Framework

**The Three Components**:

| Component | Role | Implementation |
|-----------|------|----------------|
| Actor | Generates actions/solutions | LLM with task prompt |
| Evaluator | Provides success/failure signal | Task-specific (tests, reward model) |
| Self-Reflection | Generates verbal feedback | LLM prompted to analyze failure |

**The Reflexion Loop**:
```
1. Actor attempts task
2. Evaluator determines success/failure
3. If failed: Self-Reflection generates verbal feedback
4. Feedback stored in episodic memory
5. Actor retries with memory context
6. Repeat until success or max attempts
```

- [ ] How is the reflection prompt structured?
- [ ] What information is included in episodic memory?
- [ ] How many attempts are typically allowed?

#### Section 4: Memory Architecture

**Two Memory Types**:

| Memory | Duration | Content | Purpose |
|--------|----------|---------|---------|
| Short-term | Single episode | Current trajectory/scratchpad | Working context |
| Long-term | Across episodes | Accumulated reflections | Learned lessons |

- [ ] How do short-term and long-term memory interact?
- [ ] What is the memory window size?
- [ ] How are older reflections handled?

#### Section 5: Experiments

**Key Results**:

| Task | Baseline | Reflexion | Improvement |
|------|----------|-----------|-------------|
| HumanEval (pass@1) | 80.1% | 91.0% | +10.9% |
| MBPP (pass@1) | 77.1% | 90.0% | +12.9% |
| AlfWorld (success) | 77% | 97% | +20% |
| HotpotQA (EM) | 31% | 56% | +25% |

- [ ] Which tasks show the largest improvement? Why?
- [ ] How many reflection iterations are typically needed?
- [ ] What is the ceiling on improvement?

**Key Figure**: Figure 2 shows accuracy vs. number of attempts
- Note the diminishing returns after 2-3 iterations
- Compare tasks with different improvement curves

#### Section 6: Analysis and Ablations

- [ ] What happens without reflection (just retry)?
- [ ] What makes a reflection useful vs. harmful?
- [ ] What are the failure modes?

**Important Finding**: Reflection quality matters more than quantity. Bad reflections can mislead.

### After Reading

Reflect on these questions:

1. **Limitations Acknowledged**
   - Authors mention: requires capable base model, task-specific evaluators
   - Memory window limits how much can be learned

2. **Unacknowledged Limitations**
   - What happens when reflection is wrong?
   - How do you know when to stop reflecting?
   - Can reflections compound errors?
   - Scalability to very long tasks

3. **Connection to Course**
   - Reflexion is a planning-with-feedback pattern
   - Foundation for self-improving agent loops
   - Connects to LATS, Tree of Thoughts, Self-Refine

---

## Discussion Questions (Seminar)

Prepare to discuss:

1. **Conceptual**
   - Is verbal reflection truly "learning" or just in-context adaptation?
   - What's the relationship between Reflexion and human metacognition?

2. **Technical**
   - How would you design a reflection prompt for a new task?
   - What evaluator designs work best for open-ended tasks?

3. **Practical**
   - When should you use Reflexion vs. fine-tuning?
   - How do you handle tasks where success is hard to evaluate?

4. **Critical**
   - Can Reflexion lead to "reflection hacking" (gaming the evaluator)?
   - What prevents infinite loops of bad reflections?

---

## Key Takeaways to Remember

1. **Verbal RL Formula**:
   ```
   Attempt -> Evaluate -> Reflect -> Store -> Retry
   ```

2. **Key Insight**: Self-generated natural language feedback can substitute for gradient updates in many tasks.

3. **Memory is Crucial**: Without persistent episodic memory, improvements don't accumulate.

4. **Quality over Quantity**: 2-3 good reflections outperform many poor ones.

5. **Task Dependency**: Works best when:
   - Evaluator is reliable (unit tests, clear success criteria)
   - Failures are informative (not random noise)
   - Base model is capable (GPT-4 level)

6. **When to Use Reflexion**:
   - Code generation with tests
   - Reasoning with verifiable answers
   - Decision-making with clear outcomes
   - NOT for open-ended creative tasks

---

## Supplementary Readings

| Paper | Relationship |
|-------|-------------|
| Self-Refine (Madaan et al., 2023) | Similar iterative improvement without persistent memory |
| Chain-of-Thought (Wei et al., 2022) | Foundation for reasoning traces |
| ReAct (Yao et al., 2023) | Combines reasoning and acting |
| LATS (Zhou et al., 2024) | Tree search instead of sequential reflection |
| Inner Monologue (Huang et al., 2022) | Verbal feedback for robotics |

---

## Comparison: Self-Improvement Approaches

| Approach | Memory | Learning Signal | Weight Updates |
|----------|--------|-----------------|----------------|
| Fine-tuning | In weights | Gradient | Yes |
| RLHF | In weights | Human preference | Yes |
| In-context learning | None | Examples | No |
| Self-Refine | None | Self-critique | No |
| Reflexion | Episodic | Self-reflection | No |

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read the full paper (focus on Sections 3-5)
- [ ] Understood the three-component architecture
- [ ] Studied the memory architecture (short-term vs long-term)
- [ ] Reviewed the results table (which tasks improve most?)
- [ ] Compared to Self-Refine (what's different?)
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to ReAct and agent architectures from Week 4

## Notes Template

Use this template for your reading notes:

```markdown
## Reflexion Reading Notes

**Date**: [your date]

### Main Contribution
[1-2 sentences on verbal reinforcement learning]

### The Reflexion Loop
1. Actor does: [what?]
2. Evaluator checks: [what?]
3. Self-Reflection generates: [what?]
4. Memory stores: [what?]

### Memory Architecture
- Short-term: [description]
- Long-term: [description]
- Window size: [value]

### Key Results
| Task | Improvement |
|------|-------------|
| HumanEval | |
| AlfWorld | |
| HotpotQA | |

### Strengths
- [Strength 1]
- [Strength 2]

### Weaknesses
- [Weakness 1]
- [Weakness 2]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Planning Agents
[How does Reflexion enable better planning?]
```

## Implementation Sketch

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ReflexionMemory:
    attempt: int
    action: str
    outcome: str
    reflection: str

class ReflexionAgent:
    def __init__(self, llm, evaluator, max_attempts: int = 3):
        self.llm = llm
        self.evaluator = evaluator
        self.max_attempts = max_attempts
        self.episodic_memory: list[ReflexionMemory] = []

    def solve(self, task: str) -> tuple[str, bool]:
        """Main Reflexion loop."""
        for attempt in range(1, self.max_attempts + 1):
            # Build context from memory
            context = self._build_context()

            # Actor: Generate solution
            solution = self._generate(task, context)

            # Evaluator: Check success
            success, feedback = self.evaluator(solution)

            if success:
                return solution, True

            # Self-Reflection: Generate verbal feedback
            reflection = self._reflect(task, solution, feedback)

            # Store in episodic memory
            self.episodic_memory.append(ReflexionMemory(
                attempt=attempt,
                action=solution,
                outcome=feedback,
                reflection=reflection
            ))

        return solution, False  # Failed after max attempts

    def _reflect(self, task: str, solution: str, feedback: str) -> str:
        """Generate self-reflection on failure."""
        prompt = f"""You attempted to solve this task but failed.
Analyze what went wrong and how to succeed next time.

Task: {task}
Your attempt: {solution}
Feedback: {feedback}

Reflection (2-3 sentences on what went wrong and how to fix it):"""
        return self.llm(prompt)

    def _build_context(self) -> str:
        """Build context from episodic memory."""
        if not self.episodic_memory:
            return ""
        reflections = [m.reflection for m in self.episodic_memory]
        return "Previous reflections:\n" + "\n".join(reflections)
```

## Key Vocabulary

- **Verbal reinforcement**: Learning signal expressed in natural language
- **Episodic memory**: Storage of past experiences and reflections
- **Self-reflection**: Process of analyzing one's own failures
- **Trajectory**: Sequence of actions in an episode
- **Evaluator**: Component that determines success/failure
- **Semantic gradient**: Informal term for direction provided by verbal feedback
