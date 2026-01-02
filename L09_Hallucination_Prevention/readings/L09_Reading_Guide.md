# Reading Guide: Hallucination Detection and Prevention in Agents

**Week 9 - Hallucination Prevention**

## Primary Reading

### Chain-of-Verification Reduces Hallucination in Large Language Models

- **Title**: Chain-of-Verification Reduces Hallucination in Large Language Models
- **Authors**: Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, et al.
- **Year**: 2023
- **Venue**: arXiv preprint (Meta AI)
- **arXiv**: https://arxiv.org/abs/2309.11495

## Paper Classification

- **Type**: Applied research (hallucination mitigation technique)
- **Impact**: Influential method adopted by practitioners
- **Prerequisites**: Understanding of LLM generation, prompting techniques

## Why This Paper Matters

Hallucinations are the Achilles' heel of LLM agents. CoVe provides a systematic approach to self-verification:

1. **Independent Verification**: Answers verification questions separately to avoid confirmation bias
2. **Decomposition**: Breaks claims into atomic facts for fine-grained checking
3. **Iterative Refinement**: Uses verification results to correct the response

This is essential for building trustworthy agents that can operate with minimal human oversight.

---

## Secondary Readings

### FActScore: Fine-grained Atomic Evaluation of Factual Precision

- **Title**: FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation
- **Authors**: Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, et al.
- **Year**: 2023
- **Venue**: EMNLP 2023
- **arXiv**: https://arxiv.org/abs/2305.14251
- **Code**: https://github.com/shmsw25/FActScore

#### Focus Areas
- Atomic fact decomposition methodology
- Scoring against knowledge sources
- Correlation with human judgments

### Survey of Hallucination in Natural Language Generation

- **Authors**: Ziwei Ji, Nayeon Lee, Rita Frieske, et al.
- **Year**: 2023
- **arXiv**: https://arxiv.org/abs/2202.03629

#### Focus Areas
- Taxonomy of hallucination types (intrinsic vs. extrinsic)
- Causes: data, training, decoding
- Mitigation strategies overview

### Self-Refine: Iterative Refinement with Self-Feedback

- **Authors**: Aman Madaan, Niket Tandon, Prakhar Gupta, et al.
- **Year**: 2023
- **arXiv**: https://arxiv.org/abs/2303.17651

#### Focus Areas
- Iterative self-improvement loop
- Feedback generation strategies
- Stopping criteria

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: Why do LLMs hallucinate?
   - Training data contains errors
   - Model optimizes for fluency, not accuracy
   - No built-in fact-checking mechanism
   - Confident generation regardless of knowledge

2. **Prior Work**: How did earlier systems handle hallucination?
   - Post-hoc fact-checking with external tools
   - Retrieval augmentation (RAG)
   - Uncertainty estimation
   - Human review

3. **Your Hypothesis**: Can models detect their own hallucinations?

### During Reading: CoVe Paper

#### Section 1-2: Introduction and Motivation

- [ ] What is the core insight behind CoVe?
- [ ] Why is "independent" verification important?
- [ ] What types of hallucinations does CoVe target?

**Key Insight**: Self-consistency checking fails because the model tends to confirm its own answers. Independent verification breaks this cycle.

#### Section 3: Chain-of-Verification Method

**The Four-Step Pipeline**:

| Step | Action | Output |
|------|--------|--------|
| 1. Generate | Produce initial response | Draft answer |
| 2. Plan | Create verification questions | Question list |
| 3. Execute | Answer each question independently | Verified facts |
| 4. Refine | Update response based on verification | Final answer |

```python
# CoVe Pipeline (simplified)
def chain_of_verification(query: str, llm) -> str:
    # Step 1: Generate initial response
    draft = llm.generate(query)

    # Step 2: Plan verification questions
    questions = llm.generate(f"""
    Given this response to '{query}':
    {draft}

    Generate questions to verify each factual claim:
    """)

    # Step 3: Execute verification (INDEPENDENTLY)
    verified_facts = []
    for q in questions:
        # Key: Don't show the draft to avoid confirmation bias
        answer = llm.generate(q)  # Independent context
        verified_facts.append((q, answer))

    # Step 4: Refine based on verification
    final = llm.generate(f"""
    Original question: {query}
    Draft response: {draft}
    Verification results: {verified_facts}

    Produce a corrected response:
    """)
    return final
```

- [ ] Why must verification questions be answered independently?
- [ ] How are verification questions generated?
- [ ] What happens when verification conflicts with the draft?

