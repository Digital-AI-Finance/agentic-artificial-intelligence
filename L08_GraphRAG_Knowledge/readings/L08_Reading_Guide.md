# Reading Guide: GraphRAG and Knowledge Graphs for Agents

**Week 8 - GraphRAG and Knowledge Graphs**

## Primary Reading

### GraphRAG: Unlocking LLM Discovery on Narrative Private Data

- **Title**: From Local to Global: A Graph RAG Approach to Query-Focused Summarization
- **Authors**: Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, et al.
- **Organization**: Microsoft Research
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2404.16130
- **Code**: https://github.com/microsoft/graphrag
- **Blog**: https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/

## Paper Classification

- **Type**: Applied research (novel RAG architecture)
- **Impact**: 15,000+ GitHub stars, production deployments at scale
- **Prerequisites**: Understanding of basic RAG, graph theory, LLM prompting

## Why This Paper Matters

GraphRAG addresses fundamental limitations of vector-based RAG:

1. **Global Queries**: Traditional RAG fails on "What are the main themes across all documents?"
2. **Multi-hop Reasoning**: Finding connections that span multiple documents
3. **Structured Knowledge**: Representing relationships, not just similar chunks
4. **Summarization**: Community detection enables hierarchical abstraction

This represents the evolution from retrieval to knowledge-grounded generation.

---

## Secondary Readings

### Knowledge Graphs Meet Multi-Modal Learning: A Comprehensive Survey

- **Authors**: Shirui Pan, Linhao Luo, Yufei Wang, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2306.08302

#### Focus Areas
- Section 3: Knowledge graph construction from text
- Section 5: KG-enhanced language models
- Figure 2: Taxonomy of approaches

### Graph of Thoughts: Solving Elaborate Problems with Large Language Models

- **Authors**: Maciej Besta, Nils Blach, Ales Kubicek, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2308.09687

#### Focus Areas
- Graph-based reasoning representation
- Comparison with Chain-of-Thought and Tree-of-Thoughts
- Algorithm for thought aggregation

### HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

- **Authors**: Bernal Jimenez Gutierrez, Yiheng Shu, Yu Gu, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2405.14831

#### Focus Areas
- Hippocampal indexing theory for RAG
- Pattern separation and completion
- Personal knowledge graph construction

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: When does vector-based RAG fail?
   - Global questions spanning entire corpus
   - Multi-hop reasoning across documents
   - Questions requiring relationship understanding
   - Summarization of themes/patterns

2. **Prior Work**: How did earlier systems handle knowledge graphs?
   - Entity linking to existing KGs (e.g., Wikidata)
   - Rule-based extraction
   - Supervised relation extraction

3. **Your Hypothesis**: How might graphs enhance RAG systems?

### During Reading: GraphRAG Paper

#### Section 1-2: Introduction and Background

- [ ] What are "sensemaking questions"?
- [ ] How do local vs. global queries differ?
- [ ] What is the "needle in a haystack" limitation?

**Key Insight**: Vector similarity finds local relevance but misses global patterns.

#### Section 3: Graph Construction Pipeline

**The GraphRAG Pipeline**:

```
Documents -> Entity Extraction -> Relationship Extraction ->
Graph Construction -> Community Detection -> Community Summaries
```

| Stage | Method | Output |
|-------|--------|--------|
| Entity Extraction | LLM prompting | Named entities with types |
| Relationship Extraction | LLM prompting | Entity pairs with relations |
| Graph Construction | NetworkX | Knowledge graph |
| Community Detection | Leiden algorithm | Hierarchical communities |
| Summarization | LLM prompting | Community descriptions |

- [ ] How are entities extracted from text?
- [ ] What relationship types are captured?
- [ ] How does the Leiden algorithm work for community detection?

**Key Figure**: Figure 2 shows the indexing pipeline
- Note the multi-level community hierarchy
- Understand how summaries are generated at each level

#### Section 4: Query Processing

**Two Search Modes**:

