# Week 8 Exercise: Building a Domain Knowledge Graph

## Objective
Build a GraphRAG system for a specific domain, implementing entity extraction, knowledge graph construction, and graph-based retrieval.

## Learning Outcomes
- Implement LLM-based entity and relationship extraction
- Construct a queryable knowledge graph using NetworkX
- Apply multi-hop reasoning for complex queries
- Compare graph-based vs. vector-based retrieval

## Task Description

### Part 1: Entity Extraction Pipeline (30%)
Create an entity extraction system that:
1. Processes documents from your chosen domain (finance, healthcare, legal, etc.)
2. Extracts entities with types (PERSON, ORG, CONCEPT, EVENT, etc.)
3. Extracts relationships with confidence scores
4. Handles coreference resolution for entity linking

### Part 2: Knowledge Graph Construction (30%)
Build a knowledge graph that:
1. Uses NetworkX DiGraph as the underlying data structure
2. Stores entity metadata (type, description, source document)
3. Stores relationship metadata (type, confidence, evidence)
4. Implements graph statistics (node degree, centrality, communities)

### Part 3: Graph-Based Retrieval (25%)
Implement retrieval functions:
1. Single-hop queries (direct relationships)
2. Multi-hop queries (2-3 hop traversal)
3. Path-finding between entities
4. Subgraph extraction for context building

### Part 4: Evaluation (15%)
Compare your GraphRAG system against baseline RAG:
1. Design 10 test questions requiring multi-hop reasoning
2. Measure answer quality (manual evaluation or LLM-as-judge)
3. Measure retrieval precision and recall
4. Document performance differences

## Deliverables
1. `graphrag_system.py` - Complete implementation
2. `knowledge_graph.json` - Exported graph
3. `evaluation_results.md` - Comparison report
4. `demo.ipynb` - Interactive demonstration

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Entity Extraction | 25 | Accuracy and coverage of extraction |
| Graph Construction | 25 | Proper structure and metadata |
| Retrieval Quality | 25 | Multi-hop reasoning capability |
| Evaluation Rigor | 15 | Meaningful comparison with baseline |
| Code Quality | 10 | Clean, documented, tested code |

## Resources
- NetworkX documentation: https://networkx.org/
- GraphRAG paper (Edge et al., 2024)
- Sample datasets: Wikipedia articles, SEC filings, PubMed abstracts

## Time Estimate
- Minimum: 4 hours
- Expected: 6 hours
- Maximum: 10 hours
