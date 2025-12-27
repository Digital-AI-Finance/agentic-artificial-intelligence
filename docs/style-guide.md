---
layout: default
title: Style Guide
nav_order: 16
---

# Content Style Guide

Guidelines for creating consistent, high-quality content for this course.

## Writing Style

### Voice and Tone

- **Academic but accessible**: Write for PhD students, but explain concepts clearly
- **Active voice preferred**: "The agent retrieves documents" not "Documents are retrieved by the agent"
- **Second person for instructions**: "You will implement..." or "Configure your..."
- **Present tense for descriptions**: "ReAct combines reasoning and acting"

### Terminology Consistency

Use these standard terms throughout:

| Preferred | Avoid |
|:----------|:------|
| agent | bot, assistant, AI |
| LLM | language model, model |
| tool use | function calling (unless API-specific) |
| retrieval | fetching, getting |
| reasoning | thinking, processing |
| trajectory | path, sequence |

### Capitalization

- **Concepts**: lowercase (agent, tool use, chain-of-thought)
- **Proper names**: capitalize (LangGraph, ReAct, GPT-4)
- **Acronyms**: all caps (LLM, RAG, API)
- **Headings**: sentence case ("How agents work" not "How Agents Work")

## Document Structure

### Slides (LaTeX/Beamer)

```
Slide structure:
- Title (clear, concise)
- 3-4 bullet points maximum
- Optional bottomnote for key insight
- No code on slides (reference notebooks)
```

**Font sizes**: 8pt base, Madrid theme

**Chart requirements**:
- Separate folder per chart
- figsize (10, 6)
- Minimum 10pt fonts
- Brand colors only

### Notebooks

```
Section structure:
1. Learning objectives (markdown cell)
2. Setup and imports
3. Conceptual explanation
4. Implementation with inline comments
5. Experimentation/exercises
6. Summary
```

**Code style**:
- Clear variable names
- Type hints for function signatures
- Docstrings for public functions
- Error handling for API calls

### Documentation Pages

```markdown
---
layout: default
title: Page Title
nav_order: X
---

# Page Title

Brief introduction (1-2 sentences).

## Section 1

Content...

## Section 2

Content...

---

*Footer notes if needed*
```

## Formatting Conventions

### Code Blocks

Always specify language:

````markdown
```python
def example_function():
    pass
```
````

### Tables

Use proper header rows:

```markdown
| Column 1 | Column 2 | Column 3 |
|:---------|:---------|:---------|
| Data 1   | Data 2   | Data 3   |
```

### Links

- **Internal**: Use relative URLs with Jekyll tags
- **External**: Include descriptive text

```markdown
See the [Getting Started guide]({{ '/getting-started' | relative_url }}).

Read the [ReAct paper](https://arxiv.org/abs/2210.03629) for details.
```

### Callouts

Use Jekyll callouts for important notes:

```markdown
{: .note }
> This is a helpful note.

{: .warning }
> This is a warning about potential issues.

{: .important }
> This is critical information.
```

## Academic Standards

### Citations

- Include arXiv IDs where available
- Format: Author et al. (Year)
- Link to paper in references

```markdown
The ReAct paradigm (Yao et al., 2023) combines reasoning and acting.

**Reference**: [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629)
```

### Mathematical Notation

- Use LaTeX for formulas
- Define symbols on first use
- Keep notation consistent within a document

```latex
The probability $P(a|s)$ represents the action distribution given state $s$.
```

### Figures and Charts

- Include caption/description
- Cite source if not original
- Use consistent color palette

## Brand Colors

Primary palette for all visualizations:

| Name | Hex | Usage |
|:-----|:----|:------|
| MLPURPLE | `#3333B2` | Primary, headings |
| MLBLUE | `#0066CC` | Links, secondary |
| MLORANGE | `#FF7F0E` | Accents, highlights |
| MLGREEN | `#2CA02C` | Success, positive |
| MLRED | `#D62728` | Errors, warnings |
| MLLAVENDER | `#ADADE0` | Backgrounds |

## File Naming

### Folders

```
LXX_Topic_Name/           # Lesson folder
  LXX_Topic_Name.tex      # Main slides
  01_chart_name/          # Chart folder
    chart.py              # Chart script
    chart.pdf             # Generated chart
  notebooks/              # Notebooks folder
    LXX_notebook_name.ipynb
```

### Documentation

```
docs/
  page-name.md           # Kebab-case for pages
  _data/
    data-file.yml        # Kebab-case for data
  api/
    endpoint.json        # Lowercase for API
```

## Accessibility

### Images

- Always include alt text
- Describe what the image shows, not just what it is

```markdown
![Architecture diagram showing agent loop with observation, reasoning, and action phases](./agent-loop.png)
```

### Tables

- Use header rows
- Don't rely on color alone for meaning
- Keep cells concise

### Code

- Add comments for complex logic
- Use descriptive variable names
- Provide text explanation alongside code

## Quality Checklist

Before submitting content, verify:

- [ ] Spelling and grammar checked
- [ ] Links tested and working
- [ ] Code runs without errors
- [ ] Consistent terminology used
- [ ] Proper citations included
- [ ] Accessibility requirements met
- [ ] Brand colors used correctly
- [ ] File naming conventions followed

---

*Questions about style? Open a [discussion](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions).*
