---
layout: default
title: Home
nav_order: 1
description: "PhD Course on Building Autonomous AI Systems with Large Language Models"
permalink: /
---

{% include skip-link.html %}

<main id="main-content" role="main" aria-label="Course homepage">

<div class="hero" role="banner">
  <h1>Agentic Artificial Intelligence</h1>
  <p>A comprehensive PhD course on building autonomous AI systems that can reason, plan, use tools, and collaborate.</p>
  <div class="hero-buttons">
    <a href="{{ '/getting-started' | relative_url }}" class="btn btn-primary">Get Started</a>
    <a href="{{ '/syllabus' | relative_url }}" class="btn btn-outline" style="background: rgba(255,255,255,0.1); color: white; border-color: white;">View Syllabus</a>
    <a href="{{ site.course.github }}" class="btn btn-outline" style="background: rgba(255,255,255,0.1); color: white; border-color: white;">GitHub</a>
  </div>
</div>

## Course Overview

This 12-week doctoral course covers the theory and practice of building agentic AI systems. Students will learn to design, implement, and evaluate autonomous agents that leverage large language models for complex reasoning and task execution.

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-number">12</div>
    <div class="stat-label">Weeks</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">15+</div>
    <div class="stat-label">Notebooks</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">40+</div>
    <div class="stat-label">Papers</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">12</div>
    <div class="stat-label">Exercises</div>
  </div>
</div>

## Course Modules

{% for week in site.data.weeks %}
<div class="week-card">
  <h3>
    <a href="{{ '/weeks/week-' | append: week.number | relative_url }}">Week {{ week.number }}: {{ week.title }}</a>
    {% if week.status == "complete" %}
    <span class="badge badge-low">Complete</span>
    {% else %}
    <span class="badge badge-new">Coming Soon</span>
    {% endif %}
  </h3>
  <p class="week-meta">{{ week.description }}</p>
  <div class="resource-links">
    <a href="{{ site.baseurl }}/{{ week.folder }}/{{ week.folder }}.pdf">Slides (PDF)</a>
    {% for notebook in week.notebooks %}
    <a href="https://colab.research.google.com/github/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/{{ week.folder }}/{{ notebook.file }}" style="display: inline-flex; align-items: center; gap: 0.25rem;">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="height: 18px; vertical-align: middle;">
      {{ notebook.name }}
    </a>
    {% endfor %}
  </div>
</div>
{% endfor %}

## Key Topics Covered

| Module | Topics |
|:-------|:-------|
| **Foundations** (Weeks 1-2) | Agent definitions, ReAct paradigm, Chain-of-Thought, prompting strategies |
| **Core Capabilities** (Weeks 3-5) | Tool use, function calling, planning, multi-agent systems |
| **Frameworks** (Weeks 6-7) | LangGraph, CrewAI, Self-RAG, advanced retrieval |
| **Safety & Evaluation** (Weeks 8-10) | GraphRAG, hallucination prevention, benchmarking |
| **Applications** (Weeks 11-12) | Domain agents, research frontiers, final projects |

## Prerequisites

- Strong Python programming skills
- Familiarity with machine learning concepts
- Basic understanding of transformer architectures
- Access to OpenAI or Anthropic API keys

## Quick Start

```python
# Install dependencies
pip install langchain langchain-openai python-dotenv

# Set up your API key
export OPENAI_API_KEY="your-key-here"

# Open the first notebook
jupyter notebook L01_Introduction_Agentic_AI/notebooks/L01_first_agent.ipynb
```

Or use Google Colab - click any notebook link above to open directly in the cloud.

---

<footer role="contentinfo" style="text-align: center; margin-top: 2rem;">
  <p>
    <strong>Instructor:</strong> {{ site.course.instructor.name }}<br>
    <strong>Institution:</strong> {{ site.course.instructor.institution }}<br>
    <strong>Semester:</strong> {{ site.course.semester }}
  </p>
</footer>

</main>
