---
layout: default
title: Slides
nav_order: 22
---

# Course Slides

Download lecture slides for each week. All slides are in PDF format, optimized for printing and annotation.

<div class="slides-status" style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
  <strong>Status:</strong> 5 of 12 slide decks available for download. Additional slides are being compiled.
</div>

---

## Available Slides

{% for week in site.data.weeks %}
{% assign pdf_path = week.folder | append: "/" | append: week.folder | append: ".pdf" %}
<div class="slide-card" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; margin: 0.5rem 0; background: var(--bg-secondary, #f8f9fa); border-radius: 8px; border-left: 4px solid {% if week.number <= 5 %}#2CA02C{% else %}#999{% endif %};">
  <div>
    <h4 style="margin: 0 0 0.25rem 0;">
      <a href="{{ '/weeks/week-' | append: week.number | relative_url }}">Week {{ week.number }}: {{ week.title }}</a>
    </h4>
    <p style="margin: 0; color: #666; font-size: 0.9rem;">{{ week.description }}</p>
  </div>
  <div style="text-align: right;">
    {% if week.number <= 5 %}
    <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/raw/main/{{ pdf_path }}" class="btn btn-primary" style="white-space: nowrap;">
      Download PDF
    </a>
    <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/{{ pdf_path }}" class="btn btn-outline" style="white-space: nowrap; margin-left: 0.5rem;">
      View
    </a>
    {% else %}
    <span style="color: #999; font-style: italic;">Coming soon</span>
    {% endif %}
  </div>
</div>
{% endfor %}

---

## Slide Specifications

| Property | Value |
|----------|-------|
| Format | PDF (Beamer) |
| Theme | Madrid |
| Font Size | 8pt base |
| Charts | Matplotlib/Python generated |
| Resolution | 300 DPI |

---

## Using the Slides

### For Instructors

These slides are designed for 90-minute lectures. Each deck includes:
- Title slide with learning objectives
- Concept slides with visualizations
- Code examples (non-executable)
- Discussion prompts
- Summary and preview

### For Students

We recommend:
1. Download before class for annotation
2. Follow along with Colab notebooks
3. Review reading guides for deeper understanding
4. Complete exercises after lecture

### Printing

For best results:
- Use "Handouts" mode (4-6 slides per page)
- Print in color for chart readability
- Consider double-sided to save paper

---

## Contributing

Found an error or want to improve a slide?

<div class="resource-links">
  <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/issues/new?labels=slides&template=bug_report.md" class="btn btn-primary">
    Report Issue
  </a>
  <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/pulls" class="btn btn-secondary">
    Submit PR
  </a>
</div>
