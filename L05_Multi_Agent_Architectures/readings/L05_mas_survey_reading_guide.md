# Reading Guide: Multi-Agent Systems with LLMs

**Week 5 - Multi-Agent Architectures**

## Primary Reading

- **Title**: A Systematic Survey on Large Language Model-based Multi-Agent Collaboration
- **Authors**: Tran et al.
- **Year**: 2025
- **arXiv**: https://arxiv.org/abs/2501.06322

## Secondary Readings

### AutoGen Paper
- **Title**: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
- **Authors**: Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al.
- **Year**: 2023
- **arXiv**: https://arxiv.org/abs/2308.08155
- **Code**: https://github.com/microsoft/autogen

### MetaGPT Paper
- **Title**: MetaGPT: Meta Programming for Multi-Agent Collaborative Framework
- **Authors**: Sirui Hong, Xiawu Zheng, Jonathan Chen, et al.
- **Year**: 2023
- **arXiv**: https://arxiv.org/abs/2308.00352
- **Code**: https://github.com/geekan/MetaGPT

## Paper Classification

- **Type**: Survey + Applied research
- **Impact**: Foundational for multi-agent LLM systems
- **Prerequisites**: Understanding of single-agent architectures, ReAct

## Why These Papers Matter

Single LLM agents have fundamental limitations:
- Knowledge bounded by one model
- Single perspective on complex problems
- No debate or verification mechanism
- Scalability constraints

Multi-agent systems address these by enabling collaboration, specialization, and emergent collective intelligence. These papers establish the foundation for building agent teams.

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: What challenges might arise when multiple LLMs work together?
   - Coordination overhead
   - Communication ambiguity
   - Conflicting outputs
   - Token cost explosion

2. **Prior Work**: How do human teams coordinate effectively?
   - Clear role definitions
   - Structured communication protocols
   - Feedback mechanisms
   - Conflict resolution

3. **Your Hypothesis**: What makes multi-agent collaboration effective?

### During Reading: Survey Paper

#### Key Taxonomies to Understand

**Agent Architectures**:
| Architecture | Description | Example |
|--------------|-------------|---------|
| Centralized | Single orchestrator controls all agents | Manager + workers |
| Hierarchical | Multi-level management structure | CEO > managers > workers |
| Decentralized | Peer-to-peer communication | Debate between equals |
| Hybrid | Combines multiple patterns | LangGraph StateGraph |

**Communication Patterns**:
| Pattern | Description | When to Use |
|---------|-------------|-------------|
| Direct | Agent-to-agent messages | Small teams |
| Broadcast | One-to-all messages | Announcements |
| Blackboard | Shared memory/state | Complex coordination |
| Protocol | Structured turns | Debates, reviews |

**Role Types**:
| Role | Responsibility | Example Prompt |
|------|----------------|----------------|
| Orchestrator | Coordinates workflow | "Decide which agent to invoke" |
| Specialist | Domain expertise | "You are a security expert" |
| Executor | Performs actions | "Execute this code" |
| Critic | Reviews outputs | "Find flaws in this solution" |

#### Reading Checkpoints

- [ ] What are the main categories of multi-agent architectures? (Section 3)
- [ ] How do agents typically communicate? (Section 4)
- [ ] What are the key applications of multi-agent systems? (Section 5)
- [ ] What evaluation methods are used? (Section 6)
- [ ] What open challenges are identified? (Section 7)

### During Reading: AutoGen

#### Key Concepts

**Conversable Agents**:
AutoGen's core abstraction is agents that can converse:
```python
class ConversableAgent:
    def __init__(self, name, system_message, llm_config):
        ...

    def initiate_chat(self, recipient, message):
        # Start conversation with another agent
        ...

    def generate_reply(self, messages):
        # Generate response using LLM
        ...
```

**Two-Agent Patterns**:
| Pattern | Agents | Use Case |
|---------|--------|----------|
| Assistant + User | AI + Human proxy | Code generation |
| Assistant + Critic | Generator + Reviewer | Quality control |
| Teacher + Student | Expert + Learner | Explanation |

#### Reading Checkpoints

- [ ] How are agents defined in AutoGen?
- [ ] What is the conversation loop?
- [ ] How does code execution work?
- [ ] What termination conditions are supported?

### During Reading: MetaGPT

#### Key Concepts

