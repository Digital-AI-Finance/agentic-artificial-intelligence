# Reading Guide: Domain Applications of Agentic AI

**Week 11 - Domain Applications**

## Primary Reading

### Devin: An Autonomous Software Engineer

- **Organization**: Cognition AI
- **Year**: 2024
- **Link**: https://www.cognition-labs.com/introducing-devin
- **Blog**: https://www.cognition.ai/blog/introducing-devin

## Paper Classification

- **Type**: Applied research (domain-specific agent system)
- **Impact**: First widely-publicized autonomous software engineer
- **Prerequisites**: Understanding of software development, agent architectures

## Why This Paper Matters

Devin represents the first generation of truly autonomous domain agents:

1. **End-to-End Capability**: Handles entire development workflows, not just code completion
2. **Long-Horizon Planning**: Maintains context over hours/days of work
3. **Multi-Tool Integration**: Uses shell, browser, editor seamlessly
4. **Self-Debugging**: Iterates on failures without human intervention

This sets the template for domain-specific agents across industries.

---

## Secondary Readings

### AlphaCodium: From Prompt Engineering to Flow Engineering for Code Generation

- **Authors**: Tal Ridnik, Dedy Kredo, Itamar Friedman
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2401.08500
- **Code**: https://github.com/Codium-ai/AlphaCodium

#### Focus Areas
- Test-driven development for code agents
- Flow engineering vs. prompt engineering
- Performance on competitive programming
- Iterative refinement with test feedback

### MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making

- **Authors**: Yubin Kim, Chanwoo Park, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2404.15488

#### Focus Areas
- Multi-agent collaboration for medical diagnosis
- Expert role assignment and consultation patterns
- Safety constraints in medical contexts
- Uncertainty handling for high-stakes decisions

### A Survey on Large Language Model based Autonomous Agents for Financial Applications

- **Authors**: Shuoling Li, et al.
- **Year**: 2024
- **arXiv**: https://arxiv.org/abs/2402.18485

#### Focus Areas
- Section 3: Agent architectures for finance
- Section 4: Tool integration (market data, trading)
- Section 5: Evaluation challenges and regulatory compliance

---

## Critical Reading Guide

### Before Reading

Answer these questions:

1. **Problem Context**: What makes domain-specific agents different?
   - Specialized tools and APIs
   - Domain-specific knowledge requirements
   - Regulatory and safety constraints
   - Different evaluation criteria

2. **Prior Work**: How were domain tasks automated before?
   - Rule-based systems (limited flexibility)
   - Supervised ML (narrow scope)
   - Human-in-the-loop tools (limited autonomy)

3. **Your Hypothesis**: What domain would benefit most from agentic AI?

### During Reading: Devin

#### System Architecture

**Key Components**:

| Component | Role | Implementation |
|-----------|------|----------------|
| Planner | Long-horizon task decomposition | Custom reasoning engine |
| Coder | Code generation and editing | LLM with code context |
| Shell Agent | Command execution | Sandboxed terminal |
| Browser Agent | Web research and documentation | Automated browsing |
| Debugger | Error analysis and fixing | Test-driven feedback loop |

**The Devin Workflow**:
```
1. Receive task specification
2. Plan implementation approach
3. Research documentation/APIs
4. Write initial code
5. Run tests
6. Debug failures (iterate)
7. Commit and document changes
```

- [ ] How does Devin maintain context over long tasks?
- [ ] What tools does Devin have access to?
- [ ] How does self-debugging work?

#### Capabilities and Limitations

**Demonstrated Capabilities**:
- Resolving real GitHub issues
- Building end-to-end applications
- Learning new technologies on the fly
- Debugging complex multi-file codebases

**Current Limitations**:
- Struggles with novel architectures
- Can get stuck in debugging loops
- Limited understanding of business requirements
- Requires clear specifications

- [ ] What types of tasks does Devin handle well?
- [ ] Where does it fail?
- [ ] How does it compare to human developers?

### During Reading: AlphaCodium

#### Flow Engineering Concept

**Key Insight**: Instead of optimizing prompts, optimize the entire problem-solving flow.

**AlphaCodium Flow**:
```
1. Problem reflection and clarification
2. Public test reasoning
3. Solution ideation (multiple approaches)
4. Code generation
5. Test on public tests
6. Test-based iteration
7. Final solution selection
```

**Comparison to Direct Prompting**:

