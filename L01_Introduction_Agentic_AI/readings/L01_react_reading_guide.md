# Reading Guide: ReAct Paper

**Week 1 - Introduction to Agentic AI**

## Paper Details

- **Title**: ReAct: Synergizing Reasoning and Acting in Language Models
- **Authors**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Year**: 2023
- **Venue**: ICLR 2023 (International Conference on Learning Representations)
- **arXiv**: https://arxiv.org/abs/2210.03629
- **Code**: https://github.com/ysymyth/ReAct

## Paper Classification

- **Type**: Foundational (introduces new paradigm)
- **Impact**: 2000+ citations, foundational for LLM agents
- **Prerequisites**: Basic understanding of LLMs, prompting

## Why This Paper Matters

ReAct is arguably the most influential paper in the LLM agent space. It introduced the idea of interleaving reasoning traces with actions, which has become the standard approach for building agents. Nearly every agent framework (LangChain, AutoGen, etc.) implements some variant of ReAct.

---

## Critical Reading Guide

### Before Reading

Answer these questions to prime your reading:

1. **Problem Context**: What are the limitations of using LLMs in a "one-shot" manner for complex tasks?

2. **Prior Work**: What approaches existed before ReAct?
   - Chain-of-Thought (CoT) prompting: Reasoning without action
   - Action-only approaches: Acting without explicit reasoning

3. **Your Hypothesis**: How might combining reasoning and acting improve LLM performance?

### During Reading

Focus on these aspects:

#### Section 1-2: Introduction and Related Work
- [ ] What is the key insight that motivates ReAct?
- [ ] How does ReAct differ from CoT prompting?
- [ ] How does ReAct differ from action-only approaches?

#### Section 3: ReAct Method
- [ ] What are the three components of ReAct? (Thought, Action, Observation)
- [ ] How is the prompt structured?
- [ ] What is the role of "thoughts" in the reasoning process?

**Key Figure**: Figure 1 shows the ReAct paradigm
- Compare the reasoning trace vs action trace vs ReAct trace
- Note how thoughts provide context for actions

#### Section 4: Experiments
- [ ] What tasks were used for evaluation?
  - HotpotQA (multi-hop QA)
  - FEVER (fact verification)
  - ALFWorld (text-based games)
  - WebShop (web navigation)
- [ ] What baselines were compared?
- [ ] What metrics were used?

**Key Results Table**: Table 1
- ReAct vs CoT vs Act on HotpotQA
- Note the improvement from combining approaches

#### Section 5: Analysis
- [ ] What types of errors does ReAct make?
- [ ] How does ReAct handle hallucination?
- [ ] What is the effect of few-shot examples?

### After Reading

Reflect on these questions:

1. **Limitations Acknowledged**
   - What limitations do the authors mention?
   - Cost of additional tokens for reasoning traces
   - Need for task-specific prompts

2. **Unacknowledged Limitations**
   - What limitations are NOT discussed?
   - Scalability to longer tasks
   - Error propagation in multi-step reasoning
   - Evaluation on truly open-ended tasks

3. **Connection to Course**
   - How does ReAct relate to the agent definition we discussed?
   - ReAct implements the perception-action-reasoning loop
   - Thoughts = internal reasoning, Actions = external operations

4. **Follow-up Work**
   - What papers have built on ReAct?
   - Reflexion (self-reflection)
   - LATS (tree search with ReAct)
   - Self-RAG (retrieval-augmented ReAct)

---

## Discussion Questions (Seminar)

Prepare to discuss:

1. **Conceptual**
   - Why is interleaving thoughts with actions better than separate reasoning and acting?
   - What role do "thoughts" play that couldn't be achieved implicitly?

2. **Technical**
   - How would you extend ReAct to handle tasks requiring hundreds of steps?
   - What happens when the LLM generates an invalid action?

3. **Practical**
   - In what scenarios would ReAct fail?
   - How would you evaluate a ReAct agent in production?

4. **Critical**
   - Is the improvement from ReAct due to the paradigm or just having more tokens?
   - How do the authors control for this?

---

## Key Takeaways to Remember

1. **The ReAct Formula**: Thought -> Action -> Observation -> Thought -> ...

2. **Key Insight**: Explicit reasoning traces help LLMs:
   - Plan actions
   - Track progress
   - Handle exceptions
   - Provide interpretability

3. **Trajectory Definition**:
   ```
   τ = (s₀, t₁, a₁, o₁, t₂, a₂, o₂, ..., tₙ, aₙ, oₙ)
   ```

4. **When to Use ReAct**:
   - Multi-step reasoning tasks
   - Tasks requiring external knowledge
   - Tasks needing interpretable reasoning

5. **Limitations**:
   - Token cost (thoughts add overhead)
   - Error propagation
   - Requires good few-shot examples

---

## Supplementary Readings

| Paper | Relationship |
|-------|--------------|
| Wei et al. (2022) "Chain-of-Thought" | Foundation for reasoning traces |
| Wang et al. (2024) "LLM Agent Survey" | Comprehensive overview of agent approaches |
| Shinn et al. (2023) "Reflexion" | Extends ReAct with self-reflection |
| Zhou et al. (2024) "LATS" | Tree search over ReAct trajectories |

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read the full paper (not just abstract)
- [ ] Studied Figures 1 and 2 carefully
- [ ] Understood the experimental setup
- [ ] Noted 2-3 questions for discussion
- [ ] Connected ideas to lecture content

## Notes Template

Use this template for your reading notes:

```markdown
## ReAct Reading Notes

**Date**: [your date]

### Main Contribution
[1-2 sentences]

### Key Method
[How does ReAct work?]

### Results Summary
[Key numbers from experiments]

### Strengths
- [Strength 1]
- [Strength 2]

### Weaknesses
- [Weakness 1]
- [Weakness 2]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Course
[How does this relate to lecture content?]
```