| Mode | Use Case | Method |
|------|----------|--------|
| Local Search | Specific entity queries | Entity-centric retrieval |
| Global Search | Thematic/summary queries | Community summary search |

```python
# Simplified query routing
def graphrag_search(query: str, graph: KnowledgeGraph):
    if is_local_query(query):
        # Find relevant entities and their neighborhoods
        entities = extract_entities(query)
        subgraph = graph.get_neighborhood(entities, hops=2)
        return generate_from_subgraph(query, subgraph)
    else:
        # Global search: use community summaries
        summaries = graph.get_community_summaries(level="appropriate")
        return synthesize_from_summaries(query, summaries)
```

- [ ] How does local search traverse the graph?
- [ ] How are community summaries selected for global search?
- [ ] What determines the appropriate community level?

#### Section 5: Experiments

**Key Results**:

| Query Type | Vector RAG | GraphRAG | Improvement |
|------------|------------|----------|-------------|
| Global sensemaking | 30-40% | 70-80% | +40% |
| Entity-specific | 75% | 78% | +3% |
| Multi-hop | 45% | 72% | +27% |

- [ ] Which query types benefit most from GraphRAG?
- [ ] What is the computational overhead of graph construction?
- [ ] How does quality scale with corpus size?

### During Reading: Graph of Thoughts

#### Key Concepts

**GoT vs. Other Paradigms**:

| Paradigm | Structure | Backtracking | Aggregation |
|----------|-----------|--------------|-------------|
| Chain-of-Thought | Linear | No | No |
| Tree-of-Thoughts | Tree | Yes | Limited |
| Graph-of-Thoughts | DAG | Yes | Yes |

- [ ] How does GoT enable thought aggregation?
- [ ] What makes a thought a "node" vs. an "edge"?
- [ ] When is GoT better than ToT?

### After Reading

Reflect on these questions:

1. **Trade-offs**
   | Aspect | Vector RAG | GraphRAG |
   |--------|------------|----------|
   | Index time | Fast | Slow (LLM calls) |
   | Index cost | Low | High |
   | Query time | Fast | Medium |
   | Global queries | Poor | Excellent |
   | Maintenance | Easy | Complex |

2. **When to Use GraphRAG**
   - Large document collections requiring global understanding
   - Domains with rich relationships (legal, medical, financial)
   - Applications requiring explainable retrieval
   - Multi-hop reasoning tasks

3. **When NOT to Use GraphRAG**
   - Simple factual lookup
   - Real-time applications (index overhead)
   - Rapidly changing corpora
   - Cost-sensitive deployments

---

## Discussion Questions (Seminar)

Prepare to discuss:

### Conceptual
1. When would you choose GraphRAG over traditional RAG, and vice versa?
2. Is the graph structure actually used, or is it just another way to chunk documents?
3. How does GraphRAG relate to classical knowledge graph systems?

### Technical
1. How do you handle entity disambiguation during extraction?
2. What happens when the Leiden algorithm produces poor communities?
3. How do you update a GraphRAG index incrementally?
4. What's the token cost of graph construction vs. query?

### Practical
1. How would you adapt GraphRAG for specific domains (legal, medical, financial)?
2. What evaluation metrics best capture GraphRAG benefits?
3. How do you explain graph-based retrieval to end users?

### Research
1. What are the most promising directions for combining knowledge graphs with LLMs?
2. How might graph neural networks enhance GraphRAG?
3. Can we learn optimal community hierarchies instead of using Leiden?

---

## Key Takeaways to Remember

1. **The GraphRAG Formula**:
   ```
   Extract entities -> Build graph -> Detect communities ->
   Summarize -> Route queries to local or global search
   ```

2. **Key Insight**: Community-based summaries enable global sensemaking that vector search cannot provide.

3. **Trade-off Triangle**:
   - Quality: GraphRAG wins on global, ties on local
   - Cost: GraphRAG is 10-100x more expensive to index
   - Latency: GraphRAG adds overhead for graph traversal

4. **Community Detection is Key**: The Leiden algorithm creates hierarchical structure that enables multi-resolution retrieval.

