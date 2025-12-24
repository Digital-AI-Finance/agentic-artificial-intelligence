# Agentic Artificial Intelligence

PhD-level course on LLM-based autonomous agents, multi-agent systems, and advanced RAG architectures.

## Course Overview

This 12-week course covers the theory and practice of building intelligent agents powered by large language models. Students will learn to design, implement, and evaluate autonomous systems that can reason, plan, and act in complex environments.

## Prerequisites

- Machine Learning fundamentals
- Python proficiency (3.10+)
- Experience with LLM APIs (OpenAI, Anthropic)
- Basic knowledge of transformers and attention mechanisms

## Course Structure

| Module | Weeks | Topics |
|--------|-------|--------|
| Foundations | 1-2 | Agent definition, ReAct, LLM prompting, CoT/ToT |
| Single-Agent Systems | 3-4 | Tool use (MCP), planning, memory, Reflexion |
| Multi-Agent Systems | 5-6 | Architectures, LangGraph, AutoGen, CrewAI |
| RAG & Knowledge | 7-8 | Advanced RAG, GraphRAG, knowledge graphs |
| Safety & Evaluation | 9-10 | Hallucination prevention, benchmarks, red-teaming |
| Applications | 11-12 | Domain agents, research frontiers, projects |

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up API keys (OpenAI, Anthropic, etc.)
4. Navigate to lesson folders for materials

## Repository Structure

```
agentic-artificial-intelligence/
|-- L01_Introduction_Agentic_AI/
|   |-- L01_Introduction_Agentic_AI.tex
|   |-- 01_agent_definition/
|   |   |-- chart.py
|   |   |-- chart.pdf
|   |-- notebooks/
|   |-- exercises/
|   |-- readings/
|-- L02_LLM_Foundations_Agents/
|-- ...
|-- L12_Research_Frontiers/
|-- tools/
|   |-- hallucination_checks/
|   |-- quality/
|-- datasets/
|-- SYLLABUS.md
|-- PROGRESS_TRACKER.md
|-- requirements.txt
```

## Tools & Frameworks

- **LangGraph**: State machine-based agent framework
- **AutoGen**: Conversation-based multi-agent
- **CrewAI**: Role-based team agents
- **MCP**: Model Context Protocol for tool use

## Evaluation

| Component | Weight |
|-----------|--------|
| Weekly Exercises | 30% |
| Midterm Project (Week 6) | 20% |
| Paper Presentation | 15% |
| Final Project | 35% |

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Anthropic MCP](https://docs.anthropic.com/en/docs/build-with-claude/mcp)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

## Contributing

See SYLLABUS.md for course schedule and PROGRESS_TRACKER.md for development status.

## License

Educational use only. Contact instructor for permissions.
