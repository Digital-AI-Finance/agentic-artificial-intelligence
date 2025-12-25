"""Script to create all course issues for Agentic AI course."""
import subprocess
import json

# Repository info
REPO = "Digital-AI-Finance/agentic-artificial-intelligence"

# Milestone titles by week number
MILESTONES = {
    1: "Week 1: Introduction to Agentic AI",
    2: "Week 2: LLM Foundations for Agents",
    3: "Week 3: Tool Use and Function Calling",
    4: "Week 4: Planning and Reasoning",
    5: "Week 5: Multi-Agent Architectures",
    6: "Week 6: Agent Frameworks Deep Dive",
    7: "Week 7: Advanced RAG Architectures",
    8: "Week 8: Knowledge Graphs and GraphRAG",
    9: "Week 9: Hallucination Prevention",
    10: "Week 10: Agent Evaluation",
    11: "Week 11: Domain Applications",
    12: "Week 12: Research Frontiers",
}

# Issue definitions by week
ISSUES = [
    # Week 1: Introduction to Agentic AI
    {"title": "[SLIDES] L01: Introduction to Agentic AI", "labels": ["type:slides", "priority:high", "week:01", "module:foundations"], "week": 1,
     "body": "## Learning Objectives\n- Define what makes an AI agent vs a simple LLM\n- Explain the perception-reasoning-action loop\n- Understand the ReAct paradigm\n\n## Content\n- Evolution from LLMs to agents\n- Agent definition and components\n- ReAct framework overview\n- Course roadmap"},
    {"title": "[CHART] L01/01_agent_definition: Agent vs LLM Comparison", "labels": ["type:chart", "priority:high", "week:01", "module:foundations"], "week": 1,
     "body": "## Description\nVisual comparison of traditional LLM (input->output) vs Agent (perception->reasoning->action->feedback loop)\n\n## Design\n- Two-panel diagram\n- Color-coded components\n- figsize=(10, 6)"},
    {"title": "[CHART] L01/02_react_paradigm: ReAct Cycle Visualization", "labels": ["type:chart", "priority:high", "week:01", "module:foundations"], "week": 1,
     "body": "## Description\nCircular diagram showing Reasoning-Acting-Observing cycle\n\n## Design\n- Circular flow diagram\n- Example annotations\n- figsize=(10, 6)"},
    {"title": "[NOTEBOOK] L01: First Agent Implementation", "labels": ["type:notebook", "priority:medium", "week:01", "module:foundations"], "week": 1,
     "body": "## Purpose\nHands-on introduction to building a simple agent\n\n## Sections\n1. Setting up API keys\n2. Basic agent loop\n3. Adding a simple tool\n4. Testing the agent"},
    {"title": "[EXERCISE] L01: Agent Classification Exercise", "labels": ["type:exercise", "priority:low", "week:01", "module:foundations"], "week": 1,
     "body": "## Exercise\nClassify 10 AI systems as agents or non-agents based on criteria learned\n\n## Format\n- Written analysis\n- 1 hour estimated time"},
    {"title": "[READING] L01: ReAct Paper (Yao et al., 2023)", "labels": ["type:reading", "priority:medium", "week:01", "module:foundations"], "week": 1,
     "body": "## Paper\n- Title: ReAct: Synergizing Reasoning and Acting in Language Models\n- Authors: Yao et al.\n- Year: 2023\n- arXiv: 2210.03629\n\n## Reading Guide\n1. What problem does ReAct solve?\n2. How does it combine reasoning and acting?\n3. What benchmarks were used?"},

    # Week 2: LLM Foundations for Agents
    {"title": "[SLIDES] L02: LLM Foundations for Agents", "labels": ["type:slides", "priority:high", "week:02", "module:foundations"], "week": 2,
     "body": "## Learning Objectives\n- Review transformer architecture for agent context\n- Master Chain-of-Thought prompting\n- Understand context window limitations\n\n## Content\n- Attention mechanisms recap\n- Prompting strategies\n- CoT vs ToT\n- Context management"},
    {"title": "[CHART] L02/01_cot_vs_tot: Chain-of-Thought vs Tree-of-Thought", "labels": ["type:chart", "priority:high", "week:02", "module:foundations"], "week": 2,
     "body": "## Description\nSide-by-side comparison of linear CoT vs branching ToT reasoning\n\n## Design\n- Two-panel diagram\n- Tree structure for ToT\n- Linear chain for CoT"},
    {"title": "[CHART] L02/02_context_window: Context Window Impact", "labels": ["type:chart", "priority:medium", "week:02", "module:foundations"], "week": 2,
     "body": "## Description\nVisualization of how context window size affects agent capabilities\n\n## Design\n- Bar chart or timeline\n- Model comparisons (GPT-4, Claude, etc.)"},
    {"title": "[NOTEBOOK] L02: Prompting Strategies Lab", "labels": ["type:notebook", "priority:medium", "week:02", "module:foundations"], "week": 2,
     "body": "## Purpose\nHands-on practice with different prompting techniques\n\n## Sections\n1. Zero-shot prompting\n2. Few-shot prompting\n3. Chain-of-Thought\n4. Tree-of-Thought implementation"},
    {"title": "[EXERCISE] L02: Prompt Engineering Challenge", "labels": ["type:exercise", "priority:low", "week:02", "module:foundations"], "week": 2,
     "body": "## Exercise\nOptimize prompts for a given task using different strategies\n\n## Format\n- Coding exercise\n- 2 hours estimated"},
    {"title": "[READING] L02: Chain-of-Thought Paper (Wei et al., 2022)", "labels": ["type:reading", "priority:medium", "week:02", "module:foundations"], "week": 2,
     "body": "## Paper\n- Title: Chain-of-Thought Prompting Elicits Reasoning\n- Authors: Wei et al.\n- Year: 2022\n\n## Reading Guide\n1. What is the key insight?\n2. What tasks benefit most?\n3. How does model size affect CoT?"},

    # Week 3: Tool Use and Function Calling
    {"title": "[SLIDES] L03: Tool Use and Function Calling", "labels": ["type:slides", "priority:high", "week:03", "module:single-agent"], "week": 3,
     "body": "## Learning Objectives\n- Understand MCP architecture\n- Design robust function schemas\n- Implement error handling\n\n## Content\n- Model Context Protocol (MCP)\n- Function calling patterns\n- Tool schema design\n- Error handling strategies"},
    {"title": "[CHART] L03/01_mcp_architecture: MCP Architecture Diagram", "labels": ["type:chart", "priority:high", "week:03", "module:single-agent"], "week": 3,
     "body": "## Description\nComprehensive diagram of MCP components and data flow\n\n## Design\n- Architecture diagram\n- Show client, server, tools relationship"},
    {"title": "[CHART] L03/02_tool_calling_sequence: Tool Calling Sequence", "labels": ["type:chart", "priority:medium", "week:03", "module:single-agent"], "week": 3,
     "body": "## Description\nSequence diagram showing tool invocation flow\n\n## Design\n- UML-style sequence diagram\n- Request/response flows"},
    {"title": "[NOTEBOOK] L03: MCP Tool Implementation", "labels": ["type:notebook", "priority:high", "week:03", "module:single-agent"], "week": 3,
     "body": "## Purpose\nBuild a complete MCP tool from scratch\n\n## Sections\n1. MCP server setup\n2. Tool schema definition\n3. Tool implementation\n4. Client integration"},
    {"title": "[NOTEBOOK] L03: Function Calling Comparison", "labels": ["type:notebook", "priority:medium", "week:03", "module:single-agent"], "week": 3,
     "body": "## Purpose\nCompare function calling across providers\n\n## Sections\n1. OpenAI function calling\n2. Anthropic tool use\n3. Google Gemini tools\n4. Best practices"},
    {"title": "[EXERCISE] L03: Build a Multi-Tool Agent", "labels": ["type:exercise", "priority:medium", "week:03", "module:single-agent"], "week": 3,
     "body": "## Exercise\nCreate an agent with 3+ tools working together\n\n## Requirements\n- Calculator tool\n- Web search tool\n- File operations tool\n- Proper error handling"},
    {"title": "[READING] L03: MCP Specification Review", "labels": ["type:reading", "priority:low", "week:03", "module:single-agent"], "week": 3,
     "body": "## Resource\n- Anthropic MCP Documentation\n- Protocol specification\n\n## Reading Guide\n1. Core protocol concepts\n2. Transport mechanisms\n3. Security considerations"},

    # Week 4: Planning and Reasoning
    {"title": "[SLIDES] L04: Planning and Reasoning", "labels": ["type:slides", "priority:high", "week:04", "module:single-agent"], "week": 4,
     "body": "## Learning Objectives\n- Implement task decomposition\n- Build memory-augmented agents\n- Apply self-reflection patterns\n\n## Content\n- Planning strategies\n- Hierarchical decomposition\n- Memory systems\n- Reflexion pattern"},
    {"title": "[CHART] L04/01_hierarchical_planning: Hierarchical Planning Diagram", "labels": ["type:chart", "priority:high", "week:04", "module:single-agent"], "week": 4,
     "body": "## Description\nTree structure showing task decomposition levels\n\n## Design\n- Hierarchical tree diagram\n- Color-coded depth levels"},
    {"title": "[CHART] L04/02_memory_types: Memory Types Comparison", "labels": ["type:chart", "priority:medium", "week:04", "module:single-agent"], "week": 4,
     "body": "## Description\nComparison of short-term, long-term, and episodic memory\n\n## Design\n- Three-column comparison\n- Use cases for each"},
    {"title": "[NOTEBOOK] L04: Reflexion Implementation", "labels": ["type:notebook", "priority:high", "week:04", "module:single-agent"], "week": 4,
     "body": "## Purpose\nImplement the Reflexion self-improvement pattern\n\n## Sections\n1. Basic agent setup\n2. Reflection mechanism\n3. Memory integration\n4. Iterative improvement"},
    {"title": "[EXERCISE] L04: Build a Planning Agent", "labels": ["type:exercise", "priority:medium", "week:04", "module:single-agent"], "week": 4,
     "body": "## Exercise\nCreate an agent that plans and executes multi-step tasks\n\n## Requirements\n- Task decomposition\n- Progress tracking\n- Plan revision capability"},
    {"title": "[READING] L04: Reflexion Paper (Shinn et al., 2023)", "labels": ["type:reading", "priority:medium", "week:04", "module:single-agent"], "week": 4,
     "body": "## Paper\n- Title: Reflexion: Language Agents with Verbal Reinforcement Learning\n- Authors: Shinn et al.\n- Year: 2023\n\n## Reading Guide\n1. How does verbal reinforcement work?\n2. What is the role of episodic memory?\n3. Performance on benchmarks?"},

    # Week 5: Multi-Agent Architectures
    {"title": "[SLIDES] L05: Multi-Agent Architectures", "labels": ["type:slides", "priority:high", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Learning Objectives\n- Design agent communication protocols\n- Implement role assignment\n- Coordinate multi-agent activities\n\n## Content\n- Multi-agent patterns\n- Communication topologies\n- Role specialization\n- Coordination mechanisms"},
    {"title": "[CHART] L05/01_communication_topology: Communication Topology Diagram", "labels": ["type:chart", "priority:high", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Description\nDifferent communication patterns (star, mesh, hierarchical)\n\n## Design\n- Multiple topology examples\n- Pros/cons annotations"},
    {"title": "[CHART] L05/02_role_specialization: Agent Role Matrix", "labels": ["type:chart", "priority:medium", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Description\nMatrix showing agent roles and capabilities\n\n## Design\n- Table/matrix format\n- Role-capability mapping"},
    {"title": "[NOTEBOOK] L05: Multi-Agent Message Passing", "labels": ["type:notebook", "priority:high", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Purpose\nImplement agent-to-agent communication\n\n## Sections\n1. Message protocol design\n2. Sender/receiver implementation\n3. Message routing\n4. Coordination patterns"},
    {"title": "[NOTEBOOK] L05: Agent Coordination Demo", "labels": ["type:notebook", "priority:medium", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Purpose\nDemonstrate coordinated multi-agent problem solving\n\n## Sections\n1. Task distribution\n2. Result aggregation\n3. Conflict resolution"},
    {"title": "[EXERCISE] L05: Design a Multi-Agent System", "labels": ["type:exercise", "priority:medium", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Exercise\nDesign architecture for a research assistant team\n\n## Deliverables\n- System architecture diagram\n- Role definitions\n- Communication protocol\n- Coordination strategy"},
    {"title": "[READING] L05: MAS Survey (Tran et al., 2025)", "labels": ["type:reading", "priority:medium", "week:05", "module:multi-agent"], "week": 5,
     "body": "## Paper\n- Title: Multi-Agent Collaboration Mechanisms: A Survey of LLMs\n- Authors: Tran et al.\n- Year: 2025\n\n## Reading Guide\n1. Taxonomy of collaboration patterns\n2. Emergent behaviors\n3. Open challenges"},

    # Week 6: Agent Frameworks Deep Dive
    {"title": "[SLIDES] L06: Agent Frameworks Deep Dive", "labels": ["type:slides", "priority:high", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Learning Objectives\n- Implement agents in LangGraph\n- Compare framework trade-offs\n- Select appropriate frameworks\n\n## Content\n- LangGraph overview\n- AutoGen patterns\n- CrewAI teams\n- Framework selection criteria"},
    {"title": "[CHART] L06/01_langgraph_state_machine: LangGraph State Machine", "labels": ["type:chart", "priority:high", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Description\nState machine visualization for LangGraph agents\n\n## Design\n- State diagram\n- Transitions and conditions"},
    {"title": "[CHART] L06/02_framework_decision_tree: Framework Decision Tree", "labels": ["type:chart", "priority:medium", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Description\nDecision tree for choosing the right framework\n\n## Design\n- Binary decision tree\n- Use case annotations"},
    {"title": "[NOTEBOOK] L06: LangGraph Implementation", "labels": ["type:notebook", "priority:high", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Purpose\nBuild a complete agent using LangGraph\n\n## Sections\n1. State definition\n2. Node implementation\n3. Edge conditions\n4. Execution flow"},
    {"title": "[NOTEBOOK] L06: CrewAI Team Agent", "labels": ["type:notebook", "priority:medium", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Purpose\nCreate a multi-agent team with CrewAI\n\n## Sections\n1. Agent definitions\n2. Task assignments\n3. Crew orchestration\n4. Results handling"},
    {"title": "[NOTEBOOK] L06: AutoGen Conversation", "labels": ["type:notebook", "priority:medium", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Purpose\nImplement conversation-based agents with AutoGen\n\n## Sections\n1. Agent configuration\n2. Conversation flow\n3. Code execution\n4. Human-in-the-loop"},
    {"title": "[EXERCISE] L06: Framework Selection Challenge", "labels": ["type:exercise", "priority:medium", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Exercise\nEvaluate and select framework for given scenarios\n\n## Scenarios\n- Customer service bot\n- Research assistant\n- Code review system"},
    {"title": "[READING] L06: LangGraph Documentation Review", "labels": ["type:reading", "priority:low", "week:06", "module:multi-agent"], "week": 6,
     "body": "## Resource\n- LangGraph official documentation\n- State management concepts\n\n## Focus Areas\n1. Graph construction\n2. Persistence\n3. Streaming"},

    # Week 7: Advanced RAG Architectures
    {"title": "[SLIDES] L07: Advanced RAG Architectures", "labels": ["type:slides", "priority:high", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Learning Objectives\n- Implement Self-RAG patterns\n- Handle long documents\n- Combine retrieval methods\n\n## Content\n- Self-RAG architecture\n- LongRAG strategies\n- Hybrid retrieval\n- Query enhancement"},
    {"title": "[CHART] L07/01_self_rag_architecture: Self-RAG Architecture", "labels": ["type:chart", "priority:high", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Description\nSelf-RAG pipeline with retrieval, critique, and generation\n\n## Design\n- Flow diagram\n- Feedback loops"},
    {"title": "[CHART] L07/02_hybrid_retrieval: Hybrid Retrieval Comparison", "labels": ["type:chart", "priority:medium", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Description\nCompare dense vs sparse vs hybrid retrieval\n\n## Design\n- Venn diagram or comparison matrix"},
    {"title": "[NOTEBOOK] L07: Self-RAG Implementation", "labels": ["type:notebook", "priority:high", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Purpose\nBuild a Self-RAG system from scratch\n\n## Sections\n1. Retriever setup\n2. Critique generation\n3. Adaptive retrieval\n4. Quality filtering"},
    {"title": "[NOTEBOOK] L07: LongRAG for Documents", "labels": ["type:notebook", "priority:medium", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Purpose\nHandle long document retrieval and processing\n\n## Sections\n1. Document chunking strategies\n2. Hierarchical indexing\n3. Context compression\n4. Multi-hop retrieval"},
    {"title": "[EXERCISE] L07: Build Adaptive RAG System", "labels": ["type:exercise", "priority:medium", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Exercise\nCreate a RAG system that adapts to query complexity\n\n## Requirements\n- Query classification\n- Adaptive retrieval depth\n- Quality metrics"},
    {"title": "[READING] L07: RAG Survey (Gao et al., 2024)", "labels": ["type:reading", "priority:medium", "week:07", "module:rag-knowledge"], "week": 7,
     "body": "## Paper\n- Title: Retrieval-Augmented Generation: A Comprehensive Survey\n- Authors: Gao et al.\n- Year: 2024\n\n## Reading Guide\n1. RAG taxonomy\n2. Evaluation methods\n3. Future directions"},

    # Week 8: Knowledge Graphs and GraphRAG
    {"title": "[SLIDES] L08: Knowledge Graphs and GraphRAG", "labels": ["type:slides", "priority:high", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Learning Objectives\n- Construct knowledge graphs from text\n- Implement GraphRAG\n- Perform multi-hop reasoning\n\n## Content\n- KG fundamentals\n- GraphRAG pipeline\n- Multi-hop queries\n- Multimodal integration"},
    {"title": "[CHART] L08/01_graphrag_pipeline: GraphRAG Pipeline", "labels": ["type:chart", "priority:high", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Description\nEnd-to-end GraphRAG architecture\n\n## Design\n- Pipeline diagram\n- KG + retrieval integration"},
    {"title": "[CHART] L08/02_multihop_reasoning: Multi-hop Reasoning Visualization", "labels": ["type:chart", "priority:medium", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Description\nShow path traversal in knowledge graph\n\n## Design\n- Graph with highlighted paths\n- Query decomposition"},
    {"title": "[NOTEBOOK] L08: KG Construction from Text", "labels": ["type:notebook", "priority:high", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Purpose\nBuild knowledge graphs from unstructured text\n\n## Sections\n1. Entity extraction\n2. Relation extraction\n3. Graph construction\n4. Quality validation"},
    {"title": "[NOTEBOOK] L08: GraphRAG Implementation", "labels": ["type:notebook", "priority:high", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Purpose\nImplement Microsoft's GraphRAG approach\n\n## Sections\n1. Graph indexing\n2. Community detection\n3. Query routing\n4. Answer synthesis"},
    {"title": "[EXERCISE] L08: Build Domain Knowledge Graph", "labels": ["type:exercise", "priority:medium", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Exercise\nConstruct a KG for a specialized domain\n\n## Deliverables\n- Entity types\n- Relation schema\n- Populated graph\n- Query interface"},
    {"title": "[READING] L08: GraphRAG Paper (Microsoft, 2024)", "labels": ["type:reading", "priority:medium", "week:08", "module:rag-knowledge"], "week": 8,
     "body": "## Paper\n- Title: From Local to Global: A Graph RAG Approach to Query-Focused Summarization\n- Source: Microsoft Research\n- Year: 2024\n\n## Reading Guide\n1. Local vs global queries\n2. Community summaries\n3. Scalability considerations"},

    # Week 9: Hallucination Prevention
    {"title": "[SLIDES] L09: Hallucination Prevention", "labels": ["type:slides", "priority:high", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Learning Objectives\n- Identify hallucination sources\n- Implement verification patterns\n- Build grounded agents\n\n## Content\n- Hallucination taxonomy\n- Verification tools\n- Grounding strategies\n- Testing frameworks"},
    {"title": "[CHART] L09/01_verification_pipeline: Verification Pipeline Diagram", "labels": ["type:chart", "priority:high", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Description\nEnd-to-end verification pipeline for agent outputs\n\n## Design\n- Pipeline stages\n- Verification checkpoints"},
    {"title": "[CHART] L09/02_grounding_techniques: Grounding Techniques Comparison", "labels": ["type:chart", "priority:medium", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Description\nCompare different grounding approaches\n\n## Design\n- Comparison matrix\n- Effectiveness ratings"},
    {"title": "[NOTEBOOK] L09: Hallucination Detection Demo", "labels": ["type:notebook", "priority:high", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Purpose\nDemonstrate hallucination detection techniques\n\n## Sections\n1. Pattern identification\n2. Factual verification\n3. Consistency checks\n4. Source attribution"},
    {"title": "[NOTEBOOK] L09: Verification Tool Integration", "labels": ["type:notebook", "priority:high", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Purpose\nIntegrate hallucination-prevention-toolkit\n\n## Sections\n1. Tool setup\n2. API verification\n3. Citation checking\n4. Automated testing"},
    {"title": "[EXERCISE] L09: Build Fact-Checking Agent", "labels": ["type:exercise", "priority:medium", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Exercise\nCreate an agent that verifies its own outputs\n\n## Requirements\n- Source citation\n- Confidence scoring\n- Uncertainty flagging"},
    {"title": "[READING] L09: Hallucination Survey", "labels": ["type:reading", "priority:medium", "week:09", "module:safety-eval"], "week": 9,
     "body": "## Paper\n- Title: Survey of Hallucination in Natural Language Generation\n- Focus on LLM-specific patterns\n\n## Reading Guide\n1. Types of hallucinations\n2. Detection methods\n3. Mitigation strategies"},

    # Week 10: Agent Evaluation
    {"title": "[SLIDES] L10: Agent Evaluation", "labels": ["type:slides", "priority:high", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Learning Objectives\n- Define agent metrics\n- Design benchmarks\n- Conduct safety testing\n\n## Content\n- Evaluation frameworks\n- AgentBench overview\n- Red-teaming methods\n- Human evaluation"},
    {"title": "[CHART] L10/01_metric_taxonomy: Metric Taxonomy Diagram", "labels": ["type:chart", "priority:high", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Description\nHierarchy of agent evaluation metrics\n\n## Design\n- Tree structure\n- Category groupings"},
    {"title": "[CHART] L10/02_benchmark_comparison: Benchmark Comparison Matrix", "labels": ["type:chart", "priority:medium", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Description\nCompare major agent benchmarks\n\n## Design\n- Matrix format\n- Feature comparison"},
    {"title": "[NOTEBOOK] L10: Agent Benchmarking Suite", "labels": ["type:notebook", "priority:high", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Purpose\nRun agents through benchmark evaluations\n\n## Sections\n1. Benchmark setup\n2. Agent evaluation\n3. Metric calculation\n4. Result analysis"},
    {"title": "[NOTEBOOK] L10: Red-Teaming Demonstration", "labels": ["type:notebook", "priority:medium", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Purpose\nDemonstrate adversarial testing of agents\n\n## Sections\n1. Attack vectors\n2. Jailbreak attempts\n3. Prompt injection\n4. Defense strategies"},
    {"title": "[EXERCISE] L10: Design Evaluation Criteria", "labels": ["type:exercise", "priority:medium", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Exercise\nDesign custom evaluation framework for a domain agent\n\n## Deliverables\n- Metrics definition\n- Test cases\n- Scoring rubric"},
    {"title": "[READING] L10: AgentBench Paper (Liu et al., 2023)", "labels": ["type:reading", "priority:medium", "week:10", "module:safety-eval"], "week": 10,
     "body": "## Paper\n- Title: AgentBench: Evaluating LLMs as Agents\n- Authors: Liu et al.\n- Year: 2023\n\n## Reading Guide\n1. Benchmark design\n2. Task categories\n3. Model rankings"},

    # Week 11: Domain Applications
    {"title": "[SLIDES] L11: Domain Applications - Software Engineering", "labels": ["type:slides", "priority:high", "week:11", "module:applications"], "week": 11,
     "body": "## Learning Objectives\n- Understand coding agents\n- Analyze Devin/Copilot architectures\n- Apply agents to development\n\n## Content\n- Coding agent patterns\n- Devin architecture\n- Copilot integration\n- Code review agents"},
    {"title": "[SLIDES] L11: Domain Applications - Finance & Healthcare", "labels": ["type:slides", "priority:high", "week:11", "module:applications"], "week": 11,
     "body": "## Learning Objectives\n- Apply agents to finance\n- Understand healthcare constraints\n- Design domain-specific agents\n\n## Content\n- Trading agents\n- Research analysts\n- MDAgents overview\n- Regulatory considerations"},
    {"title": "[CHART] L11/01_domain_agent_comparison: Domain Agent Comparison", "labels": ["type:chart", "priority:medium", "week:11", "module:applications"], "week": 11,
     "body": "## Description\nCompare agents across domains\n\n## Design\n- Comparison matrix\n- Capability mapping"},
    {"title": "[NOTEBOOK] L11: Code Generation Agent", "labels": ["type:notebook", "priority:high", "week:11", "module:applications"], "week": 11,
     "body": "## Purpose\nBuild a code generation and review agent\n\n## Sections\n1. Code understanding\n2. Generation pipeline\n3. Testing integration\n4. Review feedback"},
    {"title": "[NOTEBOOK] L11: Financial Analysis Agent", "labels": ["type:notebook", "priority:medium", "week:11", "module:applications"], "week": 11,
     "body": "## Purpose\nCreate an agent for financial analysis\n\n## Sections\n1. Data retrieval\n2. Analysis pipeline\n3. Report generation\n4. Risk considerations"},
    {"title": "[EXERCISE] L11: Build Domain-Specific Agent", "labels": ["type:exercise", "priority:high", "week:11", "module:applications"], "week": 11,
     "body": "## Exercise\nDesign and implement an agent for a chosen domain\n\n## Requirements\n- Domain analysis\n- Tool selection\n- Safety measures\n- Evaluation plan"},
    {"title": "[READING] L11: Devin/Copilot Analysis", "labels": ["type:reading", "priority:medium", "week:11", "module:applications"], "week": 11,
     "body": "## Resource\n- Devin technical blog\n- Copilot research papers\n\n## Reading Guide\n1. Architecture patterns\n2. Training approaches\n3. Limitations"},

    # Week 12: Research Frontiers
    {"title": "[SLIDES] L12: Research Frontiers", "labels": ["type:slides", "priority:high", "week:12", "module:applications"], "week": 12,
     "body": "## Learning Objectives\n- Explore emerging research\n- Understand future directions\n- Synthesize course knowledge\n\n## Content\n- Agent co-evolution\n- Swarm intelligence\n- AGI perspectives\n- Research opportunities"},
    {"title": "[CHART] L12/01_future_directions: Future Directions Roadmap", "labels": ["type:chart", "priority:medium", "week:12", "module:applications"], "week": 12,
     "body": "## Description\nRoadmap of agentic AI research directions\n\n## Design\n- Timeline/roadmap format\n- Key milestones"},
    {"title": "[NOTEBOOK] L12: Agent Co-Evolution Demo", "labels": ["type:notebook", "priority:medium", "week:12", "module:applications"], "week": 12,
     "body": "## Purpose\nDemonstrate agent self-improvement over time\n\n## Sections\n1. Baseline agent\n2. Evolution mechanism\n3. Performance tracking\n4. Analysis"},
    {"title": "[EXERCISE] L12: Research Proposal", "labels": ["type:exercise", "priority:high", "week:12", "module:applications"], "week": 12,
     "body": "## Exercise\nWrite a research proposal for advancing agentic AI\n\n## Requirements\n- Problem statement\n- Proposed approach\n- Expected contributions\n- Evaluation plan"},
    {"title": "[PROJECT] L12: Final Project Presentations", "labels": ["type:project", "priority:critical", "week:12", "module:applications"], "week": 12,
     "body": "## Final Project\nPresent course project implementing an agentic AI system\n\n## Requirements\n- Working demo\n- Technical report\n- Presentation\n- Code repository"},
    {"title": "[READING] L12: Frontier Papers Collection", "labels": ["type:reading", "priority:low", "week:12", "module:applications"], "week": 12,
     "body": "## Curated Papers\n- Agent emergence and scaling\n- Multi-agent cooperation\n- AGI alignment considerations\n\n## Purpose\nExposure to cutting-edge research for project inspiration"},
]

def create_issue(issue):
    """Create a single issue using gh CLI."""
    labels = ",".join(issue["labels"])
    milestone = MILESTONES[issue["week"]]

    cmd = [
        "gh", "issue", "create",
        "--repo", REPO,
        "--title", issue["title"],
        "--body", issue["body"],
        "--label", labels,
        "--milestone", milestone
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Created: {issue['title']}")
        return result.stdout.strip()
    else:
        print(f"Failed: {issue['title']} - {result.stderr}")
        return None

def main():
    """Create all issues."""
    print(f"Creating {len(ISSUES)} issues...")

    created = 0
    failed = 0

    for issue in ISSUES:
        url = create_issue(issue)
        if url:
            created += 1
        else:
            failed += 1

    print(f"\nDone! Created: {created}, Failed: {failed}")

if __name__ == "__main__":
    main()
