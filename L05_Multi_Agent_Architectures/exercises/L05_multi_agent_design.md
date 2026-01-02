# Exercise L05: Design and Implement a Multi-Agent System

**Week 5 - Multi-Agent Architectures**

## Overview

Design and implement a multi-agent system for a complex collaborative task, demonstrating understanding of agent coordination, message passing, and emergent system behaviors.

## Learning Objectives

- **Primary (Create)**: Build a functional multi-agent system with specialized roles
- **Secondary (Analyze)**: Compare coordination patterns (centralized vs decentralized)
- **Tertiary (Evaluate)**: Assess trade-offs between system complexity and capability

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- Understanding of basic agent patterns (ReAct, tool use)
- NetworkX (for agent topology visualization)

## Problem Statement

Single agents hit capability limits on complex tasks:
- Knowledge span: No single prompt can cover all domains
- Reasoning depth: Complex decisions benefit from debate
- Reliability: Multiple perspectives catch errors
- Scalability: Parallel processing requires coordination

Multi-agent systems address these by dividing labor among specialized agents. This exercise develops skills in designing effective agent teams.

### Task 1: System Design (35 points)

Design a multi-agent system for ONE of these scenarios:

**Option A: Research Assistant Team**
| Agent | Role | Tools |
|-------|------|-------|
| Literature Searcher | Finds relevant papers | search_arxiv, search_scholar |
| Summarizer | Creates paper summaries | read_pdf, generate_summary |
| Synthesizer | Combines findings | create_outline, write_section |
| Critic | Identifies gaps and limitations | check_citations, verify_claims |

**Option B: Code Review Pipeline**
| Agent | Role | Tools |
|-------|------|-------|
| Analyzer | Identifies code patterns | parse_code, find_patterns |
| Security Auditor | Checks vulnerabilities | run_sast, check_dependencies |
| Performance Reviewer | Finds bottlenecks | profile_code, suggest_optimization |
| Documentation Checker | Verifies docs | check_docstrings, validate_readme |

**Option C: Investment Analysis Team**
| Agent | Role | Tools |
|-------|------|-------|
| Data Gatherer | Collects financial data | fetch_prices, get_filings |
| Quantitative Analyst | Runs calculations | calculate_ratios, backtest |
| Qualitative Analyst | Assesses non-financial factors | analyze_news, check_management |
| Risk Assessor | Evaluates risks | calculate_var, stress_test |

**Design Deliverables:**

1. **Architecture Diagram** showing:
   - Agent topology (star, mesh, hierarchical, pipeline)
   - Communication channels between agents
   - Shared state or message bus

2. **Role Descriptions** for each agent:
   ```
   Agent: Literature Searcher
   Goal: Find all relevant papers for a research topic
   Capabilities: Search academic databases, filter by relevance
   Input: Research question or topic
   Output: List of relevant papers with metadata
   Coordination: Sends papers to Summarizer, receives feedback from Critic
   ```

3. **Message Format Specification**:
   ```python
   @dataclass
   class AgentMessage:
       sender: str           # Agent name
       recipient: str        # Target agent or "broadcast"
       message_type: str     # "request", "response", "feedback"
       content: dict         # Payload
       timestamp: datetime
       correlation_id: str   # For tracking conversations
   ```

4. **Workflow Sequence Diagram** showing message flow for a sample task

### Task 2: Implementation (40 points)

Implement your designed system with the following structure:

**2a: Base Agent Class (10 points)**
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import uuid

@dataclass
class AgentMessage:
    sender: str
    recipient: str
    message_type: str
    content: dict
    timestamp: datetime
    correlation_id: str = None

    def __post_init__(self):
        if self.correlation_id is None:
            self.correlation_id = str(uuid.uuid4())

