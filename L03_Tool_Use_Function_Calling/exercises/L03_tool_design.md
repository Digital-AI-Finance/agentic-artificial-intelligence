# Exercise L03: Tool Design and Function Calling Challenge

**Week 3 - Tool Use and Function Calling**

## Overview

Design and implement a complete toolset for an LLM agent, including tool definitions with JSON Schema, handlers with proper validation, and robust error handling strategies.

## Learning Objectives

- **Primary (Create)**: Design tool schemas following OpenAI/Anthropic specifications
- **Secondary (Apply)**: Implement tool handlers with proper validation and error handling
- **Tertiary (Analyze)**: Evaluate tool design decisions and their impact on agent performance

## Prerequisites

- OpenAI/Anthropic API access
- Python 3.10+
- Understanding of JSON Schema
- Basic knowledge of API design principles

## Problem Statement

LLM agents extend their capabilities through tools, but poorly designed tools lead to:
- Ambiguous tool selection (LLM picks wrong tool)
- Parameter hallucination (LLM invents invalid parameters)
- Silent failures (errors not communicated back to LLM)
- Security vulnerabilities (unvalidated inputs)

This exercise develops skills in designing tools that are clear, safe, and robust.

### Task 1: Design Tool Schemas (30 points)

Design JSON Schema tool definitions for the following tools. Use either OpenAI function calling or Anthropic tool use format (specify which).

**Required Tools:**

1. `search_database` - Query a product database
   - Parameters: query (required), category (optional), max_results (optional, default 10)
   - Must support filtering by category
   - Return type: list of product objects

2. `send_email` - Send an email notification
   - Parameters: to (required), subject (required), body (required), cc (optional)
   - Must validate email format
   - Return type: confirmation with message_id

3. `create_calendar_event` - Schedule a meeting
   - Parameters: title (required), start_time (required, ISO format), end_time (required), attendees (required, list), description (optional)
   - Must validate time range (end > start)
   - Return type: event object with id and link

**Schema Quality Requirements:**
| Criterion | Description |
|-----------|-------------|
| Descriptions | Action-oriented, explain what tool does and when to use it |
| Parameter names | Clear, consistent naming (snake_case or camelCase) |
| Types | Correct JSON Schema types (string, number, array, object) |
| Required vs optional | Explicitly marked, sensible defaults |
| Constraints | Enums, patterns, min/max where applicable |

**Example Schema (OpenAI format):**
```json
{
  "type": "function",
  "function": {
    "name": "search_database",
    "description": "Search the product database for items matching a query. Use when the user asks about products, availability, or pricing.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string",
          "description": "Search query for finding products"
        },
        "category": {
          "type": "string",
          "enum": ["electronics", "clothing", "home", "sports"],
          "description": "Filter results by product category"
        },
        "max_results": {
          "type": "integer",
          "default": 10,
          "minimum": 1,
          "maximum": 100,
          "description": "Maximum number of results to return"
        }
      },
      "required": ["query"]
    }
  }
}
```

### Task 2: Implement Tool Handlers (40 points)

Write Python implementations for each tool with proper validation:

```python
from typing import Optional
from dataclasses import dataclass
from datetime import datetime
import re

@dataclass
class ToolResult:
    success: bool
    data: dict | None
    error: str | None

def search_database(query: str, category: str = None, max_results: int = 10) -> ToolResult:
    """
    Search the product database.

    Args:
        query: Search query string
        category: Optional category filter
        max_results: Maximum results to return (1-100)

    Returns:
        ToolResult with products list or error message
    """
    # Implement validation and simulated search
    pass

def send_email(to: str, subject: str, body: str, cc: str = None) -> ToolResult:
    """
    Send an email notification.

    Args:
        to: Recipient email address
        subject: Email subject line
        body: Email body content
        cc: Optional CC recipient

    Returns:
        ToolResult with message_id or error
    """
    # Implement email validation and simulated sending
    pass

def create_calendar_event(
    title: str,
    start_time: str,
    end_time: str,
    attendees: list[str],
    description: str = None
) -> ToolResult:
    """
    Create a calendar event.

    Args:
        title: Event title
        start_time: Start time in ISO format
        end_time: End time in ISO format
        attendees: List of attendee emails
        description: Optional event description

    Returns:
        ToolResult with event details or error
    """
    # Implement time validation and simulated creation
    pass
```

**Implementation Requirements:**

| Requirement | Description |
|-------------|-------------|
| Input validation | Check types, ranges, formats before processing |
| Error messages | Clear, actionable messages the LLM can understand |
| Return format | Consistent ToolResult structure for all tools |
| Simulated execution | No real APIs needed, but realistic behavior |
| Type hints | Full type annotations on all functions |
| Docstrings | Complete documentation with Args and Returns |

### Task 3: Error Handling (30 points)

Implement comprehensive error handling for your tools:

**3a: Input Validation Errors (10 points)**
```python
# Example: Invalid email format
result = send_email(
    to="not-an-email",
    subject="Test",
    body="Hello"
)
# Should return:
# ToolResult(success=False, data=None,
#            error="Invalid email format for 'to': expected format 'user@domain.com'")
```

**3b: Execution Errors (10 points)**
```python
# Example: Simulated API failure
def search_database_with_failure_simulation(query: str, ...) -> ToolResult:
    # Simulate 10% failure rate
    if random.random() < 0.1:
        return ToolResult(
            success=False,
            data=None,
            error="Database temporarily unavailable. Please retry in a moment."
        )
    # ... normal execution
```

