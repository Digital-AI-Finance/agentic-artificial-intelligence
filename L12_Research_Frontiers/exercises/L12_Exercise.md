# Exercise L12: Research Proposal for Agentic AI

**Week 12 - Research Frontiers**

## Overview

Write a research proposal identifying an open problem in agentic AI and proposing a novel approach to address it. This exercise synthesizes the entire course into a concrete research contribution.

## Learning Objectives

- **Primary (Create)**: Design a research proposal with novel contributions
- **Secondary (Evaluate)**: Assess feasibility and impact of research directions
- **Tertiary (Synthesize)**: Integrate concepts from the entire course

## Prerequisites

- Completion of course weeks 1-11
- Familiarity with academic writing
- Understanding of research methodology
- Access to academic literature (arXiv, Semantic Scholar)

## Problem Statement

The field of agentic AI is rapidly evolving, with many open problems remaining unsolved. This exercise develops your ability to:
- Identify meaningful research gaps
- Position work within existing literature
- Design rigorous experiments
- Articulate contributions clearly

This is preparation for thesis research, conference submissions, or industry R&D proposals.

---

## Research Problem Categories

Choose ONE category for your proposal:

### Category A: Agent Capabilities

**Long-Horizon Planning**
- Current agents struggle beyond 10-20 step plans
- How can we improve planning under uncertainty?
- What representations enable better lookahead?

**World Models for Agents**
- How do agents learn accurate environment dynamics?
- What enables efficient mental simulation?
- How to transfer world models across domains?

**Tool Learning and Creation**
- How can agents learn to use new tools autonomously?
- Can agents create their own tools?
- What enables efficient tool selection?

### Category B: Multi-Agent Systems

**Coordination and Communication**
- How do agents develop shared protocols?
- What enables emergent specialization?
- How to scale multi-agent systems?

**Emergent Behaviors**
- Can we predict emergent behaviors?
- How to encourage beneficial emergence?
- What architectures produce stable equilibria?

**Human-Agent Collaboration**
- How to calibrate human trust in agents?
- What handoff mechanisms work best?
- How to explain agent decisions to humans?

### Category C: Safety and Alignment

**Scalable Oversight**
- How to supervise agents we can't fully understand?
- What verification methods scale with capability?
- How to ensure corrigibility (agent remains controllable)?

**Goal Stability**
- How to prevent goal drift during execution?
- What makes goals robust to distribution shift?
- How to detect and correct misalignment?

**Robustness and Security**
- How to defend against adversarial inputs?
- What makes agents robust to failures?
- How to prevent prompt injection?

### Category D: Evaluation and Infrastructure

**Better Benchmarks**
- What metrics predict real-world performance?
- How to evaluate open-ended capabilities?
- What environments capture realistic challenges?

**Memory and Knowledge**
- How to efficiently manage long-term memory?
- What enables knowledge consolidation?
- How to prevent catastrophic forgetting?

---

## Part 1: Problem Identification (25 points)

### 1a: Problem Statement (10 points)

Write a clear, specific problem statement:

```markdown
## Problem Statement

### The Problem
[One paragraph describing the specific problem you will address]

### Why It Matters
[One paragraph on the importance and impact]

### Current State
[One paragraph on what exists today and why it's insufficient]

### The Gap
[One paragraph on the specific gap your work will fill]
```

**Example Problem Statement:**

```markdown
## Problem Statement

### The Problem
Current language agents lack the ability to plan effectively over long horizons
(50+ steps) in domains with delayed feedback. While agents like ReAct and
Reflexion can handle short-term task completion, they fail when rewards are
sparse and error correction requires significant backtracking.

### Why It Matters
Real-world applications like software development, scientific research, and
strategic planning require sustained coherent behavior over extended time
periods. An agent that cannot plan beyond immediate next steps cannot tackle
these high-value problems.

### Current State
Existing approaches use either flat planning (ReAct, which struggles with
long horizons) or hierarchical planning (Plan-and-Solve, which suffers from
poor subgoal decomposition). Tree search methods (LATS) improve but are
computationally expensive and don't scale.

### The Gap
We lack a planning framework that combines: (1) efficient subgoal
decomposition, (2) robust error recovery, and (3) computational tractability
for horizons of 50+ steps. This proposal addresses this gap.
```

