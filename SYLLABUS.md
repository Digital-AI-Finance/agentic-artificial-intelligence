# Agentic Artificial Intelligence - Course Syllabus

## Course Information

- **Level**: PhD/Research
- **Duration**: 12 Weeks
- **Format**: 2h Lecture + 2h Lab per week
- **Prerequisites**: ML fundamentals, Python proficiency

## Learning Outcomes

Upon completion, students will be able to:

1. Design and implement LLM-based autonomous agents
2. Build multi-agent systems for complex problem-solving
3. Develop advanced RAG and knowledge retrieval systems
4. Evaluate agent safety and reliability
5. Apply agentic AI to domain-specific problems

---

## Weekly Schedule

### Module 1: Foundations (Weeks 1-2)

#### Week 1: Introduction to Agentic AI
- Evolution from LLMs to AI agents
- Agent definition: perception, reasoning, action
- The ReAct (Reasoning + Acting) paradigm
- Agent architectures overview

**Reading**: Yao et al. (2023) "ReAct: Synergizing Reasoning and Acting in Language Models"

#### Week 2: LLM Foundations for Agents
- Transformer architecture recap (for agents)
- Prompting strategies for agent behavior
- Chain-of-Thought and Tree-of-Thought reasoning
- Context windows and their implications

**Reading**: Wei et al. (2022) "Chain-of-Thought Prompting Elicits Reasoning"

---

### Module 2: Single-Agent Systems (Weeks 3-4)

#### Week 3: Tool Use and Function Calling
- Model Context Protocol (MCP) architecture
- Function calling patterns (OpenAI, Anthropic, Google)
- Tool schemas and validation
- Error handling and retry strategies

**Lab**: Building a tool-using agent with MCP

#### Week 4: Planning and Reasoning
- Task decomposition strategies
- Hierarchical planning
- Plan verification and self-reflection
- Memory systems (short-term, long-term, episodic)

**Reading**: Shinn et al. (2023) "Reflexion: Language Agents with Verbal Reinforcement Learning"

---

### Module 3: Multi-Agent Systems (Weeks 5-6)

#### Week 5: Multi-Agent Architectures
- Horizontal vs. vertical scaling of agents
- Communication protocols between agents
- Role assignment and specialization
- Coordination mechanisms

**Reading**: Tran et al. (2025) "Multi-Agent Collaboration Mechanisms: A Survey of LLMs"

#### Week 6: Agent Frameworks Deep Dive
- LangGraph: State machines for agents
- AutoGen: Conversation-based collaboration
- CrewAI: Role-based team agents
- Comparative analysis and selection criteria

**Lab**: Building a multi-agent system with LangGraph

**MIDTERM PROJECT DUE**

---

### Module 4: RAG and Knowledge Systems (Weeks 7-8)

#### Week 7: Advanced RAG Architectures
- Beyond basic RAG: Self-RAG and Adaptive RAG
- Long document handling (LongRAG)
- Hybrid retrieval (dense + sparse)
- Query enhancement techniques (RQ-RAG, RAG-Fusion)

**Reading**: Gao et al. (2024) "Retrieval-Augmented Generation: A Comprehensive Survey"

#### Week 8: Knowledge Graphs and GraphRAG
- Knowledge graph construction from text
- GraphRAG: Combining graphs with retrieval
- Multi-hop reasoning with structured knowledge
- Multimodal RAG (text + images)

**Lab**: Building a GraphRAG system

---

### Module 5: Agent Safety and Evaluation (Weeks 9-10)

#### Week 9: Hallucination Prevention and Verification
- Sources of agent hallucinations
- Verification patterns and tools
- Grounding agents in factual sources
- Anti-hallucination testing frameworks

**Lab**: Integration with hallucination-prevention-toolkit

#### Week 10: Agent Evaluation and Benchmarks
- Metrics for agent performance
- Benchmark suites (AgentBench, WebArena)
- Human-in-the-loop evaluation
- Safety testing and red-teaming

**Reading**: Liu et al. (2023) "AgentBench: Evaluating LLMs as Agents"

---

### Module 6: Applications and Research Frontiers (Weeks 11-12)

#### Week 11: Domain Applications
- Agents for software engineering (Devin, Copilot)
- Scientific research agents
- Agents in finance (trading, analysis)
- Healthcare decision support (MDAgents)

**Lab**: Building a domain-specific agent

#### Week 12: Research Frontiers and Course Project
- Emerging research directions
- Agent co-evolution (CoMAS)
- Swarm intelligence with LLMs
- Course project presentations

**FINAL PROJECT PRESENTATIONS**

---

## Grading

| Component | Weight | Description |
|-----------|--------|-------------|
| Weekly Exercises | 30% | 12 exercises, drop lowest 2 |
| Midterm Project | 20% | Multi-agent system implementation |
| Paper Presentation | 15% | Present and discuss research paper |
| Final Project | 35% | Complete agentic AI system |

---

## Required Readings

| Week | Paper | DOI/arXiv |
|------|-------|-----------|
| 1 | ReAct: Synergizing Reasoning and Acting | arXiv:2210.03629 |
| 2 | Chain-of-Thought Prompting Elicits Reasoning | arXiv:2201.11903 |
| 4 | Reflexion: Verbal Reinforcement Learning | arXiv:2303.11366 |
| 5 | Multi-Agent Collaboration: A Survey | arXiv:2501.06322 |
| 7 | RAG: A Comprehensive Survey | arXiv:2312.10997 |
| 8 | GraphRAG | Microsoft Research 2024 |
| 10 | AgentBench | arXiv:2308.03688 |

---

## Tools and Frameworks

- Python 3.10+
- LangChain/LangGraph
- OpenAI/Anthropic APIs
- Vector databases (Chroma, Pinecone)
- Jupyter notebooks

---

## Academic Integrity

All work must be original. Use of AI assistants for ideation is permitted; direct copying is not. Cite all sources.

---

## Office Hours

By appointment. Email instructor to schedule.
