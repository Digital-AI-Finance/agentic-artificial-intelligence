---
layout: default
title: Code Snippets
nav_order: 8
---

# Code Snippets

Reusable code patterns for building agentic AI systems.

## Agent Basics

### Simple ReAct Agent

```python
from openai import OpenAI

client = OpenAI()

def react_agent(question: str, tools: dict, max_steps: int = 5):
    """Simple ReAct agent loop."""
    history = []

    for step in range(max_steps):
        prompt = f"""Question: {question}
Previous steps: {history}

Think step by step. Use format:
Thought: your reasoning
Action: tool_name[input]

Available tools: {list(tools.keys())}"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        output = response.choices[0].message.content
        # Parse and execute action...

        if "Final Answer" in output:
            return output

    return "Max steps reached"
```

### Tool Definition Template

```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class Tool:
    name: str
    description: str
    func: Callable

    def run(self, input_str: str) -> str:
        try:
            return self.func(input_str)
        except Exception as e:
            return f"Error: {e}"

# Example tool
search_tool = Tool(
    name="search",
    description="Search for information",
    func=lambda q: f"Results for: {q}"
)
```

## Prompting Patterns

### Chain-of-Thought

```python
def chain_of_thought(question: str) -> str:
    prompt = f"{question}\n\nLet's think step by step:"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
```

### Self-Consistency

```python
from collections import Counter
import re

def self_consistency(question: str, n_samples: int = 5) -> str:
    prompt = f"{question}\n\nLet's think step by step:"
    answers = []

    for _ in range(n_samples):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        # Extract final answer
        text = response.choices[0].message.content
        numbers = re.findall(r'\b(\d+)\b', text)
        if numbers:
            answers.append(numbers[-1])

    # Majority vote
    return Counter(answers).most_common(1)[0][0]
```

## Multi-Agent Patterns

### Message Passing

```python
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Message:
    sender: str
    receiver: str
    content: str
    timestamp: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.inbox: List[Message] = []

    def receive(self, msg: Message):
        self.inbox.append(msg)

    def process(self) -> Message:
        if not self.inbox:
            return None
        msg = self.inbox.pop(0)
        response = self._handle(msg)
        return Message(self.name, msg.sender, response)

    def _handle(self, msg: Message) -> str:
        return f"Received: {msg.content}"
```

### Orchestrator Pattern

```python
class Orchestrator:
    def __init__(self, agents: dict):
        self.agents = agents

    def route(self, task: str) -> str:
        # Decide which agent handles the task
        prompt = f"""Task: {task}
Available agents: {list(self.agents.keys())}
Which agent should handle this? Return just the name."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        agent_name = response.choices[0].message.content.strip()
        if agent_name in self.agents:
            return self.agents[agent_name].handle(task)
        return "No suitable agent found"
```

## RAG Patterns

### Basic RAG

```python
def basic_rag(query: str, documents: list) -> str:
    # Simple keyword matching (replace with embeddings)
    relevant = [d for d in documents if query.lower() in d.lower()][:3]

    context = "\n".join(relevant)
    prompt = f"""Context: {context}

Question: {query}

Answer based on the context:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

### Self-RAG Decision

```python
def should_retrieve(query: str, context: str = "") -> bool:
    prompt = f"""Query: {query}
Current context: {context}

Should I retrieve more information? (YES/NO)"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return "YES" in response.choices[0].message.content.upper()
```

## Verification Patterns

### Claim Decomposition

```python
def decompose_claims(text: str) -> list:
    prompt = f"""Decompose into atomic claims:

Text: {text}

Return one claim per line, numbered."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    claims = response.choices[0].message.content.split('\n')
    return [c.strip() for c in claims if c.strip()]
```

### Verification Check

```python
def verify_claim(claim: str) -> dict:
    # Generate verification questions
    q_prompt = f"Generate 2 questions to verify: {claim}"
    questions = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q_prompt}]
    ).choices[0].message.content

    # Answer independently
    answers = []
    for q in questions.split('\n'):
        if '?' in q:
            a = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": q}]
            ).choices[0].message.content
            answers.append(a)

    # Check consistency
    check = f"""Claim: {claim}
Evidence: {answers}
Is the claim verified? (YES/NO)"""

    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": check}]
    ).choices[0].message.content

    return {"claim": claim, "verified": "YES" in result.upper()}
```

## Utility Functions

### Rate Limiting

```python
import time
from functools import wraps

def rate_limit(calls_per_minute: int):
    min_interval = 60.0 / calls_per_minute
    last_call = [0.0]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_call[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            result = func(*args, **kwargs)
            last_call[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(calls_per_minute=60)
def call_api(prompt):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
```

### Token Counting

```python
import tiktoken

def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def truncate_to_tokens(text: str, max_tokens: int) -> str:
    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    tokens = encoding.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return encoding.decode(tokens[:max_tokens])
```

---

*Copy any snippet and adapt for your use case. See the notebooks for complete implementations.*
