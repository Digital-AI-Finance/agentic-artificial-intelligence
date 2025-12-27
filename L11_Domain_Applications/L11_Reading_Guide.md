# Week 11 Reading Guide: Domain Applications of Agentic AI

## Primary Reading

### Devin: An Autonomous Software Engineer
**Organization**: Cognition AI
**Year**: 2024
**Link**: https://www.cognition-labs.com/introducing-devin

#### Key Concepts
- End-to-end autonomous coding
- Long-horizon planning for software tasks
- Shell, browser, and editor tool use
- Self-debugging and testing

#### Critical Reading Questions
1. What enables Devin to handle long-horizon tasks that other agents fail at?
2. How does Devin's architecture differ from simpler code generation agents?
3. What are the limitations and failure modes reported?

---

## Secondary Readings

### AlphaCodium: From Prompt Engineering to Flow Engineering for Code Generation
**Authors**: Ridnik, T., Kredo, D., Friedman, I.
**Year**: 2024
**arXiv**: 2401.08500

#### Focus Areas
- Test-driven development for code agents
- Iterative refinement with feedback
- Performance on competitive programming

### MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making
**Authors**: Kim, Y., et al.
**Year**: 2024
**arXiv**: 2404.15488

#### Focus Areas
- Multi-agent collaboration for diagnosis
- Expert role assignment
- Safety constraints in medical context
- Uncertainty handling

### A Survey on Large Language Model based Autonomous Agents for Financial Applications
**Authors**: Li, S., et al.
**Year**: 2024
**arXiv**: 2402.18485

#### Focus Areas
- Section 3: Agent architectures for finance
- Section 4: Tool integration (market data, trading)
- Section 5: Evaluation and challenges

---

## Discussion Questions

### For Seminar
1. **Domain Constraints**: How should agents handle domain-specific regulations (HIPAA, SEC, etc.)?

2. **Tool Integration**: What makes domain-specific tools different from general-purpose tools?

3. **Evaluation Challenges**: How do you evaluate agents in high-stakes domains where mistakes are costly?

4. **Human-in-the-Loop**: When should domain agents defer to humans? How do you design these handoffs?

5. **Generalization vs. Specialization**: Should we build domain-specific agents or adapt general agents?

---

## Practical Exercises

### Before Class
1. Read Devin introduction and watch demo videos
2. Read AlphaCodium Sections 1-3
3. Skim MDAgents abstract and introduction

### After Class
1. Identify one domain application you'd like to build
2. List the required tools and data sources
3. Draft an architecture diagram

---

## Domain Application Overview

| Domain | Key Challenges | Required Tools | Safety Concerns |
|--------|----------------|----------------|-----------------|
| Code | Long context, debugging | IDE, shell, git | Security vulnerabilities |
| Finance | Real-time data, regulations | Market APIs, databases | Financial advice laws |
| Healthcare | Privacy, accuracy | EHR systems, literature | HIPAA, patient safety |
| Legal | Precedent search, reasoning | Case law databases | Unauthorized practice |
| Research | Citation accuracy, novelty | Paper databases, search | Plagiarism, fabrication |

---

## Related Papers

| Paper | Domain | Notes |
|-------|--------|-------|
| CodeAct (Wang et al., 2024) | Code | Python execution agent |
| FinGPT (Yang et al., 2023) | Finance | Open-source financial LLM |
| ClinicalAgent (Tang et al., 2024) | Healthcare | Clinical decision support |
| LegalBench (Guha et al., 2023) | Legal | Legal reasoning benchmark |

---

## Implementation Considerations

### Code Agents
- Sandboxed execution environment
- Version control integration
- Test harness infrastructure
- Security scanning

### Financial Agents
- Real-time data feeds
- Compliance checking
- Audit logging
- Risk management

### Healthcare Agents
- PHI protection
- Evidence-based recommendations
- Uncertainty quantification
- Human review requirements

---

## Key Takeaways
1. Domain agents require specialized tools and knowledge
2. Regulatory compliance is critical in sensitive domains
3. Long-horizon planning is a key differentiator
4. Human oversight is essential for high-stakes decisions
5. Evaluation must reflect real-world deployment conditions
