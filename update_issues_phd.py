"""
PhD-Level Issue Enhancement Script
Updates all 81 issues with research depth, Bloom's taxonomy, and technical specifications
"""

import subprocess
import json
import re

# Research papers by week (verified arXiv/DOI)
PAPERS = {
    1: [
        {"title": "ReAct: Synergizing Reasoning and Acting in Language Models", "authors": "Yao et al.", "year": 2023, "venue": "ICLR 2023", "link": "https://arxiv.org/abs/2210.03629"},
        {"title": "A Survey on Large Language Model based Autonomous Agents", "authors": "Wang et al.", "year": 2024, "venue": "Frontiers of CS", "link": "https://arxiv.org/abs/2308.11432"},
        {"title": "The Rise and Potential of Large Language Model Based Agents", "authors": "Xi et al.", "year": 2023, "venue": "arXiv", "link": "https://arxiv.org/abs/2309.07864"},
        {"title": "Language Agents: From Next-Token Prediction to Digital Automation", "authors": "Sumers et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2403.12897"},
    ],
    2: [
        {"title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "authors": "Wei et al.", "year": 2022, "venue": "NeurIPS 2022", "link": "https://arxiv.org/abs/2201.11903"},
        {"title": "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", "authors": "Yao et al.", "year": 2023, "venue": "NeurIPS 2023", "link": "https://arxiv.org/abs/2305.10601"},
        {"title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models", "authors": "Wang et al.", "year": 2023, "venue": "ICLR 2023", "link": "https://arxiv.org/abs/2203.11171"},
        {"title": "Large Language Models are Zero-Shot Reasoners", "authors": "Kojima et al.", "year": 2022, "venue": "NeurIPS 2022", "link": "https://arxiv.org/abs/2205.11916"},
    ],
    3: [
        {"title": "Toolformer: Language Models Can Teach Themselves to Use Tools", "authors": "Schick et al.", "year": 2023, "venue": "NeurIPS 2023", "link": "https://arxiv.org/abs/2302.04761"},
        {"title": "API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs", "authors": "Li et al.", "year": 2023, "venue": "EMNLP 2023", "link": "https://arxiv.org/abs/2304.08244"},
        {"title": "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs", "authors": "Qin et al.", "year": 2024, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2307.16789"},
        {"title": "Gorilla: Large Language Model Connected with Massive APIs", "authors": "Patil et al.", "year": 2023, "venue": "arXiv", "link": "https://arxiv.org/abs/2305.15334"},
    ],
    4: [
        {"title": "Reflexion: Language Agents with Verbal Reinforcement Learning", "authors": "Shinn et al.", "year": 2023, "venue": "NeurIPS 2023", "link": "https://arxiv.org/abs/2303.11366"},
        {"title": "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning", "authors": "Wang et al.", "year": 2023, "venue": "ACL 2023", "link": "https://arxiv.org/abs/2305.04091"},
        {"title": "Language Agent Tree Search Unifies Reasoning Acting and Planning", "authors": "Zhou et al.", "year": 2024, "venue": "ICML 2024", "link": "https://arxiv.org/abs/2310.04406"},
        {"title": "Reasoning with Language Model is Planning with World Model", "authors": "Hao et al.", "year": 2023, "venue": "EMNLP 2023", "link": "https://arxiv.org/abs/2305.14992"},
    ],
    5: [
        {"title": "Multi-Agent Collaboration Mechanisms: A Survey of LLMs", "authors": "Tran et al.", "year": 2025, "venue": "arXiv", "link": "https://arxiv.org/abs/2501.06322"},
        {"title": "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", "authors": "Wu et al.", "year": 2023, "venue": "arXiv", "link": "https://arxiv.org/abs/2308.08155"},
        {"title": "MetaGPT: Meta Programming for Multi-Agent Collaborative Framework", "authors": "Hong et al.", "year": 2023, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2308.00352"},
        {"title": "ChatDev: Communicative Agents for Software Development", "authors": "Qian et al.", "year": 2024, "venue": "ACL 2024", "link": "https://arxiv.org/abs/2307.07924"},
    ],
    6: [
        {"title": "LangGraph: Building Stateful Multi-Actor Applications", "authors": "LangChain Team", "year": 2024, "venue": "Documentation", "link": "https://langchain-ai.github.io/langgraph"},
        {"title": "Intelligent Agents: Theory and Practice", "authors": "Wooldridge & Jennings", "year": 1995, "venue": "Knowledge Engineering Review", "link": "https://doi.org/10.1017/S0269888900008122"},
        {"title": "TaskWeaver: A Code-First Agent Framework for Seamlessly Planning and Executing Data Analytics Tasks", "authors": "Qiao et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2311.17541"},
        {"title": "CrewAI: Building Autonomous AI Agent Teams", "authors": "CrewAI Team", "year": 2024, "venue": "Documentation", "link": "https://docs.crewai.com"},
    ],
    7: [
        {"title": "Retrieval-Augmented Generation for Large Language Models: A Survey", "authors": "Gao et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2312.10997"},
        {"title": "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection", "authors": "Asai et al.", "year": 2023, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2310.11511"},
        {"title": "Corrective Retrieval Augmented Generation (CRAG)", "authors": "Yan et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2401.15884"},
        {"title": "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval", "authors": "Sarthi et al.", "year": 2024, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2401.18059"},
    ],
    8: [
        {"title": "From Local to Global: A Graph RAG Approach to Query-Focused Summarization", "authors": "Edge et al.", "year": 2024, "venue": "Microsoft Research", "link": "https://arxiv.org/abs/2404.16130"},
        {"title": "Unifying Large Language Models and Knowledge Graphs: A Roadmap", "authors": "Pan et al.", "year": 2024, "venue": "IEEE TKDE", "link": "https://arxiv.org/abs/2306.08302"},
        {"title": "Graph of Thoughts: Solving Elaborate Problems with Large Language Models", "authors": "Besta et al.", "year": 2024, "venue": "AAAI 2024", "link": "https://arxiv.org/abs/2308.09687"},
        {"title": "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models", "authors": "Gutierrez et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2405.14831"},
    ],
    9: [
        {"title": "Survey of Hallucination in Natural Language Generation", "authors": "Ji et al.", "year": 2023, "venue": "ACM Computing Surveys", "link": "https://arxiv.org/abs/2202.03629"},
        {"title": "FActScore: Fine-grained Atomic Evaluation of Factual Precision", "authors": "Min et al.", "year": 2023, "venue": "EMNLP 2023", "link": "https://arxiv.org/abs/2305.14251"},
        {"title": "Chain-of-Verification Reduces Hallucination in Large Language Models", "authors": "Dhuliawala et al.", "year": 2023, "venue": "arXiv", "link": "https://arxiv.org/abs/2309.11495"},
        {"title": "Self-Refine: Iterative Refinement with Self-Feedback", "authors": "Madaan et al.", "year": 2023, "venue": "NeurIPS 2023", "link": "https://arxiv.org/abs/2303.17651"},
    ],
    10: [
        {"title": "AgentBench: Evaluating LLMs as Agents", "authors": "Liu et al.", "year": 2023, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2308.03688"},
        {"title": "WebArena: A Realistic Web Environment for Building Autonomous Agents", "authors": "Zhou et al.", "year": 2024, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2307.13854"},
        {"title": "GAIA: A Benchmark for General AI Assistants", "authors": "Mialon et al.", "year": 2024, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2311.12983"},
        {"title": "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", "authors": "Jimenez et al.", "year": 2024, "venue": "ICLR 2024", "link": "https://arxiv.org/abs/2310.06770"},
    ],
    11: [
        {"title": "Devin: AI Software Engineer", "authors": "Cognition AI", "year": 2024, "venue": "Technical Report", "link": "https://www.cognition.ai/blog/introducing-devin"},
        {"title": "AlphaCodium: From Prompt Engineering to Flow Engineering", "authors": "Ridnik et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2401.08500"},
        {"title": "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making", "authors": "Kim et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2404.15488"},
        {"title": "A Survey on Large Language Model based Autonomous Agents in Finance", "authors": "Li et al.", "year": 2024, "venue": "arXiv", "link": "https://arxiv.org/abs/2402.18485"},
    ],
    12: [
        {"title": "Building Effective Agents", "authors": "Anthropic", "year": 2024, "venue": "Technical Report", "link": "https://www.anthropic.com/research/building-effective-agents"},
        {"title": "Voyager: An Open-Ended Embodied Agent with Large Language Models", "authors": "Wang et al.", "year": 2023, "venue": "arXiv", "link": "https://arxiv.org/abs/2305.16291"},
        {"title": "Generative Agents: Interactive Simulacra of Human Behavior", "authors": "Park et al.", "year": 2023, "venue": "UIST 2023", "link": "https://arxiv.org/abs/2304.03442"},
        {"title": "Constitutional AI: Harmlessness from AI Feedback", "authors": "Bai et al.", "year": 2022, "venue": "arXiv", "link": "https://arxiv.org/abs/2212.08073"},
    ],
}

# Slide content templates per week
SLIDES_CONTENT = {
    1: {
        "title": "Introduction to Agentic AI",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define agent, tool use, ReAct paradigm, and orchestration
- **Understand**: Explain the difference between LLM inference and agentic behavior
- **Apply**: Implement a basic ReAct agent using LangChain
- **Analyze**: Compare reactive vs. deliberative agent architectures
- **Evaluate**: Critically assess capabilities and limitations of current LLM agents
- **Create**: Design an agent architecture for a novel problem domain""",
        "definitions": """## Technical Content

### Formal Definitions
- **Agent**: An autonomous entity that perceives its environment through sensors and acts upon it through actuators to achieve goals (Russell & Norvig, 2021)
- **LLM Agent**: An agent where the core reasoning and decision-making is performed by a Large Language Model
- **ReAct Paradigm**: Reasoning + Acting - interleaving reasoning traces with action execution

### Key Algorithms
- **ReAct Loop**: Thought -> Action -> Observation -> Thought...
- **Agent Decision Cycle**: Perceive -> Plan -> Act -> Reflect

### Mathematical Formulation
- Action selection: $a_t = \\pi(s_t, h_{<t})$ where $h$ is the interaction history
- ReAct trajectory: $\\tau = (s_0, t_1, a_1, o_1, t_2, a_2, ...)$""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Course Overview + Learning Objectives
2. What is an Agent? Historical Context (Russell & Norvig)
3. From LLMs to Agents: The Capability Gap
4. Agent Definition: Perception-Action-Environment Loop
5. ReAct Paradigm: Reasoning + Acting (Yao et al., 2023)
6. ReAct Cycle Visualization (Chart 01)
7. Agent vs. LLM Comparison (Chart 02)
8. Agent Architectures Taxonomy
9. Key Components: Memory, Tools, Planning
10. Current Landscape: Commercial and Research Agents
11. Capabilities and Limitations Analysis
12. Research Frontiers and Open Problems
13. Evaluation Challenges
14. Course Roadmap: 12-Week Overview
15. Summary and Key Takeaways"""
    },
    2: {
        "title": "LLM Foundations for Agents",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define Chain-of-Thought, Tree-of-Thoughts, and Self-Consistency
- **Understand**: Explain how reasoning emerges from prompting strategies
- **Apply**: Implement various prompting techniques for complex reasoning
- **Analyze**: Compare effectiveness of different prompting strategies
- **Evaluate**: Assess trade-offs between reasoning depth and computational cost
- **Create**: Design custom prompting strategies for domain-specific tasks""",
        "definitions": """## Technical Content

### Formal Definitions
- **Chain-of-Thought (CoT)**: Prompting technique that elicits intermediate reasoning steps before final answer
- **Tree-of-Thoughts (ToT)**: Extension allowing exploration of multiple reasoning paths
- **Self-Consistency**: Sampling multiple reasoning paths and marginalizing to find most consistent answer

### Key Algorithms
- CoT: $P(answer|question) = \\sum_{chain} P(answer|chain) P(chain|question)$
- ToT: BFS/DFS over thought tree with state evaluation
- Self-Consistency: $\\hat{a} = \\arg\\max_a \\sum_i \\mathbb{1}[a_i = a]$

### Mathematical Formulation
- Reasoning complexity: O(n) for CoT, O(b^d) for ToT where b=branching, d=depth
- Self-Consistency voting: Majority vote over k sampled chains""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Why LLM Foundations Matter for Agents
3. Chain-of-Thought Prompting (Wei et al., 2022)
4. CoT vs ToT Comparison (Chart)
5. Tree-of-Thoughts: Deliberate Problem Solving
6. Self-Consistency: Ensemble Reasoning
7. Zero-Shot Reasoning: "Let's think step by step"
8. Context Window Management
9. Context Window Impact Visualization (Chart)
10. Prompt Engineering for Agents
11. Few-Shot Learning in Agent Contexts
12. Temperature and Sampling Strategies
13. Performance vs. Cost Trade-offs
14. Practical Guidelines for Agent LLM Usage
15. Summary and Key Takeaways"""
    },
    3: {
        "title": "Tool Use and Function Calling",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define function calling, MCP protocol, and tool augmentation
- **Understand**: Explain how LLMs learn to use external tools
- **Apply**: Implement tool-using agents with OpenAI and Anthropic APIs
- **Analyze**: Compare different tool integration approaches
- **Evaluate**: Assess tool selection strategies and error handling
- **Create**: Design custom tools and integrate them into agent workflows""",
        "definitions": """## Technical Content

### Formal Definitions
- **Function Calling**: Structured method for LLMs to invoke external functions with typed parameters
- **Model Context Protocol (MCP)**: Anthropic's open protocol for tool integration
- **Toolformer**: Self-supervised approach for LLMs to learn tool usage

### Key Algorithms
- Tool Selection: $t^* = \\arg\\max_t P(success|query, t, context)$
- API Retrieval: Dense retrieval over API documentation embeddings
- Error Recovery: Retry with feedback loop

### Protocol Specifications
- MCP Transport: JSON-RPC 2.0 over stdio/HTTP
- OpenAI Function Format: JSON Schema for parameters""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Why Tools Matter: Extending LLM Capabilities
3. Toolformer: Self-Supervised Tool Learning
4. MCP Architecture Diagram (Chart)
5. Model Context Protocol Deep Dive
6. Function Calling: OpenAI vs Anthropic
7. Tool Calling Sequence (Chart)
8. Tool Definition Best Practices
9. Error Handling and Retry Strategies
10. API-Bank Benchmark Results
11. ToolLLM: Scaling to 16K+ APIs
12. Gorilla: API-Optimized LLMs
13. Security Considerations
14. Building Custom Tools
15. Summary and Key Takeaways"""
    },
    4: {
        "title": "Planning and Reasoning",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define planning, task decomposition, and Reflexion
- **Understand**: Explain how agents learn from verbal reinforcement
- **Apply**: Implement planning agents with task decomposition
- **Analyze**: Compare different planning paradigms (LATS, Plan-and-Solve)
- **Evaluate**: Assess planning quality and success metrics
- **Create**: Design hierarchical planning systems""",
        "definitions": """## Technical Content

### Formal Definitions
- **Planning**: Process of generating action sequences to achieve goals
- **Reflexion**: Verbal reinforcement learning through self-reflection
- **LATS**: Language Agent Tree Search - MCTS-style planning for LLMs

### Key Algorithms
- Hierarchical Decomposition: Goal -> Subgoals -> Actions
- Reflexion: Act -> Evaluate -> Reflect -> Update Memory
- LATS: Selection -> Expansion -> Evaluation -> Backpropagation

### Mathematical Formulation
- Value function: $V(s) = \\max_a [R(s,a) + \\gamma V(s')]$
- Reflexion memory update: $m_{t+1} = f(m_t, trajectory, feedback)$""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Planning in AI: Historical Overview
3. From Classical to LLM-Based Planning
4. Hierarchical Planning Diagram (Chart)
5. Task Decomposition Strategies
6. Reflexion: Learning from Verbal Feedback
7. Memory Types Comparison (Chart)
8. LATS: Tree Search for Language Agents
9. Plan-and-Solve Prompting
10. World Models and Simulation
11. Evaluation of Plans
12. Multi-Step Reasoning Chains
13. Failure Recovery and Re-planning
14. Practical Implementation Patterns
15. Summary and Key Takeaways"""
    },
    5: {
        "title": "Multi-Agent Architectures",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define multi-agent systems, coordination, and communication protocols
- **Understand**: Explain different agent coordination mechanisms
- **Apply**: Implement multi-agent message passing systems
- **Analyze**: Compare hierarchical vs. peer-to-peer topologies
- **Evaluate**: Assess emergent behaviors and coordination efficiency
- **Create**: Design novel multi-agent architectures for complex tasks""",
        "definitions": """## Technical Content

### Formal Definitions
- **Multi-Agent System (MAS)**: System of multiple interacting intelligent agents
- **Coordination**: Mechanisms for organizing agent activities
- **Emergence**: Complex behaviors arising from simple agent interactions

### Key Algorithms
- Message Passing: $m_{i \\to j} = f(state_i, task, history)$
- Consensus: Iterative agreement protocols
- Task Allocation: Auction-based or centralized assignment

### Topologies
- Star (Manager-Worker), Mesh (Peer-to-Peer), Hierarchical""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Multi-Agent Systems: Definition and History
3. Communication Topology Diagram (Chart)
4. Communication Patterns in MAS
5. Coordination Mechanisms
6. Agent Role Matrix (Chart)
7. Role Specialization and Division of Labor
8. AutoGen: Multi-Agent Conversation
9. MetaGPT: Software Development Team
10. ChatDev: Communicative Agents
11. Emergent Behaviors in MAS
12. Failure Modes and Recovery
13. Scalability Considerations
14. Design Patterns for MAS
15. Summary and Key Takeaways"""
    },
    6: {
        "title": "Agent Frameworks Deep Dive",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define LangGraph, CrewAI, AutoGen architectures
- **Understand**: Explain state management in agent workflows
- **Apply**: Build production agents using framework APIs
- **Analyze**: Compare framework trade-offs and use cases
- **Evaluate**: Select appropriate frameworks for specific requirements
- **Create**: Extend frameworks with custom components""",
        "definitions": """## Technical Content

### Formal Definitions
- **LangGraph**: Graph-based state machine for multi-step agents
- **CrewAI**: Framework for role-based agent teams
- **AutoGen**: Conversational multi-agent framework

### State Management
- LangGraph State: TypedDict with reducers
- Checkpointing: Save/resume workflow state
- Human-in-the-loop: Interrupt and resume patterns

### API Specifications
- LangGraph: StateGraph, add_node, add_edge, compile
- CrewAI: Agent, Task, Crew, Process
- AutoGen: AssistantAgent, UserProxyAgent, GroupChat""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Framework Landscape Overview
3. LangGraph State Machine (Chart)
4. LangGraph: Building Stateful Workflows
5. LangGraph Code Patterns
6. Framework Decision Tree (Chart)
7. CrewAI: Role-Based Teams
8. CrewAI Implementation Patterns
9. AutoGen: Conversation-Based Agents
10. TaskWeaver: Code-First Approach
11. Framework Comparison Matrix
12. Production Considerations
13. When to Use Each Framework
14. Migration and Interoperability
15. Summary and Key Takeaways"""
    },
    7: {
        "title": "Advanced RAG Architectures",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define Self-RAG, CRAG, RAPTOR, and adaptive retrieval
- **Understand**: Explain self-reflection in retrieval augmentation
- **Apply**: Implement Self-RAG with critique and revision
- **Analyze**: Compare retrieval strategies for different use cases
- **Evaluate**: Assess retrieval quality and answer faithfulness
- **Create**: Design adaptive RAG pipelines for production""",
        "definitions": """## Technical Content

### Formal Definitions
- **Self-RAG**: RAG with self-reflection for retrieval and generation quality
- **CRAG**: Corrective RAG with retrieval quality assessment
- **RAPTOR**: Recursive abstractive processing for hierarchical retrieval

### Key Algorithms
- Self-RAG Tokens: [Retrieve], [ISREL], [ISSUP], [ISUSE]
- RAPTOR Clustering: Hierarchical summarization tree
- Adaptive Retrieval: Dynamic decision to retrieve

### Evaluation Metrics
- Faithfulness: Answer grounded in retrieved context
- Relevance: Retrieved documents address query
- Answer Quality: Correctness and completeness""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. RAG Evolution: From Basic to Advanced
3. Self-RAG Architecture (Chart)
4. Self-RAG: Critique and Revision
5. Self-RAG Special Tokens
6. Hybrid Retrieval Comparison (Chart)
7. CRAG: Corrective Retrieval
8. RAPTOR: Hierarchical Retrieval
9. Adaptive Retrieval Strategies
10. Dense vs. Sparse Retrieval
11. Hybrid Search Implementation
12. Long Document Handling
13. RAG Evaluation Frameworks
14. Production RAG Patterns
15. Summary and Key Takeaways"""
    },
    8: {
        "title": "Knowledge Graphs and GraphRAG",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define knowledge graphs, entities, relations, and GraphRAG
- **Understand**: Explain graph-based retrieval advantages
- **Apply**: Build knowledge graphs from unstructured text
- **Analyze**: Compare vector-based vs. graph-based retrieval
- **Evaluate**: Assess multi-hop reasoning capabilities
- **Create**: Design hybrid retrieval systems combining KGs and vectors""",
        "definitions": """## Technical Content

### Formal Definitions
- **Knowledge Graph**: G = (V, E) where V = entities, E = typed relations
- **GraphRAG**: RAG using graph structures for context retrieval
- **Multi-hop Reasoning**: Traversing multiple graph edges for inference

### Key Algorithms
- Entity Extraction: NER + Coreference Resolution
- Relation Extraction: Transformer-based RE models
- Graph Traversal: BFS/DFS for subgraph retrieval

### Mathematical Formulation
- Triple representation: (h, r, t) - head, relation, tail
- Embedding: f: V -> R^d, g: E -> R^d""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Knowledge Graphs: Fundamentals
3. GraphRAG Pipeline (Chart)
4. Microsoft GraphRAG Approach
5. Entity and Relation Extraction
6. Multi-hop Reasoning Visualization (Chart)
7. Graph Construction from Text
8. Community Detection in KGs
9. Summarization for Global Queries
10. Graph of Thoughts Integration
11. HippoRAG: Neurobiologically Inspired
12. Vector + Graph Hybrid Systems
13. Evaluation of GraphRAG
14. Implementation Considerations
15. Summary and Key Takeaways"""
    },
    9: {
        "title": "Hallucination Prevention",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define hallucination types, grounding, and verification
- **Understand**: Explain causes and detection methods for hallucinations
- **Apply**: Implement verification pipelines and fact-checking
- **Analyze**: Compare grounding techniques and their effectiveness
- **Evaluate**: Assess trade-offs between creativity and factuality
- **Create**: Design comprehensive anti-hallucination systems""",
        "definitions": """## Technical Content

### Formal Definitions
- **Hallucination**: Generated content unfaithful to source or factually incorrect
- **Intrinsic Hallucination**: Contradicts source document
- **Extrinsic Hallucination**: Cannot be verified from source

### Key Algorithms
- FActScore: Atomic fact extraction + verification
- Chain-of-Verification: Generate -> Verify -> Revise
- Self-Refine: Iterative improvement with self-feedback

### Detection Methods
- Entailment checking, Source attribution, Confidence calibration""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Hallucination Taxonomy
3. Verification Pipeline Diagram (Chart)
4. Detection Methods Overview
5. FActScore: Atomic Fact Verification
6. Grounding Techniques Comparison (Chart)
7. Chain-of-Verification Approach
8. Self-Refine: Iterative Improvement
9. Source Attribution Methods
10. Retrieval-Based Grounding
11. Confidence Calibration
12. Tool-Based Verification
13. Human-in-the-Loop Verification
14. Production Safeguards
15. Summary and Key Takeaways"""
    },
    10: {
        "title": "Agent Evaluation",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Define benchmarks, metrics, and evaluation frameworks
- **Understand**: Explain agent evaluation challenges
- **Apply**: Implement benchmarking suites for agent systems
- **Analyze**: Compare agent performance across benchmarks
- **Evaluate**: Critically assess benchmark limitations
- **Create**: Design evaluation criteria for novel agent capabilities""",
        "definitions": """## Technical Content

### Formal Definitions
- **AgentBench**: Comprehensive LLM-as-agent benchmark
- **WebArena**: Realistic web environment benchmark
- **GAIA**: General AI Assistant benchmark

### Key Metrics
- Task Success Rate, Step Efficiency, Error Recovery
- Generalization to unseen tasks
- Human preference ratings

### Evaluation Dimensions
- Capability, Reliability, Safety, Efficiency""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Agent Evaluation Challenges
3. Metric Taxonomy Diagram (Chart)
4. Key Metrics for Agents
5. Benchmark Comparison Matrix (Chart)
6. AgentBench Deep Dive
7. WebArena: Web Navigation
8. GAIA: General AI Assistants
9. SWE-bench: Code Agents
10. Red-Teaming and Safety
11. Human Evaluation Methods
12. Automated Evaluation
13. Benchmark Limitations
14. Designing Custom Evaluations
15. Summary and Key Takeaways"""
    },
    11: {
        "title": "Domain Applications",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Identify key domain-specific agent applications
- **Understand**: Explain domain-specific challenges and requirements
- **Apply**: Build specialized agents for specific domains
- **Analyze**: Compare agent architectures across domains
- **Evaluate**: Assess real-world deployment considerations
- **Create**: Design novel domain-specific agent solutions""",
        "definitions": """## Technical Content

### Domain: Software Engineering
- Code generation, debugging, test writing
- Devin, GitHub Copilot, AlphaCodium

### Domain: Healthcare
- Clinical decision support, medical reasoning
- MDAgents: Adaptive collaboration for diagnosis

### Domain: Finance
- Market analysis, risk assessment, trading
- FinAgent: LLM-based financial agents

### Key Challenges
- Domain knowledge, compliance, reliability""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Domain Agent Landscape
3. Domain Agent Comparison (Chart)
4. Software Engineering Agents
5. Devin: AI Software Engineer
6. GitHub Copilot Architecture
7. AlphaCodium: Flow Engineering
8. Healthcare Agents Overview
9. MDAgents: Medical Decision-Making
10. Finance Agents Overview
11. FinAgent Capabilities
12. Regulatory Considerations
13. Deployment Challenges
14. Success Metrics by Domain
15. Summary and Key Takeaways"""
    },
    12: {
        "title": "Research Frontiers",
        "objectives": """## Learning Objectives (Bloom's Taxonomy)

- **Remember**: Identify frontier research directions in agentic AI
- **Understand**: Explain open problems and challenges
- **Apply**: Formulate research questions and hypotheses
- **Analyze**: Compare research approaches and methodologies
- **Evaluate**: Critically assess potential impact and feasibility
- **Create**: Develop novel research proposals""",
        "definitions": """## Technical Content

### Frontier Topics
- Agent-Agent Learning (Voyager, Generative Agents)
- Constitutional AI and Safety
- Long-term Memory and Continual Learning
- Embodied Agents and World Models

### Open Problems
- Scalable alignment, Compositional generalization
- Multi-modal agents, Physical world interaction

### Research Methodology
- Ablation studies, Human evaluations, Benchmark design""",
        "slide_structure": """## Slide Structure (15 slides)

1. Title + Learning Objectives
2. Research Frontier Overview
3. Future Directions Roadmap (Chart)
4. Voyager: Open-Ended Agents
5. Generative Agents: Social Simulation
6. Constitutional AI: Safety
7. Agent-Agent Learning
8. Long-Term Memory Research
9. Embodied AI Agents
10. Multi-Modal Agents
11. Scalability Challenges
12. Alignment and Safety
13. Research Methodology
14. Project Showcase Criteria
15. Course Summary and Next Steps"""
    }
}

def format_papers_table(week):
    """Format papers as markdown table"""
    papers = PAPERS.get(week, [])
    if not papers:
        return ""

    table = """## Required Readings

| Paper | Authors | Year | Venue | Link |
|-------|---------|------|-------|------|
"""
    for p in papers:
        table += f"| {p['title']} | {p['authors']} | {p['year']} | {p['venue']} | [{p['link'].split('/')[-1]}]({p['link']}) |\n"
    return table

def get_week_from_title(title):
    """Extract week number from issue title"""
    match = re.search(r'L(\d+)', title)
    if match:
        return int(match.group(1))
    return None

def generate_slides_body(title, week):
    """Generate enhanced SLIDES issue body"""
    content = SLIDES_CONTENT.get(week, {})
    papers = format_papers_table(week)

    body = f"""# {title}

{content.get('objectives', '## Learning Objectives\n- To be defined')}

{content.get('definitions', '## Technical Content\n- To be defined')}

{papers}

{content.get('slide_structure', '## Slide Structure\n- To be defined')}

## Acceptance Criteria
- [ ] All DOIs/arXiv links verified and accessible
- [ ] Mathematical notation consistent with course conventions
- [ ] Zero LaTeX overflow warnings after compilation
- [ ] Minimum 3 citations per major conceptual claim
- [ ] Learning objectives cover all Bloom's taxonomy levels
- [ ] Each slide has max 4 bullet points
- [ ] All charts generated and integrated

## Technical Requirements
- LaTeX: Beamer with Madrid theme
- Font size: 8pt minimum
- Chart width: 0.55-0.65\\textwidth
- Python: 3.11+
- Chart libraries: matplotlib>=3.7.0, networkx>=3.0
"""
    return body

def generate_notebook_body(title, week):
    """Generate enhanced NOTEBOOK issue body"""
    papers = format_papers_table(week)

    body = f"""# {title}

## Learning Objectives
- Implement core algorithms from research papers
- Reproduce key experimental results
- Extend baseline implementations with enhancements
- Apply best practices for production-ready code

## Technical Requirements

### Environment
```yaml
Python: 3.11+
Key Libraries:
  - langchain>=0.1.0
  - langchain-openai>=0.0.5
  - langchain-anthropic>=0.1.0
  - langgraph>=0.0.20
  - openai>=1.0.0
  - anthropic>=0.7.0
  - chromadb>=0.4.0
  - networkx>=3.0
APIs:
  - OpenAI API (gpt-4-turbo)
  - Anthropic API (claude-3-opus)
Hardware: CPU sufficient, GPU optional for embeddings
```

### Architecture
```
notebook/
+-- imports and configuration
+-- data preparation
+-- core implementation
+-- experimentation
+-- visualization
+-- extension exercises
```

## Implementation Sections

### 1. Setup and Configuration (10 min)
- Environment verification
- API key configuration (from .env)
- Dependency installation check
- Logging setup

### 2. Core Implementation (30 min)
- Algorithm implementation matching paper specifications
- Step-by-step code with inline documentation
- Unit tests for core functions
- Error handling for API failures

### 3. Experimentation (20 min)
- Baseline reproduction
- Parameter ablation studies
- Performance measurement
- Result visualization

### 4. Extension Exercise (Optional, 30 min)
- Advanced modification suggestions
- Open-ended exploration prompts

## Expected Outputs
- Working implementation of core algorithm
- Reproduced results within 5% of paper baselines
- Visualizations comparing different approaches
- Performance metrics logged

{papers}

## Acceptance Criteria
- [ ] Runs in < 15 min on standard hardware (no GPU required)
- [ ] Reproduces paper results within 5% margin
- [ ] All cells have docstrings and inline comments
- [ ] Error handling for API failures and rate limits
- [ ] .env.example provided for API keys
- [ ] Requirements.txt with pinned versions
- [ ] Clear markdown explanations between code cells
"""
    return body

def generate_chart_body(title, week):
    """Generate enhanced CHART issue body"""
    body = f"""# {title}

## Visualization Purpose
This chart visualizes a key concept from Week {week} to support student understanding during lectures.
The visualization should be self-explanatory with clear labels and legend.

## Technical Specifications
```python
# Chart Parameters
figsize = (10, 6)
dpi = 150

# Color Palette (ML Course Standard)
MLPURPLE = '#3333B2'
MLLAVENDER = '#ADADE0'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'

# Font Sizes (scaled for 70% display)
plt.rcParams.update({{
    'font.size': 14,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'legend.fontsize': 13
}})
```

## Design Requirements
- [ ] Single figure (no subplots)
- [ ] All labels readable at 0.55\\textwidth
- [ ] Consistent notation with slides
- [ ] Legend if more than 2 elements
- [ ] Title matches slide terminology
- [ ] White background for PDF embedding
- [ ] Tight layout with no clipping

## Implementation
```
Folder Structure:
L{week:02d}_*/
+-- {title.split(':')[0].lower().replace(' ', '_')}/
    +-- chart.py
    +-- chart.pdf (generated)
```

### Chart.py Template
```python
\"\"\"
{title}
Week {week} - Course Visualization
\"\"\"
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ... implementation ...

plt.savefig(Path(__file__).parent / 'chart.pdf',
            dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
```

## Acceptance Criteria
- [ ] Generates valid PDF without errors
- [ ] PDF embeds correctly in Beamer
- [ ] All text readable at 0.65\\textwidth
- [ ] Color-blind accessible palette
- [ ] No matplotlib deprecation warnings
"""
    return body

def generate_exercise_body(title, week):
    """Generate enhanced EXERCISE issue body"""
    papers = format_papers_table(week)

    body = f"""# {title}

## Exercise Type
- [x] Implementation Challenge
- [ ] Paper Replication
- [ ] System Design
- [ ] Research Proposal

## Learning Objectives (Bloom's Level)
- **Primary**: Create - Design and implement a novel solution
- **Secondary**: Analyze - Compare approaches and trade-offs
- **Tertiary**: Evaluate - Assess solution quality and limitations

## Problem Statement

### Background
Students will apply concepts from Week {week} to build a working system.
This exercise reinforces theoretical concepts through hands-on implementation.

### Task Description
[Detailed problem description with formal notation where applicable]

### Constraints
- Time limit: 2-4 hours
- Must use provided starter code
- API usage within free tier limits
- Must include test coverage

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| Implementation | Python notebook | Working code with documentation |
| Report | Markdown (500 words) | Design decisions and analysis |
| Test Results | pytest output | >80% coverage |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical Correctness | 40 | Code runs without errors, produces correct output |
| Innovation/Insight | 25 | Novel approaches, thoughtful extensions |
| Documentation | 20 | Clear explanations, proper docstrings |
| Reproducibility | 15 | Others can run your code, dependencies documented |

## Resources Provided
- Starter code: `L{week:02d}_*/exercises/starter.py`
- Test framework: `L{week:02d}_*/exercises/test_solution.py`
- Example data: `datasets/week{week:02d}/`

{papers}

## Estimated Time
- Minimum: 2 hours (basic implementation)
- Expected: 3 hours (with documentation)
- Maximum: 4 hours (with extensions)

## Submission Guidelines
- Submit via GitHub Classroom
- Include README with setup instructions
- All dependencies in requirements.txt
"""
    return body

def generate_reading_body(title, week):
    """Generate enhanced READING issue body"""
    papers = PAPERS.get(week, [])
    primary_paper = papers[0] if papers else {"title": "TBD", "authors": "TBD", "year": "TBD", "venue": "TBD", "link": "TBD"}

    body = f"""# {title}

## Paper Details
- **Title**: {primary_paper.get('title', 'TBD')}
- **Authors**: {primary_paper.get('authors', 'TBD')}
- **Year**: {primary_paper.get('year', 'TBD')}
- **Venue**: {primary_paper.get('venue', 'TBD')}
- **Link**: {primary_paper.get('link', 'TBD')}

## Paper Classification
- **Type**: Foundational / Survey / Empirical / Theoretical
- **Impact**: Key paper in the field
- **Prerequisites**: Weeks 1-{week-1} content

## Critical Reading Guide

### Before Reading
1. What problem does this paper address?
2. What is the state-of-the-art before this paper?
3. What would you expect the solution to look like?

### During Reading
1. What is the key technical contribution?
2. What assumptions does the method make?
3. What are the experimental baselines?
4. What metrics are used for evaluation?
5. How do the results compare to prior work?

### After Reading
1. What are the limitations acknowledged by authors?
2. What limitations are NOT acknowledged?
3. How does this connect to Week {week} topics?
4. What follow-up work has built on this?

## Discussion Questions (for seminar)
1. How does this approach compare to alternatives discussed in class?
2. What would you change in the experimental setup?
3. How applicable is this to real-world systems?
4. What are the ethical implications?

## Additional Readings for Week {week}

| Paper | Relationship |
|-------|--------------|
"""
    for p in papers[1:]:
        body += f"| [{p['title']}]({p['link']}) | Extends/Complements primary reading |\n"

    body += """
## Preparation Checklist
- [ ] Read abstract and introduction
- [ ] Skim methodology section
- [ ] Study key figures and tables
- [ ] Read conclusion
- [ ] Prepare 2-3 discussion questions
- [ ] Note connections to course material
"""
    return body

def generate_project_body():
    """Generate enhanced PROJECT issue body"""
    body = """# Final Project Presentations

## Project Overview
The final project demonstrates mastery of agentic AI concepts through original research or engineering work.
Students work in teams of 2-3 to develop a novel contribution.

## Project Types

### Option A: Research Project
- Novel agent architecture or algorithm
- Empirical evaluation on benchmarks
- Written as a short paper (4-6 pages)

### Option B: Engineering Project
- Production-ready agent system
- Deployed and documented
- Technical report with demo

### Option C: Benchmark/Dataset
- New evaluation benchmark
- Dataset with documentation
- Leaderboard implementation

## Requirements

### Technical Requirements
- Python 3.11+ with type hints
- Comprehensive test coverage (>80%)
- Documentation (README, API docs)
- Reproducible setup (Docker or requirements.txt)

### Deliverables
| Deliverable | Due | Weight |
|-------------|-----|--------|
| Proposal | Week 8 | 10% |
| Progress Report | Week 10 | 10% |
| Final Presentation | Week 12 | 30% |
| Final Report | Week 12 | 50% |

## Evaluation Rubric (100 points)

### Presentation (30 points)
| Criterion | Points |
|-----------|--------|
| Clarity of problem statement | 8 |
| Technical depth | 10 |
| Results and evaluation | 7 |
| Q&A handling | 5 |

### Report (50 points)
| Criterion | Points |
|-----------|--------|
| Introduction and motivation | 10 |
| Technical approach | 15 |
| Experiments and results | 15 |
| Related work and positioning | 5 |
| Writing quality | 5 |

### Code and Reproducibility (20 points)
| Criterion | Points |
|-----------|--------|
| Code quality and organization | 8 |
| Documentation | 6 |
| Reproducibility | 6 |

## Timeline
- Week 7: Project topic selection
- Week 8: Proposal submission (1 page)
- Week 9-10: Implementation
- Week 10: Progress report (2 pages)
- Week 11: Final implementation
- Week 12: Presentation and final report

## Suggested Topics
1. Novel multi-agent coordination mechanism
2. Domain-specific agent for [finance/healthcare/education]
3. Improved hallucination detection system
4. GraphRAG extension for [domain]
5. Agent evaluation benchmark for [capability]
6. Tool-using agent for [API/domain]
7. Long-term memory system for agents
8. Safety and alignment mechanisms

## Resources
- GPU access: [Cloud credits provided]
- API credits: OpenAI/Anthropic [education tier]
- Office hours: Fridays 2-4 PM
"""
    return body

def update_issue(repo, number, body):
    """Update a single issue with new body"""
    # Write body to temp file to handle escaping
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(body)
        temp_path = f.name

    cmd = f'gh issue edit {number} --repo {repo} --body-file "{temp_path}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    import os
    os.unlink(temp_path)

    if result.returncode != 0:
        print(f"Error updating issue #{number}: {result.stderr}")
        return False
    return True

def main():
    repo = "Digital-AI-Finance/agentic-artificial-intelligence"

    # Get all issues
    result = subprocess.run(
        f'gh issue list --repo {repo} --limit 100 --json number,title',
        shell=True, capture_output=True, text=True
    )
    issues = json.loads(result.stdout)

    print(f"Found {len(issues)} issues to update")

    # Process each issue
    for issue in issues:
        number = issue['number']
        title = issue['title']
        week = get_week_from_title(title)

        if not week:
            print(f"Skipping issue #{number}: {title} (no week found)")
            continue

        # Determine issue type and generate body
        if '[SLIDES]' in title:
            body = generate_slides_body(title, week)
            issue_type = "SLIDES"
        elif '[NOTEBOOK]' in title:
            body = generate_notebook_body(title, week)
            issue_type = "NOTEBOOK"
        elif '[CHART]' in title:
            body = generate_chart_body(title, week)
            issue_type = "CHART"
        elif '[EXERCISE]' in title:
            body = generate_exercise_body(title, week)
            issue_type = "EXERCISE"
        elif '[READING]' in title:
            body = generate_reading_body(title, week)
            issue_type = "READING"
        elif '[PROJECT]' in title:
            body = generate_project_body()
            issue_type = "PROJECT"
        else:
            print(f"Skipping issue #{number}: {title} (unknown type)")
            continue

        print(f"Updating issue #{number} ({issue_type}): {title[:50]}...")

        if update_issue(repo, number, body):
            print(f"  -> Updated successfully")
        else:
            print(f"  -> FAILED")

if __name__ == "__main__":
    main()