#### Section 4: Experiments

**Key Results**:

| Task | Baseline | +CoVe | Improvement |
|------|----------|-------|-------------|
| List questions | 62% | 78% | +16% |
| Long-form QA | 55% | 71% | +16% |
| Multi-hop reasoning | 48% | 67% | +19% |

- [ ] Which question types benefit most?
- [ ] What is the latency overhead of CoVe?
- [ ] How does CoVe compare to retrieval-based approaches?

### During Reading: FActScore

#### Key Concepts

**Atomic Fact Decomposition**:
```
Original: "Albert Einstein was a German-born physicist who
          developed the theory of relativity and won the Nobel
          Prize in Physics in 1921."

Atomic Facts:
1. Albert Einstein was German-born
2. Albert Einstein was a physicist
3. Albert Einstein developed the theory of relativity
4. Albert Einstein won the Nobel Prize in Physics
5. Albert Einstein won the Nobel Prize in 1921
```

**Scoring**:
```
FActScore = (# supported facts) / (# total facts)
```

- [ ] How is "support" determined?
- [ ] What knowledge sources are used for verification?
- [ ] How does FActScore correlate with human judgment?

### After Reading

Reflect on these questions:

1. **Hallucination Taxonomy**

   | Type | Description | Example | Detection |
   |------|-------------|---------|-----------|
   | Intrinsic | Contradicts source | Misquotes a document | Source comparison |
   | Extrinsic | Unverifiable claim | Made-up statistics | Knowledge lookup |
   | Factual | Wrong facts | Wrong dates, names | Fact-checking |
   | Logical | Invalid reasoning | Non sequitur | Logic verification |
   | Contextual | Contradicts context | Inconsistent with prior turns | Consistency check |

2. **Detection vs. Prevention Trade-offs**

   | Approach | Pros | Cons |
   |----------|------|------|
   | CoVe (Prevention) | Catches errors before output | Latency overhead |
   | FActScore (Detection) | Fine-grained analysis | Post-hoc only |
   | RAG (Prevention) | Grounds in sources | Retrieval failures |
   | Self-Consistency (Detection) | Simple | Confirmation bias |

3. **Agent-Specific Challenges**
   - Tool call hallucinations (calling non-existent functions)
   - State tracking errors (wrong belief about environment)
   - Action sequence hallucinations (impossible action orders)
   - Attribution errors (wrong sources for claims)

---

## Discussion Questions (Seminar)

Prepare to discuss:

### Conceptual
1. Can an LLM accurately judge its own hallucinations?
2. Is hallucination fundamentally solvable, or an inherent limitation?
3. What's the relationship between uncertainty and hallucination?

### Technical
1. How should CoVe handle questions with no verifiable answer?
2. What's the optimal number of verification questions?
3. How do you verify claims that aren't in any knowledge base?
4. When does CoVe make things worse?

### Practical
1. How would you implement hallucination prevention in a production agent?
2. What's the acceptable latency overhead for verification?
3. How do you communicate uncertainty to users?

### Research
1. Can we train models to be less hallucination-prone?
2. What metrics best capture hallucination severity?
3. How should agents handle conflicting sources?

---

## Key Takeaways to Remember

1. **CoVe Formula**:
   ```
   Generate -> Plan Questions -> Verify Independently -> Refine
   ```

2. **Key Insight**: Independent verification breaks the confirmation bias that undermines self-consistency.

3. **Hallucination Types**:
   - Factual: Wrong facts (most studied)
   - Logical: Invalid reasoning
   - Contextual: Contradicts prior context
   - Fabricated: Made-up entities/sources

4. **FActScore's Contribution**: Atomic decomposition enables fine-grained factuality measurement.

5. **For Agents**:
   - Tool calls should be verified against actual API specs
   - State should be independently verified
   - Sources should always be checked

6. **When to Use Each**:
   | Scenario | Recommendation |
   |----------|----------------|
   | High-stakes decisions | CoVe + human review |
   | Factual QA | FActScore + retrieval |
   | Real-time chat | Uncertainty expressions |
   | Code generation | Execution-based verification |

---

## Supplementary Readings

| Paper | Relationship |
|-------|-------------|
| TruthfulQA (Lin et al., 2022) | Benchmark for truthfulness |
| RARR (Gao et al., 2023) | Retrieve and revise approach |
| FactKB (Yin et al., 2023) | Knowledge base for fact verification |
| FLEEK (Bayat et al., 2024) | Factual error detection system |
| SelfCheckGPT (Manakul et al., 2023) | Sampling-based consistency checking |

