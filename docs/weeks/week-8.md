---
layout: week
title: "Week 8: GraphRAG and Knowledge"
week_number: 8
nav_order: 8
parent: Weeks
---

## Key Concepts

**Knowledge Graphs**: Entity-relationship structures that make implicit relationships explicit and queryable. Represented as triples: (subject, predicate, object).

**GraphRAG**: Microsoft's approach combining knowledge graphs with retrieval-augmented generation. Enables both local (entity-specific) and global (thematic) queries.

**Community Detection**: Using the Leiden algorithm to cluster related entities, enabling hierarchical summarization for global queries.

**Query Routing**: Intelligently matching query types (local vs global) to optimal retrieval strategies.

## Exercise

Build a domain knowledge graph system:
1. Extract entities and relationships from documents using an LLM
2. Construct a queryable knowledge graph with Neo4j or NetworkX
3. Implement community detection with Leiden algorithm
4. Build both local search (entity lookup) and global search (community summaries)
5. Compare performance with vector-based retrieval on multi-hop queries

## Discussion Questions

1. When is graph-based retrieval better than vector search? What query patterns benefit most?
2. How do you handle entity disambiguation when the same entity appears with different names?
3. What are the scaling challenges of knowledge graphs for large corpora?
4. How does the upfront indexing cost of GraphRAG compare to the query benefits?
5. When would a hybrid vector + graph approach be preferred over pure GraphRAG?

## Additional Resources

- [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)
- [NetworkX Documentation](https://networkx.org/)
- [Neo4j Graph Database](https://neo4j.com/)
- [Leiden Algorithm Paper](https://arxiv.org/abs/1810.08473)