| Approach | CodeContests Score |
|----------|-------------------|
| Direct prompting | 19% |
| AlphaCodium flow | 44% |

- [ ] What is "flow engineering"?
- [ ] How does test-driven iteration improve performance?
- [ ] Why generate multiple solution approaches?

### During Reading: MDAgents

#### Multi-Agent Medical Consultation

**Agent Roles**:

| Role | Responsibility | Output |
|------|----------------|--------|
| General Practitioner | Initial assessment | Preliminary diagnosis |
| Specialists | Domain expertise | Expert opinions |
| Medical Examiner | Final synthesis | Diagnostic conclusion |
| Critic | Quality control | Potential issues |

**Safety Mechanisms**:
- Explicit uncertainty quantification
- Citation of medical literature
- Deferral to human review triggers
- Logging for audit trails

- [ ] How are expert roles assigned?
- [ ] What triggers human escalation?
- [ ] How is uncertainty communicated?

### After Reading

Compare domain applications:

| Domain | Key Challenges | Required Tools | Safety Concerns |
|--------|----------------|----------------|-----------------|
| Software | Long context, debugging | IDE, shell, git | Security vulnerabilities |
| Finance | Real-time data, regulations | Market APIs, databases | Financial advice laws |
| Healthcare | Privacy, accuracy | EHR systems, literature | HIPAA, patient safety |
| Legal | Precedent search, reasoning | Case law databases | Unauthorized practice |
| Research | Citation accuracy, novelty | Paper databases, search | Plagiarism, fabrication |

---

## Discussion Questions (Seminar)

Prepare to discuss:

### Conceptual
1. What makes a domain suitable for agentic automation?
2. How should agents handle domain-specific regulations (HIPAA, SEC, etc.)?
3. When should domain agents defer to humans?

### Technical
1. What makes domain-specific tools different from general-purpose tools?
2. How do you build domain agents that stay within regulatory bounds?
3. What's the right architecture for long-horizon domain tasks?
4. How should domain agents handle ambiguity?

### Practical
1. How do you evaluate agents in high-stakes domains where mistakes are costly?
2. What's the business case for domain agents vs. augmentation tools?
3. How do you build user trust in domain agents?

### Research
1. What domains are underserved by current agent research?
2. How might agents learn domain expertise more efficiently?
3. What evaluation benchmarks are needed for domain applications?

---

## Key Takeaways to Remember

1. **Domain Agents Require**:
   - Specialized tools and APIs
   - Domain knowledge (often fine-tuned or retrieved)
   - Compliance with regulations
   - Domain-appropriate evaluation

2. **Flow > Prompt**: AlphaCodium shows that optimizing the entire workflow matters more than optimizing individual prompts.

3. **Safety is Non-Negotiable**: In high-stakes domains, explicit uncertainty and human escalation are essential.

4. **Long-Horizon is Hard**: Devin's biggest innovation is maintaining coherent plans over hours.

5. **Domain-Specific Evaluation**: General benchmarks don't capture domain requirements.

6. **The Autonomy Spectrum**:
   | Level | Example | Human Role |
   |-------|---------|------------|
   | Tool | GitHub Copilot | Human drives |
   | Assistant | ChatGPT | Human validates |
   | Agent | Devin | Human supervises |
   | Autonomous | Future | Human oversees |

---

## Supplementary Readings

| Paper | Domain | Notes |
|-------|--------|-------|
| CodeAct (Wang et al., 2024) | Code | Python execution agent |
| FinGPT (Yang et al., 2023) | Finance | Open-source financial LLM |
| ClinicalAgent (Tang et al., 2024) | Healthcare | Clinical decision support |
| LegalBench (Guha et al., 2023) | Legal | Legal reasoning benchmark |
| ChemCrow (Bran et al., 2024) | Chemistry | Chemical research agent |
| SciAgent (Ghafarollahi & Buehler, 2024) | Science | Scientific discovery agent |

---

## Domain Agent Design Patterns

### Pattern 1: Specialist Consultation

```python
class SpecialistConsultation:
    """Multi-agent pattern for domain decisions."""

    def __init__(self, specialists: dict[str, Agent]):
        self.specialists = specialists

    def consult(self, case: dict) -> dict:
        # Get opinions from relevant specialists
        opinions = {}
        for name, agent in self.specialists.items():
            if agent.is_relevant(case):
                opinions[name] = agent.analyze(case)

        # Synthesize opinions
        return self.synthesize(opinions)
```

