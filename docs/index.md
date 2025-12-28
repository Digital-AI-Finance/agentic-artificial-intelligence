---
layout: default
title: Home
nav_order: 1
description: "PhD Course on Building Autonomous AI Systems with Large Language Models"
permalink: /
---

# Agentic Artificial Intelligence

PhD course on LLM-based autonomous agents, multi-agent systems, and advanced RAG architectures.

**Instructor:** {{ site.course.instructor.name }} | **Institution:** {{ site.course.instructor.institution }} | **Semester:** {{ site.course.semester }}

---

## Course Modules

| Week | Topic | Materials |
|:-----|:------|:----------|
{% for week in site.data.weeks %} | [{{ week.number }}]({{ '/weeks/week-' | append: week.number | relative_url }}) | {{ week.title }} | [Slides]({{ '/slides/' | append: week.folder | append: '.pdf' | relative_url }}) {% for notebook in week.notebooks %}/ [{{ notebook.name }}](https://colab.research.google.com/github/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/{{ week.folder }}/{{ notebook.file }}){% endfor %} |
{% endfor %}

---

## Topics by Module

| Module | Weeks | Topics |
|:-------|:------|:-------|
| Foundations | 1-2 | Agent definitions, ReAct, Chain-of-Thought, prompting |
| Core Capabilities | 3-5 | Tool use, MCP, planning, multi-agent systems |
| Frameworks | 6-7 | LangGraph, CrewAI, Self-RAG, advanced retrieval |
| Safety & Evaluation | 8-10 | GraphRAG, hallucination prevention, benchmarks |
| Applications | 11-12 | Domain agents, research frontiers, projects |

---

## Quick Links

| Resource | Description |
|:---------|:------------|
| [Slides]({{ '/slides' | relative_url }}) | All 12 lecture PDFs |
| [Quizzes]({{ '/quizzes' | relative_url }}) | Self-assessment for each week |
| [Glossary]({{ '/glossary' | relative_url }}) | 35+ key terms defined |
| [Reference Cards]({{ '/reference' | relative_url }}) | Printable summaries |
| [Code Playground]({{ '/playground' | relative_url }}) | Browser-based Python |
| [GitHub]({{ site.course.github }}) | Source repository |

---

## Prerequisites

- Python proficiency (3.10+)
- Machine learning fundamentals
- Transformer architecture basics
- OpenAI or Anthropic API access

## Quick Start

```bash
pip install langchain langchain-openai python-dotenv
export OPENAI_API_KEY="your-key"
```
