---
layout: default
title: API
nav_order: 20
---

# Course Data API

Access course data programmatically through our JSON API.

## Endpoints

| Endpoint | Description |
|:---------|:------------|
| [`/api/course.json`](course.json) | Complete course data (weeks, glossary, metadata) |
| [`/api/weeks.json`](weeks.json) | Week summaries only |
| [`/api/glossary.json`](glossary.json) | Glossary terms only |

## Usage Examples

### Python

```python
import requests

# Fetch course data
url = "https://digital-ai-finance.github.io/agentic-artificial-intelligence/api/course.json"
response = requests.get(url)
data = response.json()

# Get week 5 topics
week5 = next(w for w in data["weeks"] if w["number"] == 5)
print(f"Week 5: {week5['title']}")
for topic in week5["topics"]:
    print(f"  - {topic}")
```

### JavaScript

```javascript
// Fetch and display weeks
fetch('/agentic-artificial-intelligence/api/weeks.json')
  .then(response => response.json())
  .then(data => {
    data.weeks.forEach(week => {
      console.log(`Week ${week.number}: ${week.title}`);
    });
  });
```

### Command Line

```bash
# Get all weeks
curl -s https://digital-ai-finance.github.io/agentic-artificial-intelligence/api/weeks.json | jq '.weeks[].title'

# Get glossary terms for week 3
curl -s https://digital-ai-finance.github.io/agentic-artificial-intelligence/api/glossary.json | jq '.glossary[] | select(.week == 3)'
```

## Response Schema

### Course Endpoint

```json
{
  "course": {
    "name": "string",
    "code": "string",
    "semester": "string",
    "credits": "number",
    "weeks": "number",
    "instructor": {
      "name": "string",
      "email": "string",
      "institution": "string"
    },
    "github": "string",
    "website": "string"
  },
  "weeks": [...],
  "glossary": [...],
  "meta": {
    "generated_at": "ISO 8601 timestamp",
    "api_version": "string"
  }
}
```

### Week Object

```json
{
  "number": 1,
  "title": "Introduction to Agentic AI",
  "description": "...",
  "folder": "L01_Introduction_Agentic_AI",
  "status": "complete",
  "topics": ["topic1", "topic2"],
  "learning_objectives": ["objective1", "objective2"],
  "notebooks": [
    {
      "name": "First Agent",
      "file": "notebooks/L01_first_agent.ipynb",
      "colab_url": "https://colab.research.google.com/..."
    }
  ],
  "papers": [
    {
      "title": "Paper Title",
      "authors": "Author et al.",
      "year": 2023,
      "arxiv": "2210.03629",
      "url": "https://arxiv.org/abs/2210.03629"
    }
  ],
  "slides_url": "...",
  "page_url": "..."
}
```

### Glossary Term Object

```json
{
  "term": "ReAct",
  "definition": "Reasoning and Acting paradigm...",
  "related": ["Chain-of-Thought", "Agent Loop"],
  "week": 1
}
```

## Rate Limits

This is a static API hosted on GitHub Pages. There are no rate limits, but please be respectful with request frequency.

## CORS

The API supports cross-origin requests from any domain.

## Updates

The API data is regenerated whenever the site is rebuilt (typically on each push to main branch). Check the `meta.generated_at` field for the last update time.

---

*API Version: 1.0*
