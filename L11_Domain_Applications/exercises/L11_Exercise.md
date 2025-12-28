# Week 11 Exercise: Building a Domain-Specific Agent

## Objective
Design and implement a complete agent for a specific domain, demonstrating practical application of agentic AI concepts.

## Learning Outcomes
- Apply agent design principles to real-world problems
- Implement domain-specific tool integration
- Handle domain constraints and regulations
- Evaluate agent performance in realistic scenarios

## Task Description

Choose ONE domain for your implementation:

### Option A: Financial Analysis Agent
Build an agent that:
1. Retrieves financial data (stock prices, filings, news)
2. Performs quantitative analysis (ratios, trends, comparisons)
3. Generates investment summaries with citations
4. Handles compliance-aware language

### Option B: Code Generation Agent
Build an agent that:
1. Understands natural language specifications
2. Generates code with test cases
3. Iteratively refines based on test failures
4. Documents code with docstrings and comments

### Option C: Research Assistant Agent
Build an agent that:
1. Searches academic databases (arXiv, Semantic Scholar)
2. Summarizes and compares papers
3. Identifies research gaps
4. Generates literature review sections

### Option D: Customer Support Agent
Build an agent that:
1. Classifies customer inquiries
2. Retrieves relevant documentation
3. Generates helpful responses
4. Escalates complex issues appropriately

## Implementation Requirements

### Part 1: Domain Analysis (20%)
Document your domain:
1. Key tasks and workflows
2. Required data sources and tools
3. Domain constraints (regulations, best practices)
4. Success criteria and failure modes

### Part 2: Tool Implementation (30%)
Build domain-specific tools:
1. At least 3 functional tools
2. Proper error handling
3. Rate limiting and caching
4. Logging and monitoring

### Part 3: Agent Architecture (30%)
Design and implement:
1. Agent workflow (ReAct, plan-execute, or custom)
2. Memory management
3. Context handling
4. Output formatting

### Part 4: Evaluation (20%)
Demonstrate agent capability:
1. 10 test scenarios
2. Success/failure analysis
3. Performance metrics
4. Comparison with baseline (manual or simple LLM)

## Deliverables
1. `domain_agent.py` - Main agent implementation
2. `tools/` - Domain-specific tools
3. `test_scenarios.json` - Test cases
4. `demo.ipynb` - Interactive demonstration
5. `design_doc.md` - Architecture documentation

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Domain Understanding | 15 | Appropriate tool/workflow design |
| Tool Quality | 25 | Robust, well-tested tools |
| Agent Architecture | 25 | Sound design, proper integration |
| Evaluation | 20 | Meaningful testing and analysis |
| Documentation | 15 | Clear architecture and usage docs |

## Resources
- Devin Technical Report (Cognition AI)
- AlphaCodium (Ridnik et al., 2024)
- FinAgent Survey (Li et al., 2024)
- MDAgents (Kim et al., 2024)

## Time Estimate
- Minimum: 6 hours
- Expected: 10 hours
- Maximum: 15 hours
