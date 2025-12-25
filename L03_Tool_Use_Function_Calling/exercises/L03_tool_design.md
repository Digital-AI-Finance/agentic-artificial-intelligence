# Exercise L03: Tool Design Challenge

**Week 3 - Tool Use and Function Calling**

## Overview
Design and implement a complete toolset for an LLM agent, including tool definitions, handlers, and error handling.

## Task 1: Design Tool Schemas (30 points)

Design JSON Schema tool definitions for the following tools. Use either OpenAI or Anthropic format (specify which).

**Required Tools:**
1. `search_database` - Query a product database
   - Parameters: query, category (optional), max_results (optional)

2. `send_email` - Send an email notification
   - Parameters: to, subject, body, cc (optional)

3. `create_calendar_event` - Schedule a meeting
   - Parameters: title, start_time, end_time, attendees, description (optional)

**Requirements:**
- Clear, actionable descriptions
- Proper JSON Schema types
- Required vs optional parameters marked
- Enum constraints where appropriate

## Task 2: Implement Tool Handlers (40 points)

Write Python implementations for each tool:

```python
def search_database(query: str, category: str = None, max_results: int = 10) -> dict:
    """Implement database search logic."""
    pass

def send_email(to: str, subject: str, body: str, cc: str = None) -> dict:
    """Implement email sending logic."""
    pass

def create_calendar_event(title: str, start_time: str, end_time: str,
                          attendees: list, description: str = None) -> dict:
    """Implement calendar event creation."""
    pass
```

**Requirements:**
- Input validation with clear error messages
- Structured return format (success/error)
- Simulated execution (no real APIs required)
- Type hints and docstrings

## Task 3: Error Handling (30 points)

Implement robust error handling for your tools:

1. **Input Validation Errors**
   - Missing required parameters
   - Invalid parameter types
   - Out-of-range values

2. **Execution Errors**
   - Simulated API failures
   - Timeout handling
   - Rate limiting

3. **Recovery Strategies**
   - Retry logic for transient failures
   - Graceful degradation
   - Informative error messages for LLM

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Schema Design | 30 | Clear descriptions, proper types, constraints |
| Handler Implementation | 40 | Correct logic, validation, return format |
| Error Handling | 20 | Comprehensive error cases, recovery |
| Code Quality | 10 | Clean code, documentation, type hints |

## Submission

1. Jupyter notebook with all implementations
2. Test cases demonstrating each tool
3. Written analysis (200-300 words) on design decisions

## Bonus Challenge (+10 points)

Implement a tool registry that:
- Allows dynamic tool registration
- Provides tool discovery (list available tools)
- Validates tool calls before execution
- Logs all tool invocations
