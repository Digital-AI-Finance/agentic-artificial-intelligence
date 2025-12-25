# Reading Guide: Multi-Agent Systems Survey

**Week 5 - Multi-Agent Architectures**

## Paper Details
- **Title**: A Systematic Survey on Large Language Model-based Multi-Agent Collaboration
- **Authors**: Tran et al.
- **Year**: 2025
- **arXiv**: https://arxiv.org/abs/2501.06322

## Why This Paper Matters
Provides comprehensive overview of the emerging field of LLM-based multi-agent systems, covering architectures, communication, and applications.

## Critical Reading Guide

### Before Reading
1. What challenges might arise when multiple LLMs work together?
2. How do human teams coordinate effectively?
3. What existing multi-agent frameworks have you heard of?

### During Reading
1. What are the main categories of multi-agent architectures?
2. How do agents typically communicate?
3. What are the key applications of multi-agent systems?
4. What evaluation methods are used?

### After Reading
1. What are the open challenges identified?
2. How do LLM-based MAS differ from traditional MAS?
3. What research directions seem most promising?

## Key Concepts

### Agent Architectures
- **Centralized**: Single orchestrator controls all agents
- **Hierarchical**: Multi-level management structure
- **Decentralized**: Peer-to-peer communication

### Communication Patterns
- Direct message passing
- Shared memory/blackboard
- Broadcast and subscribe
- Structured protocols

### Role Types
- Orchestrator/Manager
- Specialist/Expert
- Executor/Worker
- Critic/Reviewer

## Discussion Questions

1. **Scalability**: How do systems behave with 10+ agents?
2. **Emergence**: Can useful behaviors emerge from simple rules?
3. **Evaluation**: How should we measure multi-agent performance?
4. **Cost**: What is the token cost overhead of coordination?

## Key Takeaways

- LLM-based MAS enable complex collaborative tasks
- Communication protocol design is critical
- Role specialization improves performance
- Many open challenges remain (robustness, evaluation)

## Related Papers

| Paper | Relationship |
|-------|-------------|
| AutoGen (Wu et al., 2023) | Key framework implementation |
| MetaGPT (Hong et al., 2023) | Software development simulation |
| ChatDev (Qian et al., 2024) | End-to-end code generation |
| CAMEL (Li et al., 2023) | Role-playing communication |

## Implementation Frameworks

| Framework | Key Feature |
|-----------|-------------|
| AutoGen | Conversable agents |
| LangGraph | Graph-based workflows |
| CrewAI | Role-based teams |
| MetaGPT | Structured protocols |
