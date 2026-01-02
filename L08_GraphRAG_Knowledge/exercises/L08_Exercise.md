# Exercise L08: Building a Domain Knowledge Graph System

**Week 8 - GraphRAG and Knowledge Integration**

## Overview

Build a GraphRAG system for a specific domain, implementing entity extraction, knowledge graph construction, community detection, and graph-based retrieval that outperforms vector-only approaches on multi-hop queries.

## Learning Objectives

- **Primary (Create)**: Build knowledge graphs from unstructured text using LLMs
- **Secondary (Apply)**: Implement graph-based retrieval with local and global queries
- **Tertiary (Analyze)**: Compare graph-enhanced vs vector-only retrieval strategies

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- NetworkX, chromadb or similar vector store

## Problem Statement

Vector-only RAG struggles with:
- Multi-hop reasoning: "Who founded the company that acquired X?"
- Global queries: "What are the main themes across all documents?"
- Relationship traversal: "How are entities A and B connected?"

GraphRAG addresses these by building explicit structure before retrieval.

### Task 1: Entity Extraction Pipeline (30 points)

Create an entity extraction system using LLMs:

**Requirements:**
1. Process documents from a domain (finance, healthcare, legal, or your choice)
2. Extract entities with types: PERSON, ORG, CONCEPT, EVENT, PRODUCT, LOCATION
3. Extract relationships with labels and confidence scores
4. Handle coreference resolution ("Apple", "the company", "it" -> same entity)

**Extraction Prompt Template:**
```
Extract all entities and relationships from this text.

Text: {chunk}

Return as JSON:
{
  "entities": [
    {"name": "...", "type": "PERSON|ORG|...", "description": "..."}
  ],
  "relationships": [
    {"source": "...", "target": "...", "relation": "...", "confidence": 0.0-1.0}
  ]
}
```

**Test Dataset:**
Use one of:
- 10+ Wikipedia articles on a topic (e.g., AI companies)
- SEC 10-K filings (finance)
- PubMed abstracts (healthcare)
- Legal case summaries

**Deliverable**: `entity_extractor.py` with extraction functions.

### Task 2: Knowledge Graph Construction (25 points)

Build a queryable knowledge graph:

**Requirements:**
1. Use NetworkX DiGraph as the underlying structure
2. Store entity metadata: type, description, source documents
3. Store relationship metadata: type, confidence, evidence text
4. Handle entity resolution (merge duplicate entities)

**Graph Schema:**
```python
# Node attributes
node = {
    "type": "PERSON",
    "description": "Co-founder of Apple Inc.",
    "source_docs": ["doc1.txt", "doc2.txt"],
    "mentions": 15
}

# Edge attributes
edge = {
    "relation": "FOUNDED",
    "confidence": 0.95,
    "evidence": "Steve Jobs co-founded Apple in 1976",
    "source_doc": "doc1.txt"
}
```

**Graph Statistics to Implement:**
```python
def graph_statistics(G: nx.DiGraph) -> dict:
    return {
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
        "avg_degree": sum(dict(G.degree()).values()) / G.number_of_nodes(),
        "most_connected": sorted(G.degree(), key=lambda x: x[1], reverse=True)[:10],
        "num_communities": ...,  # Using Leiden/Louvain
    }
```

### Task 3: Community Detection and Summarization (20 points)

Implement hierarchical community detection for global queries:

**Requirements:**
1. Apply Leiden algorithm (or Louvain) for community detection
2. Generate LLM summaries for each community
3. Build multi-level hierarchy: documents -> entities -> communities -> global

**Community Summary Prompt:**
```
This community contains the following entities and relationships:

Entities: {entity_list}
Key relationships: {relationship_list}

Write a 2-3 sentence summary of what this community represents.
```

**Hierarchy Structure:**
```
Level 0: Individual entities
Level 1: Small communities (5-20 entities)
Level 2: Larger communities (merged Level 1)
Level 3: Global summary (all communities)
```

### Task 4: Query Routing and Retrieval (25 points)

Implement intelligent query routing:

**Local Search (Entity-specific queries):**
```python
def local_search(query: str, G: nx.DiGraph) -> list[str]:
    """
    1. Extract entities from query
    2. Find matching nodes in graph
    3. Traverse 1-2 hops to collect context
    4. Return relevant text chunks
    """
    pass
```