### 1b: Literature Review (15 points)

Review at least 10 relevant papers with structured analysis:

```markdown
## Literature Review

### Core Papers (5+)

| Paper | Year | Key Contribution | Limitation | How We Extend |
|-------|------|------------------|------------|---------------|
| ReAct | 2023 | Reasoning + acting | Short horizon | [Your extension] |
| Reflexion | 2023 | Self-reflection | Episodic only | [Your extension] |
| ... | ... | ... | ... | ... |

### Related Work (5+)

| Paper | Year | Relevance | Key Insight |
|-------|------|-----------|-------------|
| LATS | 2024 | Tree search | Monte Carlo for agents |
| ... | ... | ... | ... |

### Research Gaps

1. **Gap 1**: [Description] - addressed by [your contribution]
2. **Gap 2**: [Description] - partially addressed by [your contribution]
3. **Gap 3**: [Description] - future work

### Positioning

[Diagram or description showing where your work fits in the landscape]
```

**Literature Search Strategy:**

```python
# Keywords to search on arXiv, Semantic Scholar, Google Scholar
SEARCH_QUERIES = [
    # Primary topic
    "language agent planning",
    "LLM long horizon reasoning",

    # Related approaches
    "hierarchical reinforcement learning",
    "goal-conditioned planning",
    "subgoal discovery",

    # Evaluation
    "agent benchmark evaluation",

    # Safety considerations
    "safe autonomous agents",
]

# Databases to use
DATABASES = [
    "arXiv (cs.CL, cs.AI, cs.LG)",
    "Semantic Scholar",
    "Google Scholar",
    "ACL Anthology",
    "NeurIPS/ICML proceedings",
]

# Time range
TIME_RANGE = "2022-2025"  # Focus on recent work
```

---

## Part 2: Proposed Approach (30 points)

### 2a: High-Level Methodology (10 points)

Describe your approach at a conceptual level:

```markdown
## Proposed Approach

### Overview
[2-3 paragraphs describing the core idea]

### Key Innovations

1. **Innovation 1**: [Name]
   - What: [Description]
   - Why: [Motivation]
   - How: [Brief mechanism]

2. **Innovation 2**: [Name]
   - What: [Description]
   - Why: [Motivation]
   - How: [Brief mechanism]

3. **Innovation 3**: [Name] (if applicable)
   - ...

### Comparison to Prior Work

| Aspect | Prior Work | Our Approach | Advantage |
|--------|------------|--------------|-----------|
| [Aspect 1] | [How they do it] | [How we do it] | [Why better] |
| [Aspect 2] | ... | ... | ... |
```

### 2b: Technical Details (15 points)

Provide algorithmic or architectural details:

```markdown
## Technical Approach

### Architecture

[Diagram or detailed description]

### Algorithm

```
Algorithm: [Name]
Input: Task T, Environment E, LLM M
Output: Solution S

1. Initialize state s_0
2. Decompose T into subgoals G = {g_1, ..., g_n} using M
3. For each subgoal g_i:
   a. Plan actions A_i = Plan(g_i, s, M)
   b. Execute actions, observe outcomes
   c. If failure:
      - Analyze failure mode
      - Revise subgoal or backtrack
   d. Update state s
