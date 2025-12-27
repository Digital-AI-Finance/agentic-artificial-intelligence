---
layout: default
title: Videos
nav_order: 18
---

# Video Resources

Supplementary video content for the course.

{: .note }
> Video lectures are supplementary to the main course materials. The primary content is in slides and notebooks.

## Course Lectures

*Video lectures will be added as they become available.*

## Recommended External Videos

### Introduction to Agents

<div class="video-grid">

<div class="video-card">
<h4>What is an AI Agent?</h4>
<p class="video-meta">DeepLearning.AI | 15 min</p>
<div class="video-embed">
<iframe
  width="100%"
  height="200"
  src="https://www.youtube.com/embed/placeholder"
  title="What is an AI Agent?"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
  loading="lazy">
</iframe>
</div>
<p class="video-description">Introduction to the concept of AI agents and their capabilities.</p>
<p><strong>Relevant to:</strong> Week 1</p>
</div>

</div>

## Conference Talks

### NeurIPS & ICML

| Talk | Speaker | Year | Link |
|:-----|:--------|:-----|:-----|
| *Coming soon* | - | - | - |

### Industry Talks

| Talk | Company | Topic | Link |
|:-----|:--------|:------|:-----|
| *Coming soon* | - | - | - |

## Tutorial Series

### Building Agents from Scratch

*Playlist links will be added.*

### RAG Deep Dives

*Playlist links will be added.*

## Adding Videos

To embed a YouTube video in course materials:

```html
<div class="video-embed">
<iframe
  width="100%"
  height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="Video Title"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
  loading="lazy">
</iframe>
</div>
```

For accessibility, always include:
- Descriptive `title` attribute
- `loading="lazy"` for performance
- Fallback text/link for users who can't view embeds

---

*Have a video recommendation? Share it in [Discussions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions)!*

<style>
.video-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.video-card {
  background: var(--bg-secondary, #f8f9fa);
  border-radius: 8px;
  padding: 1rem;
  border: 1px solid var(--border-color, #ddd);
}

.video-card h4 {
  margin-top: 0;
  color: #3333B2;
}

.video-meta {
  font-size: 0.85rem;
  color: var(--text-muted, #999);
  margin-bottom: 1rem;
}

.video-embed {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  margin-bottom: 1rem;
  border-radius: 4px;
}

.video-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.video-description {
  font-size: 0.9rem;
  color: var(--text-secondary, #666);
}

@media print {
  .video-embed {
    display: none;
  }

  .video-card::after {
    content: "(Video - see online version)";
    font-style: italic;
    color: #999;
  }
}
</style>
