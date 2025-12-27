# Week 6 Reading Guide: Agent Frameworks

## Primary Reading

### AutoGen: Enabling Next-Gen LLM Applications
- **Authors**: Wu, Q., Bansal, G., Zhang, J., et al.
- **Year**: 2023
- **Venue**: arXiv preprint
- **arXiv**: 2308.08155
- **Link**: https://arxiv.org/abs/2308.08155

#### Before Reading
1. What challenges exist in coordinating multiple LLM-powered agents?
2. How do current frameworks handle agent communication?

#### Key Sections
- Section 3: AutoGen Framework Design
- Section 4: Conversation Patterns
- Section 5: Applications and Case Studies

#### After Reading
1. How does AutoGen's conversation-based approach differ from graph-based frameworks?
2. What are the trade-offs of using message passing vs. explicit state management?
3. How does code execution sandboxing work in AutoGen?

## Secondary Reading

### LangGraph Documentation
- **Source**: LangChain
- **Link**: https://langchain-ai.github.io/langgraph
- **Focus**: Conceptual guides and how-to sections

#### Key Concepts
- StateGraph and Message Graph
- Nodes, Edges, and Conditional Routing
- Checkpointing and Persistence
- Human-in-the-loop Patterns

### TaskWeaver: A Code-First Agent Framework
- **Authors**: Qiao, B., et al.
- **Year**: 2024
- **arXiv**: 2311.17541
- **Link**: https://arxiv.org/abs/2311.17541

#### Why Read This
- Different approach: code generation as the primary action
- Interesting comparison to tool-calling approaches

## Classic Reference

### Intelligent Agents: Theory and Practice
- **Authors**: Wooldridge, M. & Jennings, N.
- **Year**: 1995
- **Venue**: Knowledge Engineering Review
- **DOI**: 10.1017/S0269888900008122

#### Historical Context
- Original definitions of intelligent agents
- BDI (Belief-Desire-Intention) architecture
- Multi-agent system foundations

## Discussion Questions

### Conceptual
1. What is the fundamental difference between chain-based and graph-based agent architectures?
2. Why do modern frameworks emphasize state management so heavily?
3. How do conversation-based (AutoGen) vs. state-machine (LangGraph) approaches handle errors differently?

### Technical
1. When should you choose checkpointing granularity at node vs. edge level?
2. How do different frameworks handle tool schema definition?
3. What are the implications of synchronous vs. asynchronous agent execution?

### Research
1. What gaps exist in current framework support for multi-modal agents?
2. How might hierarchical agent architectures be better supported?
3. What evaluation metrics are missing for agent framework comparison?

## Reading Schedule

| Day | Reading | Time |
|-----|---------|------|
| 1 | LangGraph conceptual docs | 45 min |
| 2 | AutoGen paper (Sections 1-3) | 60 min |
| 3 | AutoGen paper (Sections 4-5) | 45 min |
| 4 | TaskWeaver (skim) | 30 min |
| 5 | Wooldridge & Jennings (optional) | 45 min |

## Key Vocabulary

- **StateGraph**: LangGraph's core abstraction for stateful agent graphs
- **Checkpoint**: Serialized snapshot of agent state at a graph node
- **Reducer**: Function that merges state updates in LangGraph
- **ConversableAgent**: AutoGen's base class for agents that can converse
- **GroupChat**: AutoGen pattern for multi-agent conversations
- **Thread**: Isolation boundary for agent conversations (enables multi-tenancy)