**Global Search (Thematic queries):**
```python
def global_search(query: str, community_summaries: dict) -> str:
    """
    1. Classify query as local vs global
    2. For global: search community summaries
    3. Aggregate and synthesize answer
    """
    pass
```

**Query Classification:**
```
Local queries: "What did X say about Y?", "When did X happen?"
Global queries: "What are the main themes?", "Summarize the key findings"
```

**Test Queries (10 total):**
| Query | Type | Expected Behavior |
|-------|------|-------------------|
| "Who founded Apple?" | Local | Entity lookup + relationship |
| "What products did Apple release?" | Local | Multi-hop traversal |
| "What are the main themes in AI development?" | Global | Community summary aggregation |
| "How are Google and DeepMind connected?" | Local | Path finding |
| "Summarize the competitive landscape" | Global | Cross-community synthesis |

## Evaluation: Graph vs Vector Comparison

Compare your GraphRAG against baseline vector RAG:

**Baseline Implementation:**
```python
def vector_rag(query: str, documents: list[str]) -> str:
    # Standard RAG: embed query, retrieve top-k, generate
    pass
```

**Comparison Metrics:**
| Metric | Description |
|--------|-------------|
| Answer correctness | Manual evaluation or LLM-as-judge |
| Multi-hop success | Can answer 2-3 hop queries |
| Global query quality | Coherence of thematic answers |
| Retrieval precision | Relevant chunks retrieved |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| entity_extractor.py | Python | Complete extraction pipeline |
| knowledge_graph.py | Python | Graph construction + queries |
| knowledge_graph.json | JSON | Exported graph data |
| evaluation_results.md | Markdown | Comparison with vector RAG |
| demo.ipynb | Jupyter | Interactive demonstration |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Entity Extraction | 25 | Accuracy and coverage |
| Graph Construction | 20 | Proper structure and metadata |
| Community Detection | 15 | Working hierarchical summaries |
| Query Routing | 20 | Correct local/global handling |
| Evaluation Rigor | 10 | Meaningful comparison |
| Code Quality | 10 | Clean, documented code |

### Detailed Rubric

**Entity Extraction (25 points)**
- 10 points: Entities correctly identified
- 5 points: Types correctly assigned
- 5 points: Relationships extracted
- 5 points: Coreference handled

**Graph Construction (20 points)**
- 10 points: Valid graph structure
- 5 points: Metadata complete
- 5 points: Entity resolution works

**Community Detection (15 points)**
- 10 points: Communities identified
- 5 points: Summaries generated

**Query Routing (20 points)**
- 10 points: Local search works
- 5 points: Global search works
- 5 points: Routing logic correct

**Evaluation (10 points)**
- 5 points: Fair comparison
- 5 points: Insights documented

**Code Quality (10 points)**
- 5 points: Well-documented
- 5 points: Error handling

## Resources

- Edge et al. (2024). "From Local to Global: GraphRAG" - arXiv:2404.16130
- NetworkX documentation: https://networkx.org/
- Leiden algorithm: https://github.com/vtraag/leidenalg
- Microsoft GraphRAG: https://microsoft.github.io/graphrag/

## Submission

- **Format**: Python files + Jupyter notebook + Markdown report
- **Filename**: `L08_exercise_[your_name]/`
- **Due**: End of Week 8

## Hints

- Start with a small corpus (5-10 documents) before scaling
- Entity resolution is tricky - use fuzzy matching or embeddings
- Cache LLM calls for entity extraction (expensive!)
- Test local queries before implementing global search

## Sample Graph Visualization

```python
import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G: nx.DiGraph, highlight_community=None):
    pos = nx.spring_layout(G)
    colors = ['red' if G.nodes[n].get('community') == highlight_community else 'blue'
              for n in G.nodes()]
    nx.draw(G, pos, node_color=colors, with_labels=True, font_size=8)
    plt.title(f"Knowledge Graph ({G.number_of_nodes()} nodes)")
    plt.savefig("graph_viz.png")
```

## Time Estimate
- Minimum: 6 hours
- Expected: 8 hours
- Maximum: 12 hours
