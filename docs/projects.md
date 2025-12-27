---
layout: default
title: Project Showcase
nav_order: 14
---

# Project Showcase

Outstanding projects from course participants. These projects demonstrate innovative applications of agentic AI concepts.

{: .note }
> Want to feature your project? Submit it through [Show & Tell Discussions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions/categories/show-and-tell) or contact the instructor.

## Featured Projects

<div class="project-grid">

### Research Paper Analysis Agent
{: .project-title }

<div class="project-card">
<div class="project-meta">
<span class="badge badge-high">Multi-Agent</span>
<span class="badge badge-medium">RAG</span>
<span class="badge badge-low">LangGraph</span>
</div>

**Team**: Anonymous (Spring 2025)

An autonomous system that analyzes research papers using a team of specialized agents:
- **Extractor Agent**: Pulls key claims, methods, and results
- **Critic Agent**: Identifies limitations and potential issues
- **Connector Agent**: Finds related papers using semantic search
- **Summarizer Agent**: Generates structured summaries

**Technologies**: LangGraph, ChromaDB, Claude 3.5 Sonnet

**Key Results**: 85% agreement with human reviewers on paper quality assessment

<div class="resource-links">
<a href="#">View Demo</a>
<a href="#">GitHub</a>
<a href="#">Paper</a>
</div>
</div>

---

### Financial News Trading Agent
{: .project-title }

<div class="project-card">
<div class="project-meta">
<span class="badge badge-high">ReAct</span>
<span class="badge badge-medium">Tool Use</span>
<span class="badge badge-low">Verification</span>
</div>

**Team**: Anonymous (Spring 2025)

A verified news trading system with hallucination prevention:
- Real-time news ingestion from multiple sources
- Multi-step verification using Chain-of-Verification
- Sentiment analysis with confidence calibration
- Trade signal generation with explanation

**Technologies**: OpenAI GPT-4o, FinancialModelingPrep API, Custom verification chain

**Key Results**: 23% reduction in false positive trading signals

<div class="resource-links">
<a href="#">Architecture</a>
<a href="#">Results</a>
</div>
</div>

---

### Code Review Crew
{: .project-title }

<div class="project-card">
<div class="project-meta">
<span class="badge badge-high">CrewAI</span>
<span class="badge badge-medium">Code Agent</span>
<span class="badge badge-low">AST</span>
</div>

**Team**: Anonymous (Spring 2025)

Multi-agent code review system simulating a development team:
- **Security Analyst**: Scans for vulnerabilities (OWASP top 10)
- **Performance Expert**: Identifies optimization opportunities
- **Style Reviewer**: Checks code conventions and readability
- **Test Strategist**: Suggests test cases

**Technologies**: CrewAI, Tree-sitter, CodeLlama

**Key Results**: Identified 40% more issues than single-agent baseline

<div class="resource-links">
<a href="#">Demo Video</a>
<a href="#">GitHub</a>
</div>
</div>

</div>

## Project Categories

### Autonomous Research Assistants

| Project | Description | Agent Type |
|:--------|:------------|:-----------|
| Literature Mapper | Graph-based paper relationship visualization | GraphRAG |
| Experiment Designer | Proposes and validates research hypotheses | Planning |
| Citation Checker | Verifies claims against cited sources | Verification |

### Domain-Specific Agents

| Project | Domain | Key Innovation |
|:--------|:-------|:---------------|
| Legal Contract Analyzer | Law | Clause extraction with precedent retrieval |
| Medical Triage Assistant | Healthcare | Symptom reasoning with safety guardrails |
| Supply Chain Optimizer | Logistics | Multi-objective planning under uncertainty |

### Tool-Augmented Systems

| Project | Tools Used | Capabilities |
|:--------|:-----------|:-------------|
| Data Science Copilot | Python, SQL, Pandas | Natural language to analysis pipeline |
| Web Research Agent | Browser, Search, APIs | Autonomous information gathering |
| DevOps Automator | Git, Docker, K8s | Infrastructure as conversation |

## Submission Guidelines

### Requirements

Your project should demonstrate mastery of course concepts:

1. **Agent Architecture**: Clear design with appropriate agent pattern
2. **Tool Integration**: At least 2 external tools or APIs
3. **Reasoning**: Explicit reasoning trace (CoT, ReAct, etc.)
4. **Evaluation**: Quantitative metrics or user study results
5. **Documentation**: README, architecture diagram, examples

### Evaluation Criteria

| Criterion | Weight | Description |
|:----------|:-------|:------------|
| Innovation | 25% | Novel approach or application |
| Technical Depth | 25% | Appropriate use of course concepts |
| Implementation | 20% | Code quality and completeness |
| Evaluation | 15% | Rigor of testing and metrics |
| Presentation | 15% | Clarity of documentation and demo |

### How to Submit

1. **Prepare your repository**:
   - Clean, documented code
   - README with setup instructions
   - Architecture diagram
   - Demo notebook or video

2. **Create submission**:
   - Post in [Show & Tell](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions/categories/show-and-tell)
   - Include: title, team, summary, links
   - Tag with relevant topics

3. **Presentation**:
   - 10-minute demo during final weeks
   - Q&A with class and instructor

## Past Semesters

### Spring 2025 (Current)

*Projects will be added as they are completed and approved for showcase.*

---

<div style="text-align: center; margin: 2rem 0;">
  <p>Have a project to showcase?</p>
  <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions/new?category=show-and-tell" class="btn btn-primary">
    Submit Your Project
  </a>
</div>

<style>
.project-card {
  background: var(--bg-secondary, #f8f9fa);
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1rem 0 2rem 0;
  border-left: 4px solid #3333B2;
}

.project-meta {
  margin-bottom: 1rem;
}

.project-title {
  color: #3333B2;
  margin-bottom: 0.5rem;
}

.project-card p {
  margin-bottom: 0.5rem;
}

.project-card ul {
  margin: 0.5rem 0;
}
</style>