5. **Two Search Modes**:
   - Local: Start from query entities, expand neighborhood
   - Global: Match query to community summaries

---

## Supplementary Readings

| Paper | Relationship |
|-------|-------------|
| REALM (Guu et al., 2020) | First retrieval-augmented LM |
| RETRO (Borgeaud et al., 2022) | Chunked cross-attention for retrieval |
| Atlas (Izacard et al., 2022) | Few-shot retrieval-augmented LM |
| RAPTOR (Sarthi et al., 2024) | Tree-structured hierarchical retrieval |
| KAPING (Baek et al., 2023) | Knowledge graph augmented prompting |

---

## Implementation Comparison

```python
# Traditional RAG
def vector_rag(query: str, documents: list[str]) -> str:
    chunks = chunk_documents(documents)
    embeddings = embed(chunks)
    index = build_vector_index(embeddings)

    query_embedding = embed(query)
    similar_chunks = index.search(query_embedding, k=5)
    return generate(query, similar_chunks)

# GraphRAG (simplified)
def graph_rag(query: str, documents: list[str]) -> str:
    # Indexing (expensive, done once)
    entities = extract_entities(documents)
    relations = extract_relations(documents)
    graph = build_graph(entities, relations)
    communities = leiden_clustering(graph)
    summaries = summarize_communities(communities)

    # Query (fast)
    if is_global_query(query):
        relevant_summaries = match_summaries(query, summaries)
        return synthesize(query, relevant_summaries)
    else:
        relevant_entities = find_entities(query)
        subgraph = expand_neighborhood(relevant_entities, graph)
        return generate(query, subgraph)
```

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read the GraphRAG blog post completely
- [ ] Skimmed Sections 1-4 of the technical paper
- [ ] Understood the two search modes (local vs. global)
- [ ] Reviewed Leiden community detection algorithm basics
- [ ] Compared to traditional RAG mentally
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to RAG concepts from Week 7

## Notes Template

```markdown
## GraphRAG Reading Notes

**Date**: [your date]

### Main Contribution
[1-2 sentences on graph-based RAG]

### The Pipeline
1. Entity extraction: [method]
2. Relationship extraction: [method]
3. Community detection: [algorithm]
4. Summarization: [approach]

### Two Search Modes
- Local: [when and how]
- Global: [when and how]

### Key Results
| Query Type | Improvement |
|------------|-------------|
| Global | |
| Multi-hop | |
| Local | |

### Trade-offs vs Vector RAG
| Aspect | Winner |
|--------|--------|
| Index time | |
| Query quality | |
| Cost | |

### Strengths
- [Strength 1]
- [Strength 2]

### Weaknesses
- [Weakness 1]
- [Weakness 2]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Agent Memory
[How does GraphRAG relate to agent knowledge bases?]
```

## Key Vocabulary

- **Knowledge graph**: Graph structure with entities as nodes and relationships as edges
- **Entity extraction**: Identifying named entities (people, places, concepts) in text
- **Relation extraction**: Identifying relationships between entities
- **Community detection**: Grouping densely connected nodes in a graph
- **Leiden algorithm**: State-of-the-art community detection method
- **Global search**: Queries requiring understanding of entire corpus
- **Local search**: Queries about specific entities or facts
- **Sensemaking**: Process of understanding patterns and themes in information
- **Multi-hop reasoning**: Reasoning that requires connecting multiple pieces of information

## Practical Exercise

Design a GraphRAG system for a legal document corpus:

1. **Entity Types**: What entities would you extract? (parties, dates, statutes, courts, ...)
2. **Relationship Types**: What relationships matter? (filed_against, cites, overturns, ...)
3. **Community Structure**: What would communities represent? (case types, legal areas, time periods, ...)
4. **Query Examples**: Write 3 local and 3 global queries for this domain

| Query | Type | Why? |
|-------|------|------|
| "What cases cite Brown v. Board?" | Local | Entity-centric |
| "What are the main themes in employment law?" | Global | Needs synthesis |
| ... | | |
