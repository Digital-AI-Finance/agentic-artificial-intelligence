# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PhD-level 12-week course on Agentic AI: LLM agents, multi-agent systems, RAG, and knowledge graphs. Content managed via GitHub Issues (81 total) with Beamer slides, Jupyter notebooks, Python chart scripts, and a Jekyll-based GitHub Pages site.

**Live Site**: https://digital-ai-finance.github.io/agentic-artificial-intelligence/

## Commands

### LaTeX Compilation
```bash
# Compile slides (from lesson folder)
pdflatex L01_Introduction_Agentic_AI.tex
# Move aux files to temp/
mv *.aux *.log *.nav *.out *.snm *.toc temp/
```

### Chart Generation
```bash
# Run single chart
python L01_Introduction_Agentic_AI/01_agent_definition/chart.py

# Validate all charts (CI workflow)
for f in L*/*/chart.py; do python "$f"; done
```

### Notebook Validation
```bash
pytest --nbval-lax L*/notebooks/*.ipynb
```

### GitHub Pages / Jekyll
```bash
# Local development (from docs/ folder)
cd docs
bundle install
bundle exec jekyll serve --livereload

# Build only (no serve)
bundle exec jekyll build

# Check for broken links
bundle exec htmlproofer ./_site --disable-external
```

### Issue Management
```bash
# Update issue body
gh issue edit <number> --repo Digital-AI-Finance/agentic-artificial-intelligence --body-file body.md

# Batch update (uses update_issues_phd.py)
python update_issues_phd.py
```

## Architecture

### Repository Structure
```
agentic-artificial-intelligence/
  L01-L12/                 # Lesson folders (slides, charts, notebooks)
  docs/                    # GitHub Pages Jekyll site
  .github/workflows/       # CI/CD pipelines
  requirements.txt         # Python dependencies
  SYLLABUS.md             # Course schedule
```

### Lesson Structure
```
LXX_Topic_Name/
  LXX_Topic_Name.tex      # Beamer slides (Madrid theme, 8pt)
  01_concept_name/        # Chart folder
    chart.py              # Standalone script -> chart.pdf
    chart.pdf
  notebooks/              # Jupyter notebooks
  exercises/              # Student exercises
  readings/               # Paper annotations
  temp/                   # LaTeX auxiliary files
```

### GitHub Pages Structure (docs/)
```
docs/
  _config.yml             # Jekyll config (Just the Docs v0.8.2)
  _data/
    weeks.yml             # Course weeks metadata (topics, papers, notebooks)
    glossary.yml          # 35+ term definitions by week
    quizzes.yml           # Interactive quiz questions
    icons.yml             # SVG icons for topics/actions
  _includes/
    quiz.html             # Interactive quiz component
    theme-toggle.html     # Dark/light mode toggle
    openalex-widget.html  # Publication display
    hypothesis.html       # Annotation integration
    reading-progress.html # Progress bar
  _layouts/
    week.html             # Week page template
  _sass/color_schemes/
    custom.scss           # Course color scheme
  index.md                # Landing page
  weeks/                  # Week 1-12 pages
  glossary.md             # Searchable glossary
  quizzes.md              # Interactive quizzes
  architectures.md        # Mermaid architecture diagrams
  visual-assets.md        # Icons and infographics
```

### Issue Types and Counts (81 total)
- **SLIDES** (13): Bloom's taxonomy objectives, 15-slide structure, 3-5 papers
- **NOTEBOOK** (21): Python 3.11+, API requirements, implementation sections
- **CHART** (22): Single figure, figsize=(10,6), ML color palette
- **EXERCISE** (12): 100-point rubric, time estimates
- **READING** (12): Critical reading guide, discussion questions
- **PROJECT** (1): Final project requirements

### Beamer Template Conventions
```latex
\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}

% Standard colors
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlorange}{RGB}{255,127,14}
\definecolor{mlgreen}{RGB}{44,160,44}
\definecolor{mlred}{RGB}{214,39,40}

% Chart inclusion
\includegraphics[width=0.55\textwidth]{01_folder/chart.pdf}

% Bottom annotation
\bottomnote{Key takeaway text}
```

### Chart Script Template
```python
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})

MLPURPLE, MLBLUE, MLORANGE = '#3333B2', '#0066CC', '#FF7F0E'
MLGREEN, MLRED = '#2CA02C', '#D62728'

# ... plotting code ...

plt.savefig(Path(__file__).parent / 'chart.pdf',
            dpi=300, bbox_inches='tight')
plt.close()
```