**3c: Recovery Strategies (10 points)**

Implement a tool executor with retry logic:
```python
class ToolExecutor:
    def __init__(self, max_retries: int = 3, retry_delay: float = 1.0):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.tools = {}

    def register_tool(self, name: str, handler: callable, schema: dict):
        """Register a tool with its handler and schema."""
        pass

    def execute(self, tool_name: str, arguments: dict) -> ToolResult:
        """Execute a tool with automatic retry on transient failures."""
        pass

    def validate_arguments(self, tool_name: str, arguments: dict) -> tuple[bool, str]:
        """Validate arguments against tool schema before execution."""
        pass
```

**Error Categories to Handle:**
| Category | Example | Recovery Strategy |
|----------|---------|-------------------|
| Validation | Missing required param | Return clear error, no retry |
| Transient | Network timeout | Retry with backoff |
| Rate limit | Too many requests | Wait and retry |
| Permanent | Resource not found | Return error, no retry |

## Test Cases Required

Include at least 15 test cases covering:

| Category | Count | Examples |
|----------|-------|----------|
| Valid inputs | 5 | Normal usage for each tool |
| Validation failures | 5 | Missing params, invalid types, out of range |
| Edge cases | 3 | Empty strings, very long inputs, special characters |
| Error recovery | 2 | Retry success, max retries exceeded |

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| tool_schemas.json | JSON | All 3 tool schemas |
| tool_handlers.py | Python | Implementation with validation |
| tool_executor.py | Python | Executor with retry logic |
| test_tools.py | Python | 15+ test cases |
| analysis.md | Markdown | Design decisions (300-500 words) |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Schema Design | 30 | Clear descriptions, proper types, constraints |
| Handler Implementation | 40 | Correct logic, validation, return format |
| Error Handling | 20 | Comprehensive error cases, recovery |
| Code Quality | 10 | Clean code, documentation, type hints |

### Detailed Rubric

**Schema Design (30 points)**
- 10 points: Descriptions are clear and actionable
- 10 points: Types and constraints are correct
- 5 points: Required/optional properly marked
- 5 points: Enums and patterns where appropriate

**Handler Implementation (40 points)**
- 15 points: Input validation is thorough
- 15 points: Return format is consistent
- 5 points: Type hints complete
- 5 points: Docstrings complete

**Error Handling (20 points)**
- 5 points: Validation errors are clear
- 5 points: Execution errors are handled
- 5 points: Retry logic works correctly
- 5 points: Error messages are LLM-friendly

**Code Quality (10 points)**
- 5 points: Clean, readable code
- 5 points: All tests pass

## Resources

- Schick et al. (2023). "Toolformer" - arXiv:2302.04761
- Patil et al. (2023). "Gorilla" - arXiv:2305.15334
- OpenAI Function Calling docs: https://platform.openai.com/docs/guides/function-calling
- Anthropic Tool Use docs: https://docs.anthropic.com/claude/docs/tool-use
- JSON Schema Specification: https://json-schema.org/

## Submission

- **Format**: Python files + JSON schemas + Markdown analysis
- **Filename**: `L03_exercise_[your_name]/`
- **Due**: End of Week 3

## Hints

- Use `pydantic` or `dataclasses` for structured returns
- Test your schemas with actual LLM calls to check selection accuracy
- Error messages should tell the LLM how to fix the problem
- Consider rate limiting from the LLM's perspective (it may call tools rapidly)
- Use `jsonschema` library for programmatic schema validation

## Sample Implementation Skeleton

```python
import json
import random
import time
from dataclasses import dataclass, asdict
from typing import Optional, Callable
from datetime import datetime
import re

@dataclass
class ToolResult:
    success: bool
    data: Optional[dict]
    error: Optional[str]

    def to_dict(self) -> dict:
        return asdict(self)

class ToolRegistry:
    def __init__(self):
        self.tools: dict[str, dict] = {}

    def register(self, name: str, handler: Callable, schema: dict):
        self.tools[name] = {
            "handler": handler,
            "schema": schema
        }

    def list_tools(self) -> list[dict]:
        """Return schemas for all registered tools."""
        return [t["schema"] for t in self.tools.values()]

    def execute(self, name: str, arguments: dict) -> ToolResult:
        """Execute a tool by name with given arguments."""
        if name not in self.tools:
            return ToolResult(
                success=False,
                data=None,
                error=f"Unknown tool: {name}. Available: {list(self.tools.keys())}"
            )

        handler = self.tools[name]["handler"]
        return handler(**arguments)

# Email validation helper
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# ISO datetime validation helper
def parse_iso_datetime(dt_string: str) -> Optional[datetime]:
    try:
        return datetime.fromisoformat(dt_string.replace('Z', '+00:00'))
    except ValueError:
        return None

# Implement your tools here...
```

## Bonus Challenge (+10 points)

Implement a tool registry that:
- Allows dynamic tool registration at runtime
- Provides tool discovery (list available tools with descriptions)
- Validates tool calls against schema before execution
- Logs all tool invocations with timing information
- Supports tool versioning (v1, v2 of same tool)

## Time Estimate
- Minimum: 3 hours
- Expected: 5 hours
- Maximum: 8 hours
