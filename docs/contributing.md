---
layout: default
title: Contributing
nav_order: 12
---

# Contributing to Agentic AI Course

Thank you for your interest in improving this course! We welcome contributions from students, researchers, and practitioners.

## Ways to Contribute

### Report Issues

Found a bug, typo, or error? [Open an issue](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/issues/new) with:

- **Title**: Brief description of the issue
- **Location**: File path or page URL
- **Description**: What's wrong and (optionally) how to fix it
- **Labels**: Add appropriate labels (bug, enhancement, documentation)

### Suggest Improvements

Have ideas for new content, better explanations, or additional examples?

1. Check [existing issues](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/issues) to avoid duplicates
2. Open a new issue with the `enhancement` label
3. Describe your suggestion with as much detail as possible

### Submit Pull Requests

Ready to contribute code or content directly?

## Getting Started

### Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/agentic-artificial-intelligence.git
cd agentic-artificial-intelligence

# Add upstream remote
git remote add upstream https://github.com/Digital-AI-Finance/agentic-artificial-intelligence.git
```

### Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# For documentation site
cd docs
bundle install
bundle exec jekyll serve
```

### Create a Branch

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
```

## Contribution Guidelines

### Code Style

**Python**:
- Follow PEP 8
- Use type hints for function signatures
- Maximum line length: 88 characters (Black formatter)
- Add docstrings to all public functions

```python
def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate semantic similarity between two texts.

    Args:
        text1: First text for comparison
        text2: Second text for comparison

    Returns:
        Similarity score between 0 and 1
    """
    # Implementation
    pass
```

**Notebooks**:
- Clear all outputs before committing
- Add markdown cells explaining each section
- Include expected output examples
- Test with both OpenAI and Anthropic where applicable

### Documentation Style

**Markdown**:
- Use sentence case for headings
- Add blank lines around code blocks
- Link to related sections where relevant
- Use tables for comparisons

**LaTeX/Beamer**:
- 8pt font size
- Maximum 4 bullet points per slide
- No code on slides (reference notebooks instead)
- Include bottomnotes for key takeaways

### Commit Messages

Use conventional commit format:

```
type(scope): short description

Longer description if needed.

Closes #123
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code change that neither fixes nor adds
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(L05): add CrewAI multi-agent example

docs(glossary): add GraphRAG and HippoRAG terms

fix(L03): correct API key loading in notebook
```

### Pull Request Process

1. **Before submitting**:
   - Ensure your code runs without errors
   - Clear notebook outputs
   - Update relevant documentation
   - Add tests if applicable

2. **PR Description**:
   - Reference the issue it addresses
   - Describe what changed and why
   - List any breaking changes
   - Include screenshots for UI changes

3. **Review process**:
   - Address reviewer feedback promptly
   - Keep discussions focused on the code
   - Be patient - reviews may take a few days

## Content Types

### Adding a New Notebook

1. Create in the appropriate week folder: `LXX_Topic_Name/notebooks/`
2. Follow naming convention: `LXX_notebook_name.ipynb`
3. Include Colab badge at the top:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/LXX_Topic_Name/notebooks/LXX_notebook_name.ipynb)
```

4. Structure sections with clear markdown headers
5. Add error handling for API calls

### Adding a Chart

1. Create folder: `LXX_Topic_Name/chart_name/`
2. Add `chart.py` that generates `chart.pdf`
3. Use consistent color palette:

```python
MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
```

4. figsize: (10, 6)
5. Minimum font size: 10pt

### Adding a Glossary Term

Edit `docs/_data/glossary.yml`:

```yaml
- term: "Your Term"
  definition: "Clear, concise definition."
  related: ["Related Term 1", "Related Term 2"]
  week: 5
```

### Adding a Paper

Edit `docs/papers.md`:

1. Add to appropriate section
2. Include full citation with DOI or arXiv link
3. Verify link works

## Quality Checklist

Before submitting, verify:

- [ ] Code runs without errors
- [ ] Notebook outputs cleared
- [ ] No API keys or secrets committed
- [ ] LaTeX compiles with zero overflow warnings
- [ ] Links and references are valid
- [ ] Spelling and grammar checked
- [ ] Consistent with existing style

## Accessibility Checklist

When adding content:

- [ ] Images have alt text
- [ ] Tables have header rows
- [ ] Links are descriptive (not "click here")
- [ ] Code blocks have language specified
- [ ] Color is not the only indicator

## Recognition

Contributors are recognized in:

- GitHub Contributors page
- Course acknowledgments section
- Release notes for significant contributions

## Questions?

- **Technical issues**: [GitHub Issues](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/issues)
- **General questions**: [GitHub Discussions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions)
- **Private matters**: Email the instructor

---

*Thank you for helping improve this course for everyone!*
