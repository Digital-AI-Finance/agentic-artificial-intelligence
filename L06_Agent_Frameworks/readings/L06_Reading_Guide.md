# Reading Guide: Agent Frameworks - LangGraph, AutoGen, and Beyond

**Week 6 - Agent Frameworks**

## Primary Reading

### AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

- **Title**: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
- **Authors**: Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, et al.
- **Year**: 2023
- **Venue**: arXiv preprint
- **arXiv**: https://arxiv.org/abs/2308.08155
- **Code**: https://github.com/microsoft/autogen

## Paper Classification

- **Type**: Applied research (framework design and implementation)
- **Impact**: 25,000+ GitHub stars, widely adopted in industry
- **Prerequisites**: Understanding of multi-agent systems, LLM APIs, Python

## Why This Paper Matters

AutoGen represents a paradigm shift in how we build LLM applications. Instead of treating agents as isolated units, AutoGen models them as conversational participants that can engage in complex dialogues. This enables:

1. **Modular Design**: Agents as reusable components
2. **Flexible Orchestration**: Conversation-based coordination
3. **Human Integration**: Seamless human-in-the-loop patterns
4. **Code Execution**: Safe sandboxed code environments

This framework (and similar ones like LangGraph, CrewAI) are the foundation for building production agent systems.

---

## Secondary Readings

### LangGraph Documentation

- **Source**: LangChain
- **Link**: https://langchain-ai.github.io/langgraph
- **Focus**: Conceptual guides, StateGraph, and persistence

#### Key Sections to Read
1. Introduction and core concepts
2. StateGraph vs MessageGraph
3. Checkpointing and persistence
4. Human-in-the-loop patterns

### TaskWeaver: A Code-First Agent Framework

- **Authors**: Bo Qiao, Liqun Li, Xu Zhang, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2311.17541
- **Code**: https://github.com/microsoft/TaskWeaver

#### Why Read This
- Represents code-generation-as-action paradigm
- Interesting contrast to tool-calling approaches
- Production-oriented design decisions

### Classic Reference: Intelligent Agents - Theory and Practice

- **Authors**: Michael Wooldridge, Nicholas R. Jennings
- **Year**: 1995
- **Venue**: Knowledge Engineering Review
- **DOI**: 10.1017/S0269888900008122

#### Historical Context
- Original definitions of intelligent agents
- BDI (Belief-Desire-Intention) architecture
- Multi-agent system theoretical foundations

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: What challenges exist when building multi-agent systems?
   - Coordination overhead
   - State management complexity
   - Error handling across agents
   - Human oversight requirements

2. **Prior Work**: How did earlier frameworks handle these challenges?
   - LangChain: Sequential chains with limited branching
   - Direct API calls: No abstraction, lots of boilerplate
   - Custom solutions: Not reusable

3. **Your Hypothesis**: What abstractions make agent frameworks most useful?

### During Reading: AutoGen

#### Section 2: System Design

**Core Abstraction - ConversableAgent**:

| Property | Description |
|----------|-------------|
| System message | Defines agent role and behavior |
| LLM config | Model, temperature, tools |
| Human input mode | NEVER, TERMINATE, ALWAYS |
| Code execution config | Docker, sandbox settings |

```python
# AutoGen's core abstraction
class ConversableAgent:
    def __init__(self, name, system_message, llm_config, human_input_mode):
        ...

    def initiate_chat(self, recipient, message):
        """Start a conversation with another agent."""
        ...

    def generate_reply(self, messages, sender):
        """Generate a response given conversation history."""
        ...
```

- [ ] How does the conversation loop work?
- [ ] What are the built-in agent types?
- [ ] How is termination handled?

#### Section 3: Conversation Patterns

**Key Patterns**:

| Pattern | Description | Use Case |
|---------|-------------|----------|
| Two-agent | Simple back-and-forth | Code generation + review |
| Sequential | Agents in order | Pipeline processing |
| Group chat | Multiple agents, one manager | Complex collaboration |
| Nested | Agents within agents | Hierarchical tasks |