4. Return solution S
```

### Key Components

#### Component 1: [Name]

```python
class SubgoalDecomposer:
    """Decomposes high-level tasks into executable subgoals."""

    def __init__(self, llm: LLM, max_depth: int = 3):
        self.llm = llm
        self.max_depth = max_depth

    def decompose(self, task: str, context: str) -> list[Subgoal]:
        """Generate hierarchical subgoal tree."""
        prompt = f"""
        Task: {task}
        Context: {context}

        Decompose into 3-5 subgoals that:
        1. Are independently verifiable
        2. Have clear dependencies
        3. Can be completed in 5-10 steps each

        Format: JSON list of subgoals with dependencies
        """

        response = self.llm.complete(prompt)
        subgoals = parse_subgoals(response)

        # Recursively decompose if needed
        for sg in subgoals:
            if sg.complexity > self.complexity_threshold:
                sg.children = self.decompose(sg.description, context)

        return subgoals
```

#### Component 2: [Name]

[Similar detail for other key components]

### Theoretical Justification (if applicable)

[Mathematical formulation, proofs, or theoretical grounding]
```

### 2c: Implementation Plan (5 points)

```markdown
## Implementation Plan

### Phase 1: Core Framework (2-3 weeks)
- [ ] Implement base agent class
- [ ] Build subgoal decomposer
- [ ] Create evaluation harness

### Phase 2: Algorithm Development (3-4 weeks)
- [ ] Implement main algorithm
- [ ] Add error recovery mechanisms
- [ ] Integrate with LLM backends

### Phase 3: Evaluation (2-3 weeks)
- [ ] Run baseline experiments
- [ ] Ablation studies
- [ ] Analysis and iteration

### Technical Requirements
- Python 3.10+
- OpenAI/Anthropic API access
- GPU for local models (optional)
- Benchmark environments (specify which)

### Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | ... | ... | ... |
```

---

## Part 3: Experimental Design (25 points)

### 3a: Research Questions and Hypotheses (10 points)

```markdown
## Research Questions

### Primary Research Question
RQ1: [Your main research question]

**Hypothesis**: [Testable hypothesis]
**Metric**: [How you'll measure]
**Expected Result**: [What you predict]

### Secondary Research Questions
RQ2: [Second question]
- Hypothesis: [...]
- Metric: [...]

RQ3: [Third question]
- Hypothesis: [...]
- Metric: [...]

### Exploratory Questions (Optional)
- [Questions without specific hypotheses for discovery]
```

**Example:**

```markdown
### Primary Research Question
RQ1: Does hierarchical subgoal decomposition improve success rates on
long-horizon tasks (50+ steps) compared to flat planning?

**Hypothesis**: Hierarchical decomposition will improve success rate by >20%
on tasks requiring 50+ steps compared to ReAct baseline.

**Metric**: Task completion rate on ALFWorld and WebArena benchmarks for
tasks classified as "long-horizon" (ground truth >50 steps).

**Expected Result**: 45% success (ours) vs 25% success (ReAct) on
long-horizon subset.
```

### 3b: Experimental Setup (10 points)

```markdown
## Experimental Design

### Benchmarks and Datasets

| Benchmark | Domain | Why Chosen | Subset Used |
|-----------|--------|------------|-------------|
| [Bench 1] | [Domain] | [Rationale] | [Which tasks] |
| [Bench 2] | ... | ... | ... |

### Baselines

| Baseline | Description | Why Included |
|----------|-------------|--------------|
| [Base 1] | [Description] | [Reason] |
| [Base 2] | ... | ... |

### Evaluation Metrics

| Metric | Formula | What It Measures |
|--------|---------|------------------|
| Success Rate | correct/total | Task completion |
| Efficiency | steps/optimal | Path quality |
| [Custom] | [Formula] | [Description] |

### Experimental Protocol

1. **Training/Setup**: [If any training required]
2. **Evaluation runs**: [Number of runs, seeds]
3. **Statistical tests**: [t-test, bootstrap CI, etc.]
4. **Ablations**: [Which components to ablate]
```

### 3c: Expected Results and Analysis (5 points)