---

## Hallucination Types Reference

| Type | Example | Detection Approach | Prevention |
|------|---------|-------------------|------------|
| Factual | "Einstein won Nobel in 1920" | External knowledge lookup | Retrieval grounding |
| Logical | "A implies B, B implies C, therefore A implies D" | Logic verification | Chain-of-thought |
| Contextual | "As I mentioned earlier..." (didn't) | Consistency checking | Context tracking |
| Temporal | "In 2024, GPT-3 was released" | Timestamp verification | Date-aware retrieval |
| Fabricated | Made-up citation "Smith et al., 2023" | Source verification | Citation retrieval |
| Entity | Non-existent person/place/thing | Entity linking | Knowledge grounding |
| Numerical | Wrong statistics/calculations | Calculation verification | Calculator tools |
| Attribution | Wrong source for quote | Source verification | Quote retrieval |

---

## Implementation Comparison

```python
# Approach 1: Self-Consistency (weak)
def self_consistency(query: str, llm, n_samples: int = 5) -> str:
    responses = [llm.generate(query) for _ in range(n_samples)]
    # Problem: If model consistently hallucinates, this won't catch it
    return majority_vote(responses)

# Approach 2: CoVe (strong)
def cove(query: str, llm) -> str:
    draft = llm.generate(query)
    questions = extract_verification_questions(draft)

    verified = []
    for q in questions:
        # INDEPENDENT verification (key!)
        answer = llm.generate(q)  # Fresh context
        verified.append({"question": q, "answer": answer})

    return llm.generate(f"Refine {draft} based on {verified}")

# Approach 3: RAG-based (retrieval grounding)
def rag_grounded(query: str, llm, retriever) -> str:
    docs = retriever.search(query)
    return llm.generate(query, context=docs, instruction="Only use provided sources")

# Approach 4: FActScore-based (post-hoc detection)
def factscore_check(response: str, knowledge_base) -> float:
    facts = decompose_to_atomic_facts(response)
    supported = sum(1 for f in facts if knowledge_base.supports(f))
    return supported / len(facts)
```

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read CoVe paper completely (focus on methodology)
- [ ] Read FActScore Sections 1-3
- [ ] Understood the four-step CoVe pipeline
- [ ] Compared detection vs. prevention approaches
- [ ] Identified one real hallucination example you've encountered
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to RAG and grounding from previous weeks

## Notes Template

```markdown
## Hallucination Prevention Reading Notes

**Date**: [your date]

### CoVe Summary
- Four steps: [list them]
- Key insight: [why independent verification?]
- Main improvement: [% on what task?]

### FActScore Summary
- What it measures: [description]
- How it works: [decomposition + scoring]
- Knowledge source: [what's used?]

### Hallucination Taxonomy
| Type | Example | How to Detect |
|------|---------|---------------|
| Factual | | |
| Logical | | |
| Fabricated | | |

### Comparison
| Approach | Pros | Cons |
|----------|------|------|
| CoVe | | |
| FActScore | | |
| RAG | | |

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Agents
[What unique hallucination risks do agents face?]
```

## Key Vocabulary

- **Hallucination**: Model output that is fluent but factually incorrect or unsupported
- **Intrinsic hallucination**: Contradicts the provided source/context
- **Extrinsic hallucination**: Cannot be verified from available sources
- **Atomic fact**: Single, indivisible factual claim
- **FActScore**: Proportion of atomic facts that are supported by sources
- **Chain-of-Verification**: Multi-step self-verification pipeline
- **Independent verification**: Answering verification questions without access to draft
- **Confirmation bias**: Tendency to confirm one's prior beliefs
- **Grounding**: Anchoring generation in verifiable sources

## Practical Exercise

Design a hallucination prevention system for a medical information agent:

1. **High-Risk Claims**: What types of hallucinations are most dangerous?
2. **Verification Sources**: What knowledge bases would you use?
3. **CoVe Adaptation**: How would you modify CoVe for medical queries?
4. **Human-in-Loop**: When should the agent defer to humans?

| Risk Level | Claim Type | Verification Method | Fallback |
|------------|------------|--------------------| ---------|
| Critical | Drug interactions | Multiple DB check | Always human review |
| High | Dosage information | Official guidelines | Pharmacist referral |
| Medium | General health info | Peer-reviewed sources | Disclaimer |
| Low | Lifestyle advice | General knowledge | Standard output |