- [ ] How does GroupChatManager decide who speaks next?
- [ ] What are the speaker selection strategies?
- [ ] How do you prevent infinite loops?

#### Section 4: Code Execution

**Sandboxing Options**:

| Option | Safety | Setup Complexity |
|--------|--------|-----------------|
| Local execution | Low | None |
| Docker container | High | Medium |
| E2B sandbox | High | Low (cloud) |

- [ ] How does code execution integrate with conversation?
- [ ] What security considerations are discussed?
- [ ] How are execution results returned to agents?

### During Reading: LangGraph

#### Key Concepts

**StateGraph**:
```python
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    messages: list[BaseMessage]
    next_action: str

graph = StateGraph(AgentState)
graph.add_node("agent", call_agent)
graph.add_node("tools", execute_tools)
graph.add_edge("agent", "tools")
graph.add_conditional_edges("tools", should_continue)
```

**Core Abstractions**:

| Concept | Description |
|---------|-------------|
| State | Typed dictionary passed between nodes |
| Node | Function that processes state |
| Edge | Connection between nodes (conditional or fixed) |
| Reducer | Function that merges state updates |
| Checkpoint | Serialized state snapshot |

- [ ] How does StateGraph differ from MessageGraph?
- [ ] What is a reducer and when do you need custom ones?
- [ ] How does checkpointing enable persistence?

### After Reading

Compare the frameworks:

| Aspect | AutoGen | LangGraph | TaskWeaver |
|--------|---------|-----------|------------|
| Core abstraction | Conversable agents | State graph | Code-first agents |
| Coordination | Message passing | Graph edges | Planner-executor |
| State management | Implicit (messages) | Explicit (typed state) | Session state |
| Human integration | Human proxy agent | Interrupt nodes | Natural pauses |
| Code execution | Built-in | Separate tool | Core primitive |
| Learning curve | Medium | Higher | Medium |
| Flexibility | High | Very high | Medium |

---

## Discussion Questions (Seminar)

Prepare to discuss:

### Conceptual
1. What is the fundamental difference between conversation-based (AutoGen) and graph-based (LangGraph) approaches?
2. Why do modern frameworks emphasize explicit state management?
3. How should frameworks handle errors that occur mid-execution?

### Technical
1. When should you choose checkpointing at node vs. edge level?
2. How do different frameworks handle tool schema definition?
3. What are the implications of synchronous vs. asynchronous agent execution?
4. How do you implement cross-agent memory sharing?

### Practical
1. Which framework would you choose for a customer service chatbot?
2. How would you migrate from LangChain to LangGraph?
3. What's the overhead of using these frameworks vs. direct API calls?

### Research
1. What gaps exist in current framework support for multi-modal agents?
2. How might hierarchical agent architectures be better supported?
3. What evaluation metrics are missing for framework comparison?

---

## Key Takeaways to Remember

1. **AutoGen's Insight**: Model agents as conversation participants, not isolated processors.

2. **LangGraph's Insight**: Explicit state graphs enable complex control flow and persistence.

3. **Framework Trade-offs**:
   - More abstraction = less boilerplate, more constraints
   - Implicit state = simpler, but harder to debug
   - Explicit state = verbose, but transparent

4. **When to Use Each**:
   | Scenario | Recommended |
   |----------|-------------|
   | Simple two-agent chat | AutoGen |
   | Complex state machine | LangGraph |
   | Code-heavy tasks | TaskWeaver |
   | Quick prototyping | AutoGen |
   | Production deployment | LangGraph |

5. **Common Pitfalls**:
   - Forgetting termination conditions (infinite loops)
   - Inadequate error handling
   - State bloat from accumulated messages
   - Insufficient logging/observability

---

## Supplementary Readings