```markdown
## Expected Results

### Main Results Table

| Method | Success Rate | Efficiency | Cost |
|--------|--------------|------------|------|
| ReAct (baseline) | ~25% | 1.8x | $X |
| Reflexion | ~35% | 1.5x | $Y |
| **Ours** | **~45%** | **1.2x** | $Z |

### Ablation Studies

| Ablation | Expected Impact | Insight |
|----------|-----------------|---------|
| Remove subgoal decomposition | -15% success | Core contribution |
| Remove error recovery | -10% success | Important for robustness |
| ... | ... | ... |

### Analysis Plan
- What patterns to look for in results
- How to interpret unexpected outcomes
- Failure case analysis methodology
```

---

## Part 4: Impact and Contribution (20 points)

### 4a: Contributions (10 points)

```markdown
## Contributions

### Technical Contributions
1. **[Contribution 1]**: [Description of novel technique/algorithm]
2. **[Contribution 2]**: [Description of novel insight/finding]
3. **[Contribution 3]**: [Description of new benchmark/dataset/tool]

### Conceptual Contributions
- [New way of thinking about the problem]
- [Connection to other fields]

### Practical Contributions
- [Usable artifact (code, benchmark, dataset)]
- [Guidelines for practitioners]
```

### 4b: Broader Impact (5 points)

```markdown
## Broader Impact

### Positive Impacts
- [How this helps society/science/industry]
- [Who benefits from this work]

### Potential Risks
- [How this could be misused]
- [What safeguards are needed]

### Ethical Considerations
- [IRB considerations if human subjects]
- [Dual-use concerns]
- [Environmental impact of compute]
```

### 4c: Limitations and Future Work (5 points)

```markdown
## Limitations

### Scope Limitations
- [What this work does NOT address]
- [Assumptions that may not hold]

### Technical Limitations
- [Known weaknesses of approach]
- [Scalability concerns]

### Evaluation Limitations
- [Benchmark limitations]
- [Generalization concerns]

## Future Work

### Immediate Extensions
- [Short-term follow-ups]

### Longer-Term Directions
- [Where this leads in 2-3 years]

### Open Questions
- [What remains unknown after this work]
```

---

## Proposal Format Template

```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{graphicx}

\title{[Your Proposal Title]}
\author{[Your Name]}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
[200-word abstract summarizing problem, approach, and expected contribution]
\end{abstract}

\section{Introduction}
[1 page: Problem statement, motivation, thesis statement]

\section{Related Work}
[1-1.5 pages: Literature review, positioning]

\section{Proposed Approach}
[1.5-2 pages: Methodology, technical details]

\section{Experimental Design}
[1 page: Research questions, setup, metrics]

\section{Expected Contributions}
[0.5 page: What this work contributes]

\section{Timeline}
[0.5 page: Project plan]

\bibliography{references}
\end{document}
```

---

## Deliverables

| Deliverable | Format | Requirements |
|-------------|--------|--------------|
| proposal.pdf | LaTeX PDF | 6-8 pages, 11pt font |
| literature_review.md | Markdown | 10+ annotated papers |
| slides.pdf | Beamer/PPT | 10-12 slides |
| prototype.py (optional) | Python | Proof-of-concept |
| references.bib | BibTeX | All citations |

---

## Evaluation Rubric (100 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Problem Selection | 20 | Important, tractable, novel angle |
| Literature Review | 20 | Comprehensive, well-positioned |
| Technical Approach | 25 | Sound, innovative methodology |
| Experimental Design | 20 | Rigorous, appropriate evaluation |
| Presentation | 15 | Clear writing, good structure |

### Detailed Rubric

**Problem Selection (20 points)**
- 10 points: Problem is significant and well-motivated
- 5 points: Clear gap in existing literature
- 5 points: Scope is appropriate (not too broad or narrow)

**Literature Review (20 points)**
- 10 points: Comprehensive coverage of relevant work
- 5 points: Critical analysis (not just summaries)
- 5 points: Clear positioning of proposed work

**Technical Approach (25 points)**
- 10 points: Approach is technically sound
- 10 points: Novel elements are clearly identified
- 5 points: Implementation is feasible

**Experimental Design (20 points)**
- 10 points: Research questions are clear and testable
- 5 points: Baselines are appropriate
- 5 points: Metrics are meaningful

