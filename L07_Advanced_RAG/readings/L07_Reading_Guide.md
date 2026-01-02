# Reading Guide: Advanced RAG - Self-RAG and CRAG

**Week 7 - Advanced RAG**

## Primary Readings

### Paper 1: Self-RAG

- **Title**: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- **Authors**: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi
- **Year**: 2023
- **Venue**: ICLR 2024
- **arXiv**: https://arxiv.org/abs/2310.11511
- **Code**: https://github.com/AkariAsai/self-rag

### Paper 2: CRAG

- **Title**: Corrective Retrieval Augmented Generation
- **Authors**: Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2401.15884

## Paper Classification

- **Type**: Applied research (improves RAG reliability)
- **Impact**: Addresses fundamental RAG failure modes
- **Prerequisites**: Understanding of basic RAG, retrieval systems

## Why These Papers Matter

Standard RAG has a fundamental problem: it always retrieves and uses documents, even when retrieval fails. This leads to:
- Hallucinations from irrelevant context
- Confident wrong answers
- No self-awareness of retrieval quality

Self-RAG and CRAG both address this by teaching models to evaluate and correct their own retrieval.

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: What happens when RAG retrieves irrelevant documents?
   - Model may hallucinate from noisy context
   - Correct knowledge in parameters gets overridden
   - No mechanism to detect retrieval failure

2. **Prior Work**: How did earlier RAG systems handle retrieval quality?
   - Assumed all retrieved docs are relevant
   - Simple top-k retrieval without filtering
   - No confidence estimation

3. **Your Hypothesis**: How might a model learn to evaluate its own retrieval?

### During Reading: Self-RAG

#### Key Concepts

**Reflection Tokens**:
Self-RAG trains the model to generate special tokens that indicate:
| Token | Meaning |
|-------|---------|
| [Retrieve] | Should I retrieve for this? |
| [IsRel] | Is this document relevant? |
| [IsSup] | Does generation follow from documents? |
| [IsUse] | Is the overall response useful? |

**Adaptive Retrieval**:
Unlike standard RAG, Self-RAG decides whether to retrieve:
- Simple factual recall: No retrieval needed
- Complex questions: Retrieve and verify
- Ambiguous queries: Retrieve multiple times

#### Reading Checkpoints

- [ ] How are reflection tokens trained? (Section 3)
- [ ] What is the inference algorithm? (Section 4)
- [ ] How does adaptive retrieval work?
- [ ] What tasks show the biggest improvement? (Section 5)

**Key Figure**: Figure 1 shows the Self-RAG inference process
- Note the decision points for retrieval
- Observe how critique tokens guide generation

### During Reading: CRAG

#### Key Concepts

**Retrieval Evaluator**:
A lightweight classifier that scores retrieval quality:
```
query + documents -> {correct, ambiguous, incorrect}
```

**Three-Way Routing**:
| Classification | Action |
|---------------|--------|
| Correct | Use documents directly |
| Ambiguous | Decompose query, re-retrieve |
| Incorrect | Fall back to web search |

**Knowledge Refinement**:
For ambiguous cases, CRAG:
1. Decomposes query into sub-queries
2. Re-retrieves for each sub-query
3. Aggregates refined results

#### Reading Checkpoints

- [ ] How is the retrieval evaluator trained? (Section 3)
- [ ] What features determine correct/ambiguous/incorrect?
- [ ] How does web search fallback work? (Section 4)
- [ ] What is the latency overhead? (Section 5)

### After Reading

Compare the two approaches:

| Aspect | Self-RAG | CRAG |
|--------|----------|------|
| Training | Fine-tune with reflection tokens | Train separate evaluator |
| Retrieval decision | Per-generation | Per-query |
| Fallback | No explicit fallback | Web search |
| Overhead | Reflection tokens add latency | Evaluator adds latency |
| Granularity | Token-level critique | Query-level classification |

---

## Discussion Questions (Seminar)

Prepare to discuss:

