---
layout: default
title: Weeks
nav_order: 2
has_children: true
---

# Course Weeks

This course consists of 12 weeks covering the theory and practice of agentic AI systems.

## Progress Overview

<div class="progress-bar" style="margin: 1.5rem 0; height: 24px; background: #e9ecef; border-radius: 12px;">
  <div class="progress-fill" style="width: 100%; height: 100%; background: linear-gradient(90deg, #3333B2, #0066CC); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
    12/12 Weeks Complete
  </div>
</div>

## All Weeks

{% for week in site.data.weeks %}
<div class="week-card">
  <h3>
    <a href="{{ '/weeks/week-' | append: week.number | relative_url }}">Week {{ week.number }}: {{ week.title }}</a>
  </h3>
  <p class="week-meta">{{ week.description }}</p>
  <div class="resource-links">
    <a href="{{ '/slides/' | append: week.folder | append: '.pdf' | relative_url }}">Slides</a>
    {% for notebook in week.notebooks %}
    <a href="https://colab.research.google.com/github/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/{{ week.folder }}/{{ notebook.file }}">
      {{ notebook.name }}
    </a>
    {% endfor %}
  </div>
</div>
{% endfor %}