| Paper/Resource | Relationship |
|---------------|-------------|
| CrewAI documentation | Role-based agent framework |
| MetaGPT (Hong et al., 2023) | SOP-based multi-agent |
| CAMEL (Li et al., 2023) | Role-playing communication |
| AgentVerse (Chen et al., 2023) | Multi-agent simulation |
| Semantic Kernel docs | Microsoft's orchestration library |

---

## Framework Comparison Matrix

| Feature | AutoGen | LangGraph | CrewAI | MetaGPT |
|---------|---------|-----------|--------|---------|
| Multi-agent | Yes | Yes | Yes | Yes |
| State persistence | Limited | Full | Limited | Yes |
| Human-in-loop | Yes | Yes | Yes | Limited |
| Code execution | Docker | External | External | Yes |
| Async support | Yes | Yes | No | Limited |
| Type safety | No | Yes | No | Partial |
| Learning curve | Medium | High | Low | Medium |
| Production ready | Yes | Yes | Partial | Partial |

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read AutoGen paper Sections 1-4
- [ ] Completed LangGraph quickstart tutorial
- [ ] Understood StateGraph vs. MessageGraph
- [ ] Compared conversation-based vs. graph-based paradigms
- [ ] Tried running one AutoGen example
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to multi-agent concepts from Week 5

## Reading Schedule

| Day | Reading | Time |
|-----|---------|------|
| 1 | LangGraph conceptual docs | 45 min |
| 2 | AutoGen paper (Sections 1-3) | 60 min |
| 3 | AutoGen paper (Sections 4-5) | 45 min |
| 4 | TaskWeaver (skim) | 30 min |
| 5 | Wooldridge & Jennings (optional) | 45 min |

## Notes Template

```markdown
## Agent Frameworks Reading Notes

**Date**: [your date]

### AutoGen Summary
- Core abstraction: [ConversableAgent description]
- Conversation patterns: [list 3-4]
- Code execution approach: [description]

### LangGraph Summary
- Core abstraction: [StateGraph description]
- Key concepts: [State, Node, Edge, Checkpoint]
- When to use: [scenarios]

### Framework Comparison
| Aspect | AutoGen | LangGraph |
|--------|---------|-----------|
| Coordination | | |
| State management | | |
| Best for | | |

### Strengths of Each
AutoGen:
- [Strength 1]
- [Strength 2]

LangGraph:
- [Strength 1]
- [Strength 2]

### Weaknesses of Each
AutoGen:
- [Weakness 1]
- [Weakness 2]

LangGraph:
- [Weakness 1]
- [Weakness 2]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Course
[How do frameworks enable the agent patterns we've studied?]
```

## Implementation Exercise

Design a simple research assistant using your framework of choice:

```python
# Sketch your design
# Requirements:
# 1. Search agent: queries academic databases
# 2. Summarizer agent: condenses findings
# 3. Writer agent: produces final report
# 4. Human approval before final output

# AutoGen approach:
researcher = AssistantAgent("researcher", system_message="...")
summarizer = AssistantAgent("summarizer", system_message="...")
writer = AssistantAgent("writer", system_message="...")
human = UserProxyAgent("human", human_input_mode="TERMINATE")

# LangGraph approach:
class ResearchState(TypedDict):
    query: str
    search_results: list
    summary: str
    report: str
    approved: bool

graph = StateGraph(ResearchState)
graph.add_node("search", search_node)
graph.add_node("summarize", summarize_node)
graph.add_node("write", write_node)
graph.add_node("human_review", human_review_node)
```

Compare: Which approach feels more natural for this task?

## Key Vocabulary

- **StateGraph**: LangGraph's core abstraction for stateful agent workflows
- **Checkpoint**: Serialized snapshot of agent state at a graph node
- **Reducer**: Function that merges state updates (e.g., append vs. replace)
- **ConversableAgent**: AutoGen's base class for agents that can converse
- **GroupChat**: AutoGen pattern for multi-agent conversations
- **Thread**: Isolation boundary for conversations (enables multi-tenancy)
- **Human-in-the-loop**: Design pattern where humans can intervene in agent execution
- **Code sandbox**: Isolated environment for safe code execution
