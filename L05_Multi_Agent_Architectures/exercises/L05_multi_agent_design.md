# Exercise L05: Design a Multi-Agent System

**Week 5 - Multi-Agent Architectures**

## Overview
Design and implement a multi-agent system for a complex collaborative task.

## Task 1: System Design (35 points)

Design a multi-agent system for one of these scenarios:

**Option A: Research Assistant Team**
- Literature Searcher: Finds relevant papers
- Summarizer: Creates paper summaries
- Synthesizer: Combines findings
- Critic: Identifies gaps and limitations

**Option B: Code Review Pipeline**
- Analyzer: Identifies code patterns
- Security Auditor: Checks vulnerabilities
- Performance Reviewer: Finds bottlenecks
- Documentation Checker: Verifies docs

**Deliverables:**
1. Architecture diagram showing agent topology
2. Role descriptions for each agent
3. Message format specification
4. Workflow sequence diagram

## Task 2: Implementation (40 points)

Implement your designed system:

```python
class MultiAgentSystem:
    def __init__(self):
        self.agents = {}
        self.router = MessageRouter()

    def add_agent(self, agent: Agent):
        """Register an agent with the system."""
        pass

    def run_task(self, task: str) -> dict:
        """Execute a collaborative task."""
        pass

    def get_results(self) -> list:
        """Return all generated artifacts."""
        pass
```

**Requirements:**
- Minimum 3 specialized agents
- Implement message passing between agents
- Track workflow state and artifacts
- Handle at least one error case

## Task 3: Analysis (25 points)

Write a comparison of coordination approaches:

1. **Centralized vs. Decentralized**
   - When is each approach better?
   - What are the failure modes?

2. **Synchronous vs. Asynchronous**
   - Trade-offs for each pattern
   - Impact on system complexity

3. **Your Design Decisions**
   - Why did you choose your topology?
   - What would you change for scale?

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| System Design | 35 | Clear architecture, well-defined roles |
| Implementation | 40 | Working code, proper message passing |
| Analysis | 25 | Thoughtful comparison, justified choices |

## Submission

1. Design document (diagrams + specifications)
2. Jupyter notebook with implementation
3. Written analysis (400-500 words)

## Bonus Challenge (+15 points)

Implement one of:
- Dynamic agent spawning based on task complexity
- Conflict resolution when agents disagree
- Performance monitoring and bottleneck detection