**Presentation (15 points)**
- 10 points: Writing is clear and well-organized
- 5 points: Figures and tables are effective

---

## Presentation Guidelines

Prepare a 10-minute presentation with 5 minutes Q&A:

```markdown
## Slide Structure (10-12 slides)

1. **Title Slide** (30 sec)
   - Title, your name, date

2. **Problem Motivation** (1 min)
   - Why this matters
   - Current limitations

3. **Research Question** (30 sec)
   - Clear statement of what you're investigating

4. **Related Work** (1 min)
   - Key prior work
   - What's missing

5. **Proposed Approach** (2 min)
   - High-level overview
   - Key innovations

6. **Technical Details** (2 min)
   - Algorithm or architecture
   - How it works

7. **Experimental Design** (1 min)
   - Benchmarks and baselines
   - Metrics

8. **Expected Results** (1 min)
   - What you predict
   - Ablations

9. **Contributions** (30 sec)
   - Summary of contributions

10. **Limitations and Future Work** (30 sec)
    - Honest assessment

11. **Questions** (5 min)
    - Be prepared for challenges
```

---

## Resources

### Key Survey Papers
- Xi et al. (2023). "The Rise and Potential of LLM Based Agents" arXiv:2309.07864
- Wang et al. (2024). "A Survey on Large Language Model based Autonomous Agents" arXiv:2308.11432
- Sumers et al. (2024). "Language Agents" arXiv:2403.12897

### Research Venues
- NeurIPS, ICML, ICLR (Machine Learning)
- ACL, EMNLP, NAACL (NLP)
- AAAI, IJCAI (AI General)
- CHI, UIST (Human-AI Interaction)

### Writing Resources
- "How to Write a Great Research Paper" (Simon Peyton Jones)
- "The Science of Scientific Writing" (Gopen & Swan)
- Anthropic, OpenAI, DeepMind research blogs

---

## Submission

- **Format**: Directory with all deliverables
- **Filename**: `L12_proposal_[your_name]/`
- **Due**: End of Week 12
- **Presentation**: 10-minute slot during final week

---

## Common Pitfalls to Avoid

### Problem Selection
- Too broad ("solve AGI")
- Too narrow ("improve accuracy by 0.5%")
- Not novel (already solved)
- Not feasible (requires resources you don't have)

### Literature Review
- Missing key papers
- No critical analysis
- Poor positioning
- Outdated references

### Technical Approach
- Hand-waving ("we use deep learning")
- Over-complicated without justification
- No theoretical grounding
- Infeasible implementation

### Experimental Design
- Wrong baselines
- Unfair comparisons
- Meaningless metrics
- No ablations

### Writing
- Unclear thesis
- Poor organization
- Too much jargon
- Missing figures

---

## Checklist Before Submission

### Proposal Document
- [ ] Clear problem statement
- [ ] 10+ papers reviewed
- [ ] Technical approach is detailed
- [ ] Research questions are testable
- [ ] Baselines are appropriate
- [ ] Contributions are explicit
- [ ] Limitations acknowledged
- [ ] 6-8 pages, proper format

### Literature Review
- [ ] 10+ papers annotated
- [ ] Each paper has: contribution, limitation, relevance
- [ ] Papers are recent (mostly 2022-2025)
- [ ] Includes both foundational and recent work

### Presentation
- [ ] 10-12 slides
- [ ] Can present in 10 minutes
- [ ] Key figures are clear
- [ ] Prepared for Q&A

### Optional Prototype
- [ ] Demonstrates core idea
- [ ] Runs without errors
- [ ] Has README with instructions

---

## Time Estimate

- Minimum: 12 hours
- Expected: 20 hours
- Maximum: 30 hours

### Time Breakdown
- Literature search: 4-6 hours
- Writing proposal: 8-12 hours
- Creating slides: 3-4 hours
- Prototype (optional): 4-6 hours
- Revision: 2-4 hours