class BaseAgent(ABC):
    def __init__(self, name: str, role: str, llm_client):
        self.name = name
        self.role = role
        self.llm = llm_client
        self.inbox: list[AgentMessage] = []
        self.outbox: list[AgentMessage] = []
        self.memory: list[dict] = []

    @abstractmethod
    def process_message(self, message: AgentMessage) -> list[AgentMessage]:
        """Process an incoming message and return response messages."""
        pass

    @abstractmethod
    def get_system_prompt(self) -> str:
        """Return the system prompt for this agent's role."""
        pass

    def receive(self, message: AgentMessage):
        """Add message to inbox."""
        self.inbox.append(message)

    def send(self, message: AgentMessage):
        """Add message to outbox."""
        self.outbox.append(message)
```

**2b: Specialized Agents (15 points)**
Implement at least 3 specialized agent classes:

```python
class LiteratureSearcher(BaseAgent):
    def get_system_prompt(self) -> str:
        return """You are a Literature Searcher agent. Your role is to find
        relevant academic papers for research topics.

        When given a research question:
        1. Identify key search terms
        2. Search academic databases
        3. Filter results by relevance and recency
        4. Return structured list of papers with titles, authors, abstracts

        Output format:
        {"papers": [{"title": "...", "authors": [...], "abstract": "...", "url": "..."}]}
        """

    def process_message(self, message: AgentMessage) -> list[AgentMessage]:
        # Implement literature search logic
        pass

class Summarizer(BaseAgent):
    # Implement summarization agent
    pass

class Critic(BaseAgent):
    # Implement critic agent
    pass
```

**2c: Coordinator/Router (15 points)**
```python
class MultiAgentSystem:
    def __init__(self):
        self.agents: dict[str, BaseAgent] = {}
        self.message_queue: list[AgentMessage] = []
        self.artifacts: list[dict] = []
        self.max_iterations: int = 10

    def add_agent(self, agent: BaseAgent):
        """Register an agent with the system."""
        self.agents[agent.name] = agent

    def route_message(self, message: AgentMessage):
        """Route a message to its recipient(s)."""
        if message.recipient == "broadcast":
            for agent in self.agents.values():
                if agent.name != message.sender:
                    agent.receive(message)
        elif message.recipient in self.agents:
            self.agents[message.recipient].receive(message)
        else:
            raise ValueError(f"Unknown recipient: {message.recipient}")

    def run_task(self, task: str, initiator: str = None) -> dict:
        """Execute a collaborative task."""
        # Create initial message
        initial_message = AgentMessage(
            sender="user",
            recipient=initiator or list(self.agents.keys())[0],
            message_type="request",
            content={"task": task},
            timestamp=datetime.now()
        )
        self.route_message(initial_message)

        # Run coordination loop
        for iteration in range(self.max_iterations):
            # Process all agent inboxes
            for agent in self.agents.values():
                while agent.inbox:
                    msg = agent.inbox.pop(0)
                    responses = agent.process_message(msg)
                    for response in responses:
                        self.route_message(response)

            # Check for completion
            if self._is_complete():
                break

        return self.get_results()

    def _is_complete(self) -> bool:
        """Check if task is complete (all inboxes empty, final artifact exists)."""
        pass

    def get_results(self) -> dict:
        """Return all generated artifacts."""
        return {"artifacts": self.artifacts, "message_count": len(self.message_queue)}
