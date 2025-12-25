# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PhD-level 12-week course on Agentic AI: LLM agents, multi-agent systems, RAG, and knowledge graphs. Content managed via GitHub Issues (81 total) with Beamer slides, Jupyter notebooks, and Python chart scripts.

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

### Issue Management
```bash
# Update issue body
gh issue edit <number> --repo Digital-AI-Finance/agentic-artificial-intelligence --body-file body.md

# Batch update (uses update_issues_phd.py)
python update_issues_phd.py
```

## Architecture

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

### Issue Types and Counts
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

# ... plotting code ...

plt.savefig(Path(__file__).parent / 'chart.pdf',
            dpi=300, bbox_inches='tight')
plt.close()
```

## Week-to-Topic Mapping

| Week | Folder | Topic |
|------|--------|-------|
| 1 | L01 | Introduction, ReAct paradigm |
| 2 | L02 | LLM foundations, CoT/ToT |
| 3 | L03 | Tool use, MCP, function calling |
| 4 | L04 | Planning, Reflexion, memory |
| 5 | L05 | Multi-agent architectures |
| 6 | L06 | LangGraph, AutoGen, CrewAI |
| 7 | L07 | Self-RAG, CRAG, RAPTOR |
| 8 | L08 | GraphRAG, knowledge graphs |
| 9 | L09 | Hallucination prevention |
| 10 | L10 | AgentBench, evaluation |
| 11 | L11 | Domain applications |
| 12 | L12 | Research frontiers, projects |

## CI/CD Workflows

- **compile_slides.yml**: Compiles L*/*.tex, checks for Overfull warnings
- **validate_charts.yml**: Runs all chart.py scripts, verifies PDF output
- **validate_notebooks.yml**: pytest --nbval-lax on all notebooks

## Key Files

- `update_issues_phd.py`: Contains all 48 research papers with arXiv links, generates enhanced issue bodies
- `template_beamer_final.tex`: Reference template with 28 slide layouts
- `requirements.txt`: Python dependencies (langchain, openai, anthropic, chromadb)
