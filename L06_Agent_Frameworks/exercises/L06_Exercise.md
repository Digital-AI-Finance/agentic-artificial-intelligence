# Exercise L06: Multi-Framework Agent Implementation

**Week 6 - Agent Frameworks**

## Overview

Implement the same agent functionality across multiple frameworks (LangGraph, AutoGen) to understand framework trade-offs, design patterns, and practical considerations for production deployment.

## Learning Objectives

- **Primary (Apply)**: Implement agents using LangGraph StateGraph and AutoGen patterns
- **Secondary (Analyze)**: Compare framework characteristics through empirical implementation
- **Tertiary (Evaluate)**: Assess trade-offs and select appropriate frameworks for use cases

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- LangGraph 0.2+, AutoGen 0.2+
- Understanding of agent patterns (ReAct, tool use)

## Problem Statement

Agent frameworks provide abstractions that simplify development, but each makes different trade-offs:
- **LangGraph**: Graph-based state machines, explicit control flow, checkpointing
- **AutoGen**: Conversation-based, code execution, multi-agent by default

Choosing the right framework requires understanding these trade-offs through hands-on experience.

### Task: Research Assistant Agent

Build an agent that can:
1. Search a knowledge base (simulated or real)
2. Perform calculations
3. Summarize findings
4. Track conversation context across turns

### Part 1: LangGraph Implementation (40 points)

Implement a StateGraph-based agent with proper state management:

**1a: State Schema (10 points)**
```python
from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    """State schema for the research assistant."""
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sources: list[dict]           # Retrieved sources
    iteration_count: int          # Safety limit counter
    current_task: str             # Current subtask being worked on
    final_answer: str | None      # Final synthesized answer
```

**1b: Tool Definitions (10 points)**
```python
from langchain_core.tools import tool

@tool
def search_knowledge_base(query: str) -> list[dict]:
    """Search the knowledge base for relevant information.

    Args:
        query: Search query string

    Returns:
        List of relevant documents with title, content, and source
    """
    # Simulated search - in production, replace with real retrieval
    knowledge_base = [
        {"title": "AI Agents Overview", "content": "AI agents are systems that...", "source": "doc1"},
        {"title": "LangGraph Tutorial", "content": "LangGraph provides...", "source": "doc2"},
        {"title": "Multi-Agent Systems", "content": "Multiple agents can...", "source": "doc3"},
    ]
    # Simple keyword matching for simulation
    results = [doc for doc in knowledge_base if query.lower() in doc["content"].lower()]
    return results if results else [{"title": "No results", "content": "No matching documents found", "source": "none"}]

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression.

    Args:
        expression: Mathematical expression to evaluate (e.g., "2 + 2 * 3")

    Returns:
        Result of the calculation
    """
    try:
        # Safe evaluation (in production, use a proper math parser)
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return "Error: Invalid characters in expression"
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def summarize_sources(sources: list[dict]) -> str:
    """Summarize the key findings from retrieved sources.

    Args:
        sources: List of source documents to summarize

    Returns:
        Synthesized summary of the sources
    """
    if not sources:
        return "No sources to summarize."
    titles = [s.get("title", "Unknown") for s in sources]
    return f"Summary of {len(sources)} sources: {', '.join(titles)}"
```

**1c: Graph Construction (15 points)**
```python
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

def create_research_agent():
    """Create the LangGraph research assistant."""

    # Define the agent node
    def agent_node(state: AgentState) -> dict:
        """Main agent reasoning node."""
        messages = state["messages"]
        iteration = state.get("iteration_count", 0)

        # Safety check
        if iteration >= 10:
            return {
                "messages": [AIMessage(content="Maximum iterations reached. Stopping.")],
                "final_answer": "Task incomplete due to iteration limit."
            }

        # Call LLM with tools
        response = llm.bind_tools(tools).invoke(messages)

        return {
            "messages": [response],
            "iteration_count": iteration + 1
        }

    # Define the tool execution node
    tool_node = ToolNode(tools=[search_knowledge_base, calculator, summarize_sources])

    # Define routing logic
    def should_continue(state: AgentState) -> str:
        """Determine next step based on last message."""
        last_message = state["messages"][-1]

        # If LLM made tool calls, execute them
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"

        # Otherwise, end
        return "end"

    # Build the graph
    workflow = StateGraph(AgentState)

    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("agent")

    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )

    workflow.add_edge("tools", "agent")

    # Compile with checkpointing
    memory = MemorySaver()
    return workflow.compile(checkpointer=memory)
```

