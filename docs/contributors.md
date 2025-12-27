---
layout: default
title: Contributors
nav_order: 15
---

# Contributors

This course is made possible by the contributions of many individuals. Thank you to everyone who has helped improve this material!

## Course Team

<div class="contributor-grid">
<div class="contributor-card contributor-lead">
<div class="contributor-avatar">JO</div>
<h3>Prof. Dr. Joerg Osterrieder</h3>
<p class="contributor-role">Course Creator & Lead Instructor</p>
<p class="contributor-affiliation">FHGR - University of Applied Sciences of the Grisons</p>
<div class="contributor-links">
<a href="https://github.com/osterried">GitHub</a>
<a href="https://orcid.org/0000-0003-3497-4574">ORCID</a>
</div>
</div>
</div>

## GitHub Contributors

Thanks to everyone who has contributed code, documentation, or bug fixes:

<div id="github-contributors" class="contributor-grid">
<p>Loading contributors...</p>
</div>

<script>
fetch('https://api.github.com/repos/Digital-AI-Finance/agentic-artificial-intelligence/contributors')
  .then(response => response.json())
  .then(contributors => {
    const container = document.getElementById('github-contributors');
    if (contributors.length === 0 || contributors.message) {
      container.innerHTML = '<p>Be the first to contribute!</p>';
      return;
    }
    container.innerHTML = contributors.map(c => `
      <div class="contributor-card">
        <img src="${c.avatar_url}" alt="${c.login}" class="contributor-avatar-img">
        <h4><a href="${c.html_url}">${c.login}</a></h4>
        <p class="contributor-stats">${c.contributions} contribution${c.contributions > 1 ? 's' : ''}</p>
      </div>
    `).join('');
  })
  .catch(err => {
    document.getElementById('github-contributors').innerHTML =
      '<p>Could not load contributors. <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/graphs/contributors">View on GitHub</a></p>';
  });
</script>

## Special Thanks

### Research Advisors

We thank the following researchers for their insights and feedback:

| Name | Affiliation | Contribution |
|:-----|:------------|:-------------|
| *To be added* | - | - |

### Institutions

- **FHGR** - Hosting and institutional support
- **Digital AI Finance** - Research group coordination

### Open Source Projects

This course builds upon many excellent open-source projects:

| Project | Use in Course |
|:--------|:--------------|
| [LangChain](https://github.com/langchain-ai/langchain) | Agent framework foundations |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful agent workflows |
| [CrewAI](https://github.com/joaomdmoura/crewAI) | Multi-agent collaboration |
| [AutoGen](https://github.com/microsoft/autogen) | Conversational agents |
| [ChromaDB](https://github.com/chroma-core/chroma) | Vector storage |
| [OpenAI](https://github.com/openai/openai-python) | API client |
| [Anthropic](https://github.com/anthropics/anthropic-sdk-python) | API client |

### Funding

*Research funding acknowledgments will be added here.*

## How to Get Recognized

Contributions are recognized automatically through GitHub:

1. **Code contributions**: PRs that get merged
2. **Documentation**: Fixing typos, improving explanations
3. **Issues**: Reporting bugs, suggesting improvements
4. **Discussions**: Helping other students

See the [Contributing Guide]({{ '/contributing' | relative_url }}) to get started.

---

<div style="text-align: center; margin-top: 2rem;">
  <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence" class="btn btn-primary">
    Contribute on GitHub
  </a>
</div>

<style>
.contributor-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.contributor-card {
  background: var(--bg-secondary, #f8f9fa);
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  border: 1px solid var(--border-color, #ddd);
}

.contributor-lead {
  grid-column: 1 / -1;
  max-width: 400px;
  margin: 0 auto;
  border-left: 4px solid #3333B2;
}

.contributor-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3333B2, #0066CC);
  color: white;
  font-size: 2rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
}

.contributor-avatar-img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin-bottom: 0.5rem;
}

.contributor-card h3,
.contributor-card h4 {
  margin: 0.5rem 0;
  color: #3333B2;
}

.contributor-role {
  font-weight: 500;
  color: var(--text-secondary, #666);
  margin-bottom: 0.25rem;
}

.contributor-affiliation {
  font-size: 0.9rem;
  color: var(--text-muted, #999);
}

.contributor-links {
  margin-top: 1rem;
}

.contributor-links a {
  display: inline-block;
  margin: 0 0.5rem;
  font-size: 0.85rem;
}

.contributor-stats {
  font-size: 0.85rem;
  color: var(--text-muted, #999);
}
</style>
