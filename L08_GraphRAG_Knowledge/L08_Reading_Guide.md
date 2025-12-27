# Week 8 Reading Guide: GraphRAG and Knowledge Graphs

## Primary Reading

### GraphRAG: Unlocking LLM Discovery on Narrative Private Data
**Authors**: Edge, D., Trinh, H., Cheng, N., et al.
**Organization**: Microsoft Research
**Year**: 2024
**Link**: https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/

#### Key Concepts
- Graph-based indexing for RAG systems
- Community detection for document summarization
- Global vs. local search strategies
- Entity extraction and relationship modeling

#### Critical Reading Questions
1. How does GraphRAG address the "needle in a haystack" problem differently than vector search?
2. What are the computational trade-offs of graph construction vs. vector indexing?
3. How does community detection enable global summarization?

---

## Secondary Readings

### Knowledge Graphs Meet Multi-Modal Learning: A Comprehensive Survey
**Authors**: Pan, S., Luo, L., Wang, Y., et al.
**Year**: 2024
**arXiv**: 2306.08302

#### Focus Areas
- Section 3: Knowledge graph construction from text
- Section 5: KG-enhanced language models
- Figure 2: Taxonomy of approaches

### Graph of Thoughts: Solving Elaborate Problems with Large Language Models
**Authors**: Besta, M., et al.
**Year**: 2024
**arXiv**: 2308.09687

#### Focus Areas
- Graph-based reasoning representation
- Comparison with Chain-of-Thought and Tree-of-Thoughts
- Algorithm for thought aggregation

### HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models
**Authors**: Gutierrez, B. J., et al.
**Year**: 2024
**arXiv**: 2405.14831

#### Focus Areas
- Hippocampal indexing theory for RAG
- Pattern separation and completion
- Personal knowledge graph construction

---

## Discussion Questions

### For Seminar
1. **Architecture Trade-offs**: When would you choose GraphRAG over traditional RAG, and vice versa?

2. **Scalability**: How do knowledge graphs scale with corpus size? What are the computational bottlenecks?

3. **Quality vs. Coverage**: How do you balance entity extraction precision against recall? What are the downstream effects?

4. **Domain Adaptation**: How would you adapt GraphRAG for specific domains (legal, medical, financial)?

5. **Future Directions**: What are the most promising directions for combining knowledge graphs with LLMs?

---

## Practical Exercises

### Before Class
1. Read the GraphRAG blog post completely
2. Skim Sections 1-3 of the Knowledge Graph survey
3. Prepare one question about graph-based reasoning

### After Class
1. Implement the entity extraction component from your reading
2. Compare extraction quality across domains
3. Document three insights from the papers

---

## Related Papers

| Paper | Relationship | Notes |
|-------|--------------|-------|
| REALM (Guu et al., 2020) | Foundational | First retrieval-augmented LM |
| RETRO (Borgeaud et al., 2022) | Architecture | Chunked cross-attention |
| Atlas (Izacard et al., 2022) | Training | Few-shot RAG |
| RAPTOR (Sarthi et al., 2024) | Hierarchical | Tree-structured retrieval |

---

## Key Takeaways
1. Knowledge graphs provide structured, interpretable retrieval
2. Graph construction is expensive but enables new query types
3. Community detection enables global summarization
4. Hybrid approaches (graph + vector) often outperform either alone