**1d: Streaming and Checkpointing (5 points)**
```python
def run_with_streaming(agent, question: str, thread_id: str = "default"):
    """Run the agent with streaming output."""
    config = {"configurable": {"thread_id": thread_id}}

    initial_state = {
        "messages": [HumanMessage(content=question)],
        "sources": [],
        "iteration_count": 0,
        "current_task": "",
        "final_answer": None
    }

    # Stream the execution
    for event in agent.stream(initial_state, config):
        for node_name, output in event.items():
            print(f"\n--- {node_name} ---")
            if "messages" in output:
                for msg in output["messages"]:
                    print(f"  {msg.type}: {msg.content[:100]}...")

    # Return final state
    return agent.get_state(config)
```

### Part 2: AutoGen Implementation (30 points)

Implement the same functionality using AutoGen's conversation-based approach:

**2a: Agent Configuration (10 points)**
```python
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Configure LLM
config_list = [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]

llm_config = {
    "config_list": config_list,
    "timeout": 120,
    "temperature": 0,
}

# Create the assistant agent
assistant = AssistantAgent(
    name="ResearchAssistant",
    system_message="""You are a research assistant that helps users find and
    analyze information. You can:
    1. Search the knowledge base for relevant documents
    2. Perform calculations
    3. Summarize findings

    Always explain your reasoning and cite sources when available.
    When the task is complete, say TERMINATE.""",
    llm_config=llm_config,
)

# Create the user proxy with code execution
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # No human input needed
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # Set True in production
    },
)
```

**2b: Tool Registration (10 points)**
```python
# Register tools with the assistant
@user_proxy.register_for_execution()
@assistant.register_for_llm(description="Search the knowledge base")
def search_knowledge_base_autogen(query: str) -> str:
    """Search for relevant information."""
    results = search_knowledge_base.invoke({"query": query})
    return str(results)

@user_proxy.register_for_execution()
@assistant.register_for_llm(description="Evaluate a math expression")
def calculator_autogen(expression: str) -> str:
    """Perform calculations."""
    return calculator.invoke({"expression": expression})
```

**2c: Execution and State Tracking (10 points)**
```python
def run_autogen_agent(question: str) -> dict:
    """Run the AutoGen research assistant."""
    # Track execution metadata
    start_time = time.time()
    token_count = 0

    # Initiate the conversation
    result = user_proxy.initiate_chat(
        assistant,
        message=question,
        summary_method="reflection_with_llm",
    )

    # Extract conversation history
    history = []
    for msg in user_proxy.chat_messages[assistant]:
        history.append({
            "role": msg.get("role", "unknown"),
            "content": msg.get("content", "")[:200],
            "name": msg.get("name", "")
        })

    return {
        "final_answer": result.summary,
        "conversation_length": len(history),
        "execution_time": time.time() - start_time,
        "history": history
    }
```

### Part 3: Comparison Analysis (30 points)

Create a detailed comparison based on your implementations:

**3a: Quantitative Comparison (15 points)**

Run both implementations on the same 5 test queries:

| Query | LangGraph (tokens) | AutoGen (tokens) | LangGraph (time) | AutoGen (time) |
|-------|-------------------|------------------|------------------|----------------|
| "What is RAG?" | | | | |
| "Calculate 15% of $320" | | | | |
| "Compare agents A and B" | | | | |
| "Summarize recent AI news" | | | | |
| "Multi-step: search then calculate" | | | | |

**3b: Qualitative Comparison (15 points)**

Create a comparison table:

| Criterion | LangGraph | AutoGen | Winner | Notes |
|-----------|-----------|---------|--------|-------|
| Lines of code | | | | |
| Setup complexity | | | | |
| State management | | | | |
| Debugging ease | | | | |
| Error handling | | | | |
| Extensibility | | | | |
| Documentation | | | | |
| Community support | | | | |
| Production readiness | | | | |

**Analysis Questions to Answer:**
1. Which framework was easier to implement? Why?
2. Which provides better observability into agent behavior?
3. Which is better suited for production deployment?
4. When would you choose one over the other?

## Test Scenarios

Include at least 10 test scenarios:

| Scenario | Input | Expected Behavior | Pass/Fail (LG) | Pass/Fail (AG) |
|----------|-------|-------------------|----------------|----------------|
| Simple query | "What is AI?" | Returns relevant info | | |
| Calculation | "What is 2+2?" | Returns 4 | | |
| Multi-turn | Follow-up questions | Maintains context | | |
| Tool selection | Ambiguous query | Picks correct tool | | |
| Error handling | Invalid input | Graceful failure | | |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| langgraph_agent.py | Python | Complete StateGraph implementation |
| autogen_agent.py | Python | Complete AutoGen implementation |
| comparison.md | Markdown | Detailed framework comparison (500+ words) |
| test_results.json | JSON | Quantitative comparison data |
| demo.ipynb | Jupyter | Interactive demonstration of both |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| LangGraph Implementation | 40 | Working agent with all features |
| AutoGen Implementation | 30 | Working agent with all features |
| Comparison Analysis | 30 | Insightful, evidence-based comparison |

### Detailed Rubric

**LangGraph (40 points)**
- 10 points: State schema properly defined
- 10 points: Tools implemented and working
- 15 points: Graph compiles and runs correctly
- 5 points: Checkpointing and streaming work

**AutoGen (30 points)**
- 10 points: Agents properly configured
- 10 points: Tools registered and working
- 10 points: Conversation terminates correctly

**Comparison (30 points)**
- 10 points: Quantitative metrics collected
- 10 points: Qualitative analysis is thoughtful
- 10 points: Recommendations are justified

## Resources

- LangGraph documentation: https://langchain-ai.github.io/langgraph
- AutoGen documentation: https://microsoft.github.io/autogen
- LangChain tools: https://python.langchain.com/docs/modules/tools
- Qiao et al. (2024). "Agent Survey" - arXiv:2309.07864

## Submission

- **Format**: Python files + Jupyter notebook + Markdown analysis
- **Filename**: `L06_exercise_[your_name]/`
- **Due**: End of Week 6

## Hints

- Start with LangGraph - its explicit state makes debugging easier
- Use the same LLM (e.g., GPT-4) for fair comparison
- Log all LLM calls to count tokens accurately
- Test tool execution separately before integrating into agents
- AutoGen's code execution can be tricky - start with `use_docker=False`

## Sample Test Harness

```python
import json
import time
from dataclasses import dataclass, asdict

@dataclass
class TestResult:
    query: str
    framework: str
    success: bool
    answer: str
    tokens_used: int
    execution_time: float
    error: str | None = None

def run_comparison_test(query: str) -> tuple[TestResult, TestResult]:
    """Run the same query on both frameworks and compare."""

    # Test LangGraph
    lg_start = time.time()
    try:
        lg_result = run_with_streaming(langgraph_agent, query)
        lg_success = True
        lg_answer = lg_result.values.get("final_answer", "")
        lg_error = None
    except Exception as e:
        lg_success = False
        lg_answer = ""
        lg_error = str(e)
    lg_time = time.time() - lg_start

    # Test AutoGen
    ag_start = time.time()
    try:
        ag_result = run_autogen_agent(query)
        ag_success = True
        ag_answer = ag_result.get("final_answer", "")
        ag_error = None
    except Exception as e:
        ag_success = False
        ag_answer = ""
        ag_error = str(e)
    ag_time = time.time() - ag_start

    return (
        TestResult(query, "LangGraph", lg_success, lg_answer, 0, lg_time, lg_error),
        TestResult(query, "AutoGen", ag_success, ag_answer, 0, ag_time, ag_error)
    )

def run_full_comparison(queries: list[str]) -> dict:
    """Run full comparison suite."""
    results = []
    for query in queries:
        lg_result, ag_result = run_comparison_test(query)
        results.append({"langgraph": asdict(lg_result), "autogen": asdict(ag_result)})

    return {"results": results, "timestamp": time.time()}
```

## Extension (Optional, +15 points)

Implement a third version using CrewAI with role-based agents:

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="Researcher",
    goal="Find accurate information on any topic",
    backstory="Expert at searching and synthesizing information",
    tools=[search_tool, calculator_tool]
)

# Define tasks and crew...
```

Compare all three frameworks on the same metrics.

## Time Estimate
- Minimum: 4 hours
- Expected: 6 hours
- Maximum: 10 hours (with CrewAI extension)