### Pattern 2: Regulatory Guardrails

```python
class RegulatoryGuardrails:
    """Enforce domain regulations on agent actions."""

    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def check_action(self, action: Action) -> tuple[bool, str]:
        for rule in self.rules:
            if rule.violated_by(action):
                return False, rule.violation_message
        return True, "OK"

    def filter_outputs(self, output: str) -> str:
        for rule in self.rules:
            output = rule.redact(output)  # Remove prohibited content
        return output
```

### Pattern 3: Uncertainty Escalation

```python
class UncertaintyEscalation:
    """Escalate to humans when confidence is low."""

    def __init__(self, confidence_threshold: float = 0.8):
        self.threshold = confidence_threshold

    def decide(self, decision: Decision) -> Action:
        if decision.confidence < self.threshold:
            return EscalateToHuman(
                decision=decision,
                reason=f"Confidence {decision.confidence} below threshold"
            )
        return ExecuteDecision(decision)
```

---

## Implementation Considerations by Domain

### Code Agents
- Sandboxed execution environment
- Version control integration
- Test harness infrastructure
- Security scanning (SAST/DAST)
- CI/CD integration

### Financial Agents
- Real-time market data feeds
- Compliance checking pipelines
- Audit logging (immutable)
- Risk management limits
- Regulatory reporting

### Healthcare Agents
- PHI protection (encryption, access control)
- Evidence-based recommendation engine
- Uncertainty quantification
- Human review requirements
- EHR integration standards (HL7, FHIR)

### Legal Agents
- Jurisdiction-aware reasoning
- Citation verification
- Conflict of interest checking
- Client confidentiality
- Unauthorized practice prevention

---

## Preparation Checklist

Before class, ensure you:
- [ ] Read Devin introduction and watched demo videos
- [ ] Read AlphaCodium Sections 1-3
- [ ] Skimmed MDAgents abstract and introduction
- [ ] Identified one domain application you'd like to build
- [ ] Listed required tools and data sources for that domain
- [ ] Noted regulatory constraints for your chosen domain
- [ ] Prepared 2-3 questions for discussion

## Notes Template

```markdown
## Domain Applications Reading Notes

**Date**: [your date]

### Devin Summary
- Key capabilities: [list 3-4]
- How long-horizon works: [description]
- Limitations: [list 2-3]

### AlphaCodium Summary
- Flow engineering: [definition]
- Key improvement: [% on what benchmark]
- Main insight: [1 sentence]

### MDAgents Summary
- Agent roles: [list them]
- Safety mechanisms: [list 2-3]
- When to escalate: [criteria]

### Domain Comparison
| Domain | Key Challenge | Critical Tool | Safety Concern |
|--------|---------------|---------------|----------------|
| Code | | | |
| Finance | | | |
| Healthcare | | | |

### Domain Agent Design
For my chosen domain [X]:
- Required tools: [list]
- Regulatory constraints: [list]
- Key metrics: [list]
- Human escalation triggers: [list]

### Questions for Discussion
1. [Question 1]
2. [Question 2]

### Connection to Course
[How do domain agents build on general agent patterns?]
```

## Key Vocabulary

- **Domain agent**: Agent specialized for a specific industry/field
- **Flow engineering**: Optimizing the entire problem-solving workflow
- **Regulatory compliance**: Adhering to domain-specific laws and rules
- **Uncertainty quantification**: Expressing confidence in predictions
- **Human escalation**: Deferring decisions to human oversight
- **Long-horizon planning**: Maintaining coherent plans over extended timeframes
- **Domain tools**: Specialized APIs and systems for a specific field
- **Audit trail**: Record of agent decisions for accountability
- **Guardrails**: Constraints that prevent harmful agent actions

## Practical Exercise

Design a domain agent for your area of interest:

1. **Domain Selection**: What field will you focus on?
2. **Task Scope**: What tasks should the agent handle?
3. **Tool Requirements**: What APIs/systems are needed?
4. **Safety Constraints**: What regulations apply?
5. **Evaluation Criteria**: How will you measure success?
6. **Human Integration**: When should humans be involved?

| Component | Your Design |
|-----------|-------------|
| Domain | |
| Primary task | |
| Key tools | |
| Regulatory constraints | |
| Success metrics | |
| Escalation triggers | |