```

**Implementation Requirements:**
| Requirement | Description |
|-------------|-------------|
| Minimum 3 agents | Each with distinct role and system prompt |
| Message passing | Agents communicate only via messages |
| State tracking | Track workflow state and artifacts |
| Error handling | Handle at least one failure case |
| Termination | Clear completion criteria |

### Task 3: Analysis (25 points)

Write a comparative analysis (400-500 words) covering:

**3a: Coordination Patterns (10 points)**

| Pattern | Centralized | Decentralized |
|---------|-------------|---------------|
| Definition | Single coordinator routes all messages | Agents communicate directly |
| Advantages | Easy to debug, clear control flow | Scalable, no single point of failure |
| Disadvantages | Bottleneck, coordinator complexity | Hard to debug, message explosion |
| Best for | Small teams, clear workflows | Large teams, parallel tasks |

Analyze:
- Which pattern did you choose and why?
- How would behavior change with the other pattern?

**3b: Synchronous vs Asynchronous (10 points)**

| Aspect | Synchronous | Asynchronous |
|--------|-------------|--------------|
| Message handling | Wait for response before continuing | Send and continue |
| State management | Simpler, sequential | Complex, need to track pending |
| Parallelism | Limited | High |
| Implementation | Easier | Harder |

Analyze:
- Which approach did you use?
- What are the trade-offs for your specific task?

**3c: Design Decisions (5 points)**
- Why did you choose your agent topology?
- What would you change for 10x scale?
- What failure modes did you encounter?

## Test Scenarios Required

Include at least 10 test scenarios:

| Scenario | Type | Expected Behavior |
|----------|------|-------------------|
| Happy path | Normal | All agents complete their roles |
| Missing agent | Error | System handles gracefully |
| Circular messages | Edge | Detected and broken |
| Agent disagreement | Conflict | Resolution mechanism works |
| Timeout | Error | System doesn't hang |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| design_doc.md | Markdown | Architecture + role descriptions |
| agents.py | Python | Base class + 3+ specialized agents |
| coordinator.py | Python | MultiAgentSystem implementation |
| test_scenarios.py | Python | 10+ test cases |
| analysis.md | Markdown | 400-500 word comparative analysis |
| demo.ipynb | Jupyter | Interactive demonstration |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| System Design | 35 | Clear architecture, well-defined roles |
| Implementation | 40 | Working code, proper message passing |
| Analysis | 25 | Thoughtful comparison, justified choices |

### Detailed Rubric

**System Design (35 points)**
- 10 points: Architecture diagram is clear and complete
- 10 points: Role descriptions are well-defined
- 10 points: Message format is properly specified
- 5 points: Workflow sequence makes sense

**Implementation (40 points)**
- 10 points: Base agent class is well-designed
- 15 points: Specialized agents work correctly
- 10 points: Coordinator routes messages properly
- 5 points: Error handling is present

**Analysis (25 points)**
- 10 points: Coordination pattern analysis is insightful
- 10 points: Sync/async trade-offs are correctly identified
- 5 points: Design decisions are justified

## Resources

- Wu et al. (2023). "AutoGen: Enabling Next-Gen LLM Applications" - arXiv:2308.08155
- Hong et al. (2023). "MetaGPT" - arXiv:2308.00352
- Li et al. (2023). "CAMEL" - arXiv:2303.17760
- Park et al. (2023). "Generative Agents" - arXiv:2304.03442

## Submission

- **Format**: Design document + Python files + Jupyter notebook
- **Filename**: `L05_exercise_[your_name]/`
- **Due**: End of Week 5

## Hints

- Start with 2 agents before adding more
- Use print statements liberally for debugging message flow
- Implement termination conditions early to avoid infinite loops
- Test agent pairs before full system
- Consider using a message bus pattern for cleaner routing

## Sample Visualization

```python
import networkx as nx
import matplotlib.pyplot as plt

def visualize_agent_topology(agents: dict, edges: list[tuple]):
    """Visualize the agent communication topology."""
    G = nx.DiGraph()

    for name, agent in agents.items():
        G.add_node(name, role=agent.role)

    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    colors = ['lightblue' if G.nodes[n]['role'] != 'coordinator' else 'lightcoral'
              for n in G.nodes()]

    nx.draw(G, pos, node_color=colors, with_labels=True,
            font_size=10, node_size=2000, arrows=True)
    plt.title("Agent Communication Topology")
    plt.savefig("topology.png")
```

## Bonus Challenge (+15 points)

Implement ONE of:
- **Dynamic agent spawning**: Create new agents based on task complexity
- **Conflict resolution**: Protocol when agents disagree (voting, arbitration)
- **Performance monitoring**: Track message counts, latency, bottlenecks
- **Agent learning**: Agents improve based on feedback from other agents

## Time Estimate
- Minimum: 5 hours
- Expected: 8 hours
- Maximum: 12 hours