**Standard Operating Procedures (SOPs)**:
MetaGPT structures collaboration like a software company:
```
Product Manager -> Architect -> Engineer -> QA
       |              |           |        |
    PRD doc      Design doc   Code      Tests
```

**Role Definitions**:
Each role has specific responsibilities and outputs.

#### Reading Checkpoints

- [ ] How does MetaGPT model software development?
- [ ] What artifacts does each role produce?
- [ ] How are dependencies between roles handled?
- [ ] What makes this more structured than AutoGen?

### After Reading

Reflect on these questions:

1. **Trade-offs**
   | Aspect | Centralized | Decentralized |
   |--------|-------------|---------------|
   | Coordination | Easy | Hard |
   | Scalability | Limited | Better |
   | Single point of failure | Yes | No |
   | Debugging | Easy | Hard |

2. **When to Use Multi-Agent**
   - Task requires multiple perspectives
   - Quality control is critical
   - Task naturally decomposes into roles
   - Scalability is needed

3. **When NOT to Use Multi-Agent**
   - Simple tasks
   - Low latency required
   - Token cost is critical
   - Single expert suffices

---

## Discussion Questions (Seminar)

Prepare to discuss:

1. **Conceptual**
   - What problems can multi-agent systems solve that single agents cannot?
   - When does adding more agents help vs hurt?

2. **Technical**
   - How do you design effective agent communication protocols?
   - What determines optimal team size?

3. **Practical**
   - How would you debug a multi-agent system?
   - What's the token cost overhead of coordination?

4. **Critical**
   - Can emergent behaviors arise from simple agent rules?
   - How do you prevent agent "groupthink"?

---

## Key Takeaways to Remember

1. **Architecture Patterns**:
   - Centralized: Simple but bottlenecked
   - Hierarchical: Scalable with clear authority
   - Decentralized: Resilient but complex

2. **Communication Matters**: Protocol design determines success

3. **Role Specialization**: Focused agents outperform generalists

4. **Evaluation is Hard**: No standard benchmarks exist

5. **Cost Consideration**: Every agent message costs tokens

---

## Supplementary Readings

| Paper | Relationship |
|-------|--------------|
| CAMEL (Li et al., 2023) | Role-playing communication framework |
| ChatDev (Qian et al., 2024) | End-to-end software development |
| Generative Agents (Park et al., 2023) | Simulated social behavior |
| AgentVerse (Chen et al., 2023) | Multi-agent simulation platform |

---

## Framework Comparison

| Framework | Key Feature | Best For |
|-----------|-------------|----------|
| AutoGen | Conversable agents | General multi-agent |
| LangGraph | Graph-based workflows | Complex state machines |
| CrewAI | Role-based teams | Structured tasks |
| MetaGPT | SOPs and artifacts | Software development |

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read survey paper Sections 1-4
- [ ] Skimmed AutoGen paper (focus on Section 2-3)
- [ ] Understood the architecture taxonomy
- [ ] Compared centralized vs decentralized patterns
- [ ] Noted 2-3 questions for discussion
- [ ] Connected to single-agent patterns from Week 4

## Notes Template

```markdown
## Multi-Agent Reading Notes

**Date**: [your date]

### Survey Summary
- Key architectures: [list 3-4]
- Communication patterns: [list main patterns]
- Open challenges: [list 2-3]

### AutoGen Summary
- Core abstraction: [1 sentence]
- Key patterns: [list 2-3]
- Strengths: [list 2]
- Weaknesses: [list 2]

### MetaGPT Summary
- Core idea: [1 sentence]
- Role structure: [describe the flow]
- Key innovation: [what's novel?]

### Comparison
| Aspect | AutoGen | MetaGPT |
|--------|---------|---------|
| Structure | | |
| Flexibility | | |
| Complexity | | |

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Course
[How do multi-agent systems extend single-agent patterns?]
```

## Implementation Exercise

Design a multi-agent system for code review:

1. **Define roles**: What agents do you need?
2. **Design communication**: How do agents interact?
3. **Specify outputs**: What does each agent produce?
4. **Handle conflicts**: What if agents disagree?

```python
# Sketch your design
class CodeReviewTeam:
    def __init__(self):
        self.agents = {
            "analyzer": ...,
            "security": ...,
            "reviewer": ...,
        }

    def review(self, code: str) -> dict:
        # Define the coordination logic
        pass
```
