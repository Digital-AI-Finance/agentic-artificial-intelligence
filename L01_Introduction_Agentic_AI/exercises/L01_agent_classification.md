# Exercise L01: Agent Classification

**Week 1 - Introduction to Agentic AI**

## Overview

In this exercise, you will analyze and classify different AI systems according to the agent taxonomy presented in class.

## Learning Objectives

- **Primary (Analyze)**: Classify systems according to agent properties
- **Secondary (Evaluate)**: Assess strengths and limitations of different architectures
- **Tertiary (Apply)**: Apply formal definitions to real-world systems

## Problem Statement

Given the formal definition of an agent (Russell & Norvig):
- An **agent** perceives its environment through sensors and acts upon it through actuators
- Agent function: f: P* -> A (percept history to action)

And the key agent properties (Wooldridge & Jennings):
- **Autonomy**: Operates without direct intervention
- **Reactivity**: Responds to environment changes
- **Pro-activeness**: Takes initiative toward goals
- **Social ability**: Interacts with other agents

### Task 1: System Classification (40 points)

Classify each of the following systems. For each system, determine:
1. Is it an agent? (Yes/No/Partially)
2. What are its sensors (inputs)?
3. What are its actuators (outputs)?
4. Which agent properties does it exhibit?

**Systems to classify:**

| System | Description |
|--------|-------------|
| A | ChatGPT (standard chat interface) |
| B | GitHub Copilot |
| C | Roomba vacuum cleaner |
| D | Stock trading algorithm |
| E | Claude with Computer Use |
| F | Google Search |

**Format your answer as:**
```
System A: ChatGPT
- Is Agent: [Yes/No/Partially]
- Sensors: [list inputs]
- Actuators: [list outputs]
- Autonomy: [High/Medium/Low/None] - [justification]
- Reactivity: [High/Medium/Low/None] - [justification]
- Pro-activeness: [High/Medium/Low/None] - [justification]
- Social ability: [High/Medium/Low/None] - [justification]
```

### Task 2: Architecture Analysis (35 points)

For each classified agent (from Task 1), identify its architecture type:

| Architecture | Description |
|--------------|-------------|
| Reactive | Direct stimulus-response, no internal state |
| Deliberative | Plan then execute, maintains world model |
| Hybrid | Combines reactive and deliberative layers |

Additionally, identify:
- **Memory type**: None / Short-term / Long-term / Both
- **Tool access**: None / Limited / Extensive

### Task 3: Design Proposal (25 points)

Design an agent for the following scenario:

**Scenario**: You need to build an agent that helps researchers find relevant papers, summarize them, and maintain a knowledge base of research topics.

Your design should include:
1. **Agent type** (reactive/deliberative/hybrid)
2. **Core components** (LLM, memory, tools, planning)
3. **Sensors** (what inputs does it receive?)
4. **Actuators** (what outputs/actions can it take?)
5. **Tool inventory** (list 3-5 tools with descriptions)
6. **Memory design** (what to remember, how to store)
7. **Simple architecture diagram** (ASCII or description)

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| Task 1 Response | Markdown | Classification for all 6 systems |
| Task 2 Response | Markdown | Architecture analysis table |
| Task 3 Design | Markdown + Diagram | Complete design document |

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Task 1: Classification | 40 | Correct classification with justification |
| Task 2: Architecture | 35 | Accurate architecture identification |
| Task 3: Design | 25 | Complete, coherent design proposal |

### Detailed Rubric

**Task 1 (40 points)**
- 5 points per system (6 systems + 10 bonus)
- Full credit: Correct classification with clear justification
- Partial credit: Correct classification, weak justification
- No credit: Incorrect classification

**Task 2 (35 points)**
- 5 points per architecture analysis
- Full credit: Correct architecture with memory/tool assessment
- Partial credit: Correct architecture only

**Task 3 (25 points)**
- Components defined (5 points)
- Tools specified (5 points)
- Memory design (5 points)
- Architecture coherence (5 points)
- Diagram/visualization (5 points)

## Resources

- Russell & Norvig (2021). "Artificial Intelligence: A Modern Approach" - Chapter 2
- Wooldridge & Jennings (1995). "Intelligent Agents: Theory and Practice"
- Yao et al. (2023). "ReAct" - arXiv:2210.03629
- Wang et al. (2024). "LLM Agent Survey" - arXiv:2308.11432

## Submission

- **Format**: Single Markdown file (.md)
- **Filename**: `L01_exercise_[your_name].md`
- **Due**: End of Week 1

## Hints

- Consider that some systems may be "borderline" agents
- Think about what happens between user interactions
- Consider whether the system maintains state
- Remember: an agent needs autonomy, not just automation

## Sample Answer (Task 1, System A only)

```
System A: ChatGPT (standard chat interface)
- Is Agent: Partially
- Sensors: Text input from user, conversation history (within session)
- Actuators: Text output to user
- Autonomy: Low - Requires user prompt for each response
- Reactivity: High - Responds immediately to user input
- Pro-activeness: None - Does not initiate actions toward goals
- Social ability: Low - Single-turn interaction, no multi-agent communication

Justification: ChatGPT in its basic form is closer to a "stateless oracle"
than a true agent. It lacks autonomy (waits for prompts), has no persistent
memory, and cannot take actions in the world. However, with plugins or
function calling enabled, it moves closer to agent status.
```
