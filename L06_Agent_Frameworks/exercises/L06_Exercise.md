# Week 6 Exercise: Multi-Framework Agent Implementation

## Learning Objectives
- **Apply**: Implement agents in multiple frameworks
- **Analyze**: Compare framework characteristics empirically
- **Evaluate**: Assess trade-offs for different use cases

## Problem Statement

Implement the same agent functionality in three different frameworks and compare their characteristics.

### Task: Research Assistant Agent

Build an agent that can:
1. Search a knowledge base (simulated)
2. Perform calculations
3. Summarize findings
4. Track conversation context

### Requirements

#### Part 1: LangGraph Implementation (40 points)
```python
# Implement a StateGraph with:
# - Agent node (LLM decision making)
# - Tool node (search + calculator)
# - Conditional routing
# - Checkpointing enabled

# Your state schema should include:
# - messages: list of conversation messages
# - sources: list of retrieved sources
# - iteration_count: safety limit counter
```

#### Part 2: AutoGen Implementation (30 points)
```python
# Implement the same functionality with:
# - UserProxyAgent (represents user)
# - AssistantAgent (LLM-powered)
# - Code execution for calculations
# - Group chat if using multiple specialists
```

#### Part 3: Comparison Analysis (30 points)

Create a comparison table evaluating:

| Criterion | LangGraph | AutoGen | Notes |
|-----------|-----------|---------|-------|
| Lines of code | | | |
| Setup complexity | | | |
| State management | | | |
| Debugging ease | | | |
| Error handling | | | |
| Extensibility | | | |

## Evaluation Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| LangGraph correctness | 25 | Graph compiles and runs correctly |
| LangGraph features | 15 | Uses checkpointing, streaming, proper state |
| AutoGen correctness | 20 | Agents communicate and execute tools |
| AutoGen features | 10 | Uses code execution, proper termination |
| Comparison depth | 20 | Insightful analysis with evidence |
| Code quality | 10 | Clean, documented, follows patterns |

## Deliverables

1. `langgraph_agent.py` - Complete LangGraph implementation
2. `autogen_agent.py` - Complete AutoGen implementation
3. `comparison.md` - Framework comparison analysis
4. `demo.ipynb` - Notebook demonstrating both implementations

## Resources

- LangGraph docs: https://langchain-ai.github.io/langgraph
- AutoGen docs: https://microsoft.github.io/autogen
- Reference notebook: `L06_LangGraph_Agent.ipynb`

## Time Estimate
- Minimum: 3 hours
- Expected: 5 hours
- Maximum: 8 hours (with extensions)

## Extension (Optional)

Implement a third version using CrewAI with role-based agents and compare all three.