## Week-to-Topic Mapping

| Week | Folder | Topic | Key Papers |
|------|--------|-------|------------|
| 1 | L01 | Introduction, ReAct paradigm | Yao 2023, Wang 2024 |
| 2 | L02 | LLM foundations, CoT/ToT | Wei 2022, Yao 2023 |
| 3 | L03 | Tool use, MCP, function calling | Schick 2023, Patil 2023 |
| 4 | L04 | Planning, Reflexion, memory | Shinn 2023, Zhou 2024 |
| 5 | L05 | Multi-agent architectures | Wu 2023, Hong 2023 |
| 6 | L06 | LangGraph, AutoGen, CrewAI | LangChain docs, Qiao 2024 |
| 7 | L07 | Self-RAG, CRAG, RAPTOR | Asai 2023, Yan 2024 |
| 8 | L08 | GraphRAG, knowledge graphs | Edge 2024, Besta 2024 |
| 9 | L09 | Hallucination prevention | Dhuliawala 2023, Min 2023 |
| 10 | L10 | AgentBench, evaluation | Liu 2023, Jimenez 2024 |
| 11 | L11 | Domain applications | Ridnik 2024, Li 2024 |
| 12 | L12 | Research frontiers, projects | Park 2023, Wang 2023 |

## CI/CD Workflows

- **compile_slides.yml**: Compiles L*/*.tex, checks for Overfull warnings
- **validate_charts.yml**: Runs all chart.py scripts, verifies PDF output
- **validate_notebooks.yml**: pytest --nbval-lax on all notebooks
- **pages.yml**: Deploys docs/ to GitHub Pages
- **link-check.yml**: Weekly arXiv/DOI link validation (Sunday)
- **lighthouse.yml**: Accessibility/performance scoring (>90 required)

## Key Files

- `update_issues_phd.py`: Contains all 48 research papers with arXiv links, generates enhanced issue bodies
- `template_beamer_final.tex`: Reference template with 28 slide layouts
- `requirements.txt`: Python dependencies (langchain, openai, anthropic, chromadb)
- `docs/_config.yml`: Jekyll site configuration
- `docs/_data/weeks.yml`: Week metadata (topics, papers, notebooks per week)
- `docs/_data/glossary.yml`: 35+ agentic AI terms with definitions

## GitHub Pages Features

| Feature | Location | Description |
|---------|----------|-------------|
| Dark Mode | _includes/theme-toggle.html | Persistent toggle (localStorage) |
| Quizzes | _includes/quiz.html, _data/quizzes.yml | Interactive self-assessment (12 weeks) |
| Glossary | glossary.md, _data/glossary.yml | Searchable term definitions |
| Architectures | architectures.md | Mermaid diagrams (ReAct, RAG, etc.) |
| Week Pages | weeks/*.md | Learning objectives, papers, notebooks |
| Code Playground | playground.md | Pyodide browser-based Python |
| Framework Comparison | comparison.md | Sortable/filterable tables |
| Quick Reference | reference.md | Printable cards for all 12 weeks |
| JSON API | api/*.json | weeks, charts, exercises, quizzes endpoints |
| Accessibility | accessibility.md, custom.css | WCAG 2.1 AA, print stylesheets, skip links |

### Site Enhancements (assets/js/enhancements.js)
- Code copy buttons on all code blocks
- Keyboard shortcuts: Cmd+K (search), arrows (week nav), ? (help)
- Auto table of contents for long pages
- Reading time estimates
- Progress tracking (localStorage)

## Data Files (docs/_data/)

| File | Purpose |
|------|---------|
| weeks.yml | Course weeks metadata (topics, papers, notebooks) |
| quizzes.yml | Interactive quiz questions for all 12 weeks |
| glossary.yml | 35+ agentic AI term definitions |
| charts.yml | Chart metadata and descriptions |
| exercises.yml | Exercise specifications with rubrics |
| readings.yml | Reading guide metadata |
| icons.yml | SVG icons for course topics |

## Issue Labels

| Label | Color | Description |
|-------|-------|-------------|
| type:slides | #0366d6 | Beamer slide content |
| type:notebook | #7057ff | Jupyter notebooks |
| type:chart | #1d76db | Python chart scripts |
| type:pages | #0366d6 | GitHub Pages/Jekyll |
| type:quiz | #7057ff | Quiz content |
| type:qa | #d93f0b | Quality assurance |
| type:a11y | #0e8a16 | Accessibility |