1. **Conceptual**
   - When should you use Self-RAG vs CRAG?
   - Is token-level critique better than query-level classification?

2. **Technical**
   - How do you handle the latency overhead of critique generation?
   - What are the failure modes of adaptive retrieval?

3. **Practical**
   - How would you combine these approaches with GraphRAG?
   - What's the right threshold for "incorrect" retrieval?

4. **Critical**
   - Can the model accurately assess its own retrieval quality?
   - What happens when the evaluator is confidently wrong?

---

## Key Takeaways to Remember

### Self-RAG

1. **Reflection Tokens**: Special tokens that enable self-critique
2. **Adaptive Retrieval**: Only retrieve when needed
3. **Key Insight**: Train the model to evaluate itself, not just generate

### CRAG

1. **Three-Way Classification**: correct/ambiguous/incorrect
2. **Fallback Mechanism**: Web search when retrieval fails
3. **Key Insight**: Detect retrieval failure before generation

### When to Use Each

| Scenario | Recommendation |
|----------|----------------|
| General QA | Self-RAG (flexible) |
| Domain-specific | CRAG (cleaner separation) |
| High reliability needed | CRAG (explicit fallback) |
| Low latency needed | Standard RAG (no overhead) |

---

## Supplementary Readings

| Paper | Relationship |
|-------|--------------|
| RAPTOR (Sarthi et al., 2024) | Hierarchical document representation |
| GraphRAG (Edge et al., 2024) | Knowledge graph for retrieval |
| RAG Survey (Gao et al., 2024) | Comprehensive taxonomy |
| Dense Passage Retrieval (Karpukhin et al., 2020) | Foundation for neural retrieval |

---

## Implementation Comparison

```python
# Standard RAG
def standard_rag(query):
    docs = retrieve(query, k=5)
    return generate(query, docs)

# Self-RAG (simplified)
def self_rag(query):
    if needs_retrieval(query):  # [Retrieve] token
        docs = retrieve(query, k=5)
        relevant_docs = [d for d in docs if is_relevant(query, d)]  # [IsRel]
        response = generate(query, relevant_docs)
        if is_supported(response, relevant_docs):  # [IsSup]
            return response
    return generate(query, context=None)

# CRAG (simplified)
def crag(query):
    docs = retrieve(query, k=5)
    quality = evaluate_retrieval(query, docs)

    if quality == "correct":
        return generate(query, docs)
    elif quality == "ambiguous":
        sub_queries = decompose(query)
        refined_docs = [retrieve(sq) for sq in sub_queries]
        return generate(query, merge(refined_docs))
    else:  # incorrect
        web_results = web_search(query)
        return generate(query, web_results)
```

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read Self-RAG Sections 1-4
- [ ] Read CRAG Sections 1-4
- [ ] Understood the reflection token mechanism
- [ ] Understood the three-way classification
- [ ] Compared computational overhead of both approaches
- [ ] Noted 2-3 questions for discussion

## Notes Template

```markdown
## Advanced RAG Reading Notes

**Date**: [your date]

### Self-RAG Summary
- Key contribution: [1 sentence]
- Reflection tokens: [list the 4 tokens and meanings]
- Main improvement: [% improvement on what task?]

### CRAG Summary
- Key contribution: [1 sentence]
- Three actions: [correct/ambiguous/incorrect responses]
- Fallback mechanism: [how does web search work?]

### Comparison
| Aspect | Self-RAG | CRAG |
|--------|----------|------|
| Overhead | | |
| Flexibility | | |
| Reliability | | |

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Course
[How do these relate to agent reliability?]
```

## Key Vocabulary

- **Critique tokens**: Special tokens indicating retrieval/relevance decisions
- **Adaptive retrieval**: Dynamically deciding whether to retrieve
- **Corrective action**: Response to poor retrieval quality
- **Confidence scoring**: Quantifying retrieval quality
- **Query decomposition**: Breaking complex queries into sub-queries
- **Retrieval evaluator**: Model that assesses retrieval quality
- **Knowledge refinement**: Improving retrieved context before generation
