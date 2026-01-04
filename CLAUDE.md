# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PhD-level 12-week course on Agentic AI: LLM agents, multi-agent systems, RAG, and knowledge graphs. Beamer slides, Jupyter notebooks, Python chart scripts, and Jekyll-based GitHub Pages site.

**Live Site**: https://digital-ai-finance.github.io/agentic-artificial-intelligence/

## Commands

### LaTeX Compilation
```bash
# Compile slides (from lesson folder)
pdflatex L01_Introduction_Agentic_AI.tex

# Move aux files to temp/ (Windows)
move *.aux *.log *.nav *.out *.snm *.toc temp\

# Move aux files to temp/ (Unix)
mv *.aux *.log *.nav *.out *.snm *.toc temp/
```

### Chart Generation
```bash
# Run single chart
python L01_Introduction_Agentic_AI/01_agent_definition/agent_definition.py

# Run all chart tests
pytest tests/test_charts.py -v

# Run charts for specific lecture
pytest tests/test_charts.py -k "L01" -v
```

### Notebook Validation
```bash
pytest --nbval-lax L*/notebooks/*.ipynb
```

### Jekyll Site (from docs/ folder)
```bash
bundle install
bundle exec jekyll serve --livereload  # http://localhost:4000
bundle exec htmlproofer ./_site --disable-external
```

### Quality Scripts
```bash
python scripts/extract_glossary.py       # Audit term definitions across lectures
python scripts/generate_term_index.py    # Create cross-lecture term matrix
python scripts/quality_check.py          # Playwright-based accessibility check
python scripts/screenshot_website.py     # Capture website screenshots
```

## Architecture

### Lesson Structure (L01-L12)
```
LXX_Topic_Name/
  LXX_Topic_Name.tex      # Beamer slides (Madrid theme, 8pt)
  01_concept_name/        # Chart folder
    concept_name.py       # Script generates concept_name.pdf
  notebooks/              # Jupyter notebooks
  exercises/              # Student exercises with rubrics
  readings/               # Reading guides with paper annotations
  temp/                   # LaTeX auxiliary files
```

### Reviews (reviews/)
- `L01_review.md` through `L12_review.md` - Individual lecture reviews
- `REVIEW_SUMMARY.md` - Cumulative review with citation verification, chart usage

### Jekyll Site (docs/)
- `_config.yml` - Site config (Just the Docs theme v0.8.2)
- `_data/weeks.yml` - Week metadata (topics, papers, notebooks)
- `_data/glossary.yml` - Term definitions by week
- `_data/quizzes.yml` - Interactive quiz questions
- `_includes/quiz.html` - Quiz component
- `_layouts/week.html` - Week page template
- `weeks/*.md` - Week 1-12 pages (collection with `/weeks/:name/` permalink)

### Beamer Conventions
- Theme: Madrid, 8pt, aspectratio=169
- Chart width: 0.55\textwidth (with text) or 0.65\textwidth (standalone)
- Colors defined in each .tex preamble:
  - mlpurple: RGB(51,51,178) / #3333B2
  - mlblue: RGB(0,102,204) / #0066CC
  - mlorange: RGB(255,127,14) / #FF7F0E
  - mlgreen: RGB(44,160,44) / #2CA02C
  - mlred: RGB(214,39,40) / #D62728
- Use `\bottomnote{text}` for key takeaways on each slide

### Chart Script Requirements
```python
plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
    'figure.figsize': (10, 6), 'figure.dpi': 150
})
# Output: plt.savefig(Path(__file__).parent / 'concept_name.pdf', dpi=300, bbox_inches='tight')
```

### Term Definitions
Define terms inline at first use: `LLM (Large Language Model)`, `Leiden algorithm (graph clustering method)`

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
| 12 | L12 | Research frontiers |

## CI/CD Workflows

- **compile_slides.yml**: Compiles L*/*.tex, checks for Overfull warnings
- **validate_charts.yml**: pytest on tests/test_charts.py
- **validate_notebooks.yml**: pytest --nbval-lax
- **pre-commit.yml**: black, isort, flake8, markdownlint
- **pages.yml**: Deploys docs/ to GitHub Pages
- **link-check.yml**: Weekly arXiv/DOI validation
- **lighthouse.yml**: Accessibility scoring (>90 required)

## Jekyll/Liquid Gotchas

1. **Filter chain bug**: Pre-calculate numbers before append
   ```liquid
   {% assign prev = week_num | minus: 1 %}
   {{ '/weeks/week-' | append: prev | relative_url }}
   ```

2. **Markdown in layouts**: Use HTML tags in _layouts/*.html, not markdown

3. **Liquid in comments**: Jekyll processes tags even in HTML comments - remove Liquid syntax

4. **Sass units**: Just the Docs uses rem - convert px to rem (264px -> 16.5rem)

5. **PDF exclusion**: Never exclude *.pdf in _config.yml - slides need to be downloadable

## Citation Format

All arXiv citations must be verified. Format: `Author et al. (Year). "Title." arXiv:XXXX.XXXXX`

Key verified papers:
- ReAct: arXiv:2210.03629
- CoT: arXiv:2201.11903
- ToT: arXiv:2305.10601
- Reflexion: arXiv:2303.11366
- Self-RAG: arXiv:2310.11511
- GraphRAG: arXiv:2404.16130
- AgentBench: arXiv:2308.03688
- Sumers et al. (CoALA): arXiv:2309.02427 (NOT 2403.12897)
