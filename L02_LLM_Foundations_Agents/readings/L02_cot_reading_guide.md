# Reading Guide: Chain-of-Thought Prompting

**Week 2 - LLM Foundations for Agents**

## Paper Details

- **Title**: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Authors**: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- **Year**: 2022
- **Venue**: NeurIPS 2022
- **arXiv**: https://arxiv.org/abs/2201.11903
- **Code**: https://github.com/google-research/chain-of-thought

## Paper Classification

- **Type**: Foundational (introduces new prompting paradigm)
- **Impact**: 5000+ citations, transformed how we prompt LLMs for reasoning
- **Prerequisites**: Basic understanding of LLMs, few-shot prompting

## Why This Paper Matters

Chain-of-Thought (CoT) prompting is the foundation of LLM reasoning capabilities. Before CoT, LLMs struggled with multi-step problems. This paper showed that simply including intermediate reasoning steps in examples unlocks emergent reasoning in large models. CoT is the basis for agent "thinking" - the internal reasoning that precedes actions in systems like ReAct.

---

## Critical Reading Guide

### Before Reading

Answer these questions to prime your reading:

1. **Problem Context**: What happens when you ask an LLM a math problem directly?
   - They often jump to wrong answers
   - They miss intermediate steps
   - They can't show their work

2. **Prior Work**: What prompting techniques existed before CoT?
   - Zero-shot prompting (direct question)
   - Few-shot prompting (examples without reasoning)
   - Scratchpad approaches (prior work on intermediate computation)

3. **Your Hypothesis**: How might showing intermediate steps change LLM behavior?

### During Reading

Focus on these aspects:

#### Section 1-2: Introduction and Related Work
- [ ] What is the key observation that motivates CoT?
- [ ] How does CoT differ from standard few-shot prompting?
- [ ] What prior work on reasoning does this build on?

**Key Figure**: Figure 1 shows standard vs CoT prompting
- Note the structure of reasoning traces
- Compare input/output formats

#### Section 3: Chain-of-Thought Prompting
- [ ] What exactly is a "chain of thought"?
- [ ] How are the exemplar reasoning traces created?
- [ ] What makes a good CoT example?

**Key Definition**:
```
Standard: Input -> Output
CoT: Input -> Reasoning Steps -> Output
```

#### Section 4: Experiments

Key experiments to understand:

**Arithmetic Reasoning** (Section 4.1)
- [ ] What benchmarks were used? (GSM8K, SVAMP, etc.)
- [ ] How much does CoT improve over standard prompting?
- [ ] What model sizes were tested?

**Key Results Table**: Table 1
- Note the jump in performance with CoT
- Note that smaller models don't benefit as much

**Commonsense Reasoning** (Section 4.2)
- [ ] Does CoT help on non-math tasks?
- [ ] What types of commonsense reasoning were tested?

**Symbolic Reasoning** (Section 4.3)
- [ ] What are symbolic reasoning tasks?
- [ ] How does CoT perform on out-of-distribution lengths?

#### Section 5: Analysis
- [ ] Why does CoT work? (Authors' hypothesis)
- [ ] What is the effect of model scale?
- [ ] What happens with incorrect reasoning traces?

**Critical Finding**: CoT is an emergent ability
- Only appears at sufficient model scale (~100B parameters)
- Smaller models don't benefit

### After Reading

Reflect on these questions:

1. **Limitations Acknowledged**
   - What limitations do the authors mention?
   - Only works for large models
   - Requires manually written reasoning traces
   - Doesn't guarantee correct reasoning

2. **Unacknowledged Limitations**
   - What limitations are NOT discussed?
   - Reasoning traces can be wrong but plausible
   - No verification of intermediate steps
   - Cost of longer outputs

3. **Connection to Course**
   - How does CoT relate to agent design?
   - CoT = the "thinking" in ReAct's think-act-observe loop
   - Foundation for agent planning and reflection
   - Enables multi-step tool use decisions

4. **Follow-up Work**
   - What papers built on CoT?
   - Self-Consistency (multiple paths, voting)
   - Tree of Thoughts (structured exploration)
   - Zero-shot CoT ("Let's think step by step")

---

## Discussion Questions (Seminar)

Prepare to discuss:

1. **Conceptual**
   - Is CoT teaching LLMs to reason, or just to format outputs differently?
   - What's the relationship between CoT and human step-by-step problem solving?

2. **Technical**
   - Why does CoT only work with large models?
   - How would you create CoT examples for a new task?

3. **Practical**
   - When should you use CoT vs direct prompting?
   - What's the cost-benefit trade-off (more tokens vs better answers)?

4. **Critical**
   - Can an LLM with correct CoT still give wrong final answers?
   - How do you detect when CoT reasoning is flawed?

---

## Key Takeaways to Remember

1. **The CoT Formula**:
   ```
   Few-shot examples + Reasoning traces = Better reasoning
   ```

2. **Key Insight**: Showing intermediate steps in examples causes LLMs to generate intermediate steps, improving accuracy on multi-step problems.

3. **Emergence Threshold**: CoT benefits appear around 100B parameters - smaller models don't show improvement.

4. **When to Use CoT**:
   - Multi-step arithmetic
   - Logical reasoning
   - Planning tasks
   - Any task requiring intermediate computation

5. **When NOT to Use CoT**:
   - Simple factual recall
   - Single-step tasks
   - When latency/cost is critical
   - With smaller models

---

## Supplementary Readings

| Paper | Relationship |
|-------|--------------|
| Wang et al. (2023) "Self-Consistency" | Multiple CoT paths + voting |
| Kojima et al. (2022) "Zero-shot CoT" | "Let's think step by step" trigger |
| Yao et al. (2023) "Tree of Thoughts" | Structured exploration of reasoning |
| Wei et al. (2022) "Emergent Abilities" | Why CoT only works at scale |

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read the full paper (not just abstract)
- [ ] Studied Figure 1 (standard vs CoT prompting)
- [ ] Understood Table 1 (performance comparisons)
- [ ] Tried CoT prompting yourself (ChatGPT, Claude)
- [ ] Noted 2-3 questions for discussion
- [ ] Connected ideas to agent reasoning

## Notes Template

Use this template for your reading notes:

```markdown
## CoT Reading Notes

**Date**: [your date]

### Main Contribution
[1-2 sentences on what CoT is]

### Key Method
[How does CoT prompting work?]

### Results Summary
[Key numbers: improvement on GSM8K, model size threshold]

### Strengths
- [Strength 1]
- [Strength 2]

### Weaknesses
- [Weakness 1]
- [Weakness 2]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Agent Design
[How does CoT enable agent reasoning?]
```

## Practical Exercise

Try these prompts to understand CoT:

**Standard prompting**:
```
Q: A bakery sells 45 cupcakes at $3 each. How much money total?
A:
```

**CoT prompting**:
```
Q: A bakery sells 23 muffins at $2 each. How much money total?
A: The bakery sells 23 muffins at $2 each.
Total = 23 * $2 = $46.
The answer is $46.

Q: A bakery sells 45 cupcakes at $3 each. How much money total?
A:
```

Compare outputs and note the difference.
