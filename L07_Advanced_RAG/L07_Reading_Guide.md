# Week 7 Reading Guide: Advanced RAG

## Primary Reading

### Self-RAG: Learning to Retrieve, Generate, and Critique
- **Authors**: Asai, A., Wu, Z., Wang, Y., et al.
- **Year**: 2023
- **arXiv**: 2310.11511
- **Link**: https://arxiv.org/abs/2310.11511

#### Key Contributions
- Trained LLM to generate special reflection tokens
- Adaptive retrieval based on query complexity
- Self-critique for quality control

#### Critical Reading Questions
1. How are the reflection tokens trained?
2. What is the computational overhead of critique generation?
3. How does Self-RAG handle conflicting sources?

### Corrective Retrieval Augmented Generation (CRAG)
- **Authors**: Yan, S., et al.
- **Year**: 2024
- **arXiv**: 2401.15884
- **Link**: https://arxiv.org/abs/2401.15884

#### Key Contributions
- Lightweight retrieval evaluator
- Three-way decision (correct/ambiguous/incorrect)
- Web search fallback mechanism

## Secondary Reading

### RAG Survey
- **Authors**: Gao, Y., et al.
- **Year**: 2024
- **arXiv**: 2312.10997
- **Focus**: Comprehensive taxonomy of RAG approaches

### RAPTOR: Recursive Abstractive Processing
- **Authors**: Sarthi, P., et al.
- **Year**: 2024
- **arXiv**: 2401.18059
- **Focus**: Hierarchical document representation

## Discussion Questions

1. When should you use Self-RAG vs CRAG?
2. How do you handle the latency overhead of critique generation?
3. What are the failure modes of adaptive retrieval?
4. How would you combine these approaches with GraphRAG?

## Key Vocabulary

- **Critique tokens**: Special tokens indicating retrieval/relevance decisions
- **Adaptive retrieval**: Dynamically deciding whether to retrieve
- **Corrective action**: Response to poor retrieval quality
- **Confidence scoring**: Quantifying retrieval quality
- **Query decomposition**: Breaking complex queries into sub-queries
