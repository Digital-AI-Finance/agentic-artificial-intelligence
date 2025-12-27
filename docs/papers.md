---
layout: default
title: Papers
nav_order: 5
---

# Research Papers

A curated collection of foundational and cutting-edge papers in agentic AI with summaries.

<div style="margin-bottom: 1.5rem;">
<input type="text" id="paper-search" placeholder="Search papers..." style="width: 100%; padding: 0.75rem; border: 1px solid var(--border-color, #ddd); border-radius: 8px; font-size: 1rem;">
</div>

## Key Papers with Summaries

<details open>
<summary><strong>ReAct: Synergizing Reasoning and Acting (Yao et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Interleave reasoning traces and actions in LLMs, allowing models to reason about tasks (Thought) and interact with external environments (Action) to gather information (Observation).</p>
<p><strong>Key Contribution</strong>: Shows that combining reasoning and acting outperforms either approach alone on question answering and decision making tasks.</p>
<p><strong>Why It Matters</strong>: Foundational paradigm for most modern LLM agents. The Thought-Action-Observation loop is now standard in agent frameworks.</p>
<p><a href="https://arxiv.org/abs/2210.03629">arXiv</a> | Week 1</p>
</div>
</details>

<details>
<summary><strong>Chain-of-Thought Prompting (Wei et al., 2022)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Adding "Let's think step by step" or providing reasoning examples dramatically improves LLM performance on complex reasoning tasks.</p>
<p><strong>Key Contribution</strong>: Demonstrates emergent reasoning abilities in large models when prompted to show intermediate steps.</p>
<p><strong>Why It Matters</strong>: Enables agents to break down complex problems and explain their reasoning, improving both accuracy and interpretability.</p>
<p><a href="https://arxiv.org/abs/2201.11903">arXiv</a> | Week 2</p>
</div>
</details>

<details>
<summary><strong>Toolformer (Schick et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Train LLMs to decide when and how to use external tools (calculators, search, etc.) by self-supervised learning on API calls.</p>
<p><strong>Key Contribution</strong>: Shows LLMs can learn tool use without explicit supervision by generating and filtering training data from successful tool calls.</p>
<p><strong>Why It Matters</strong>: Foundational work for function calling and tool-augmented LLMs used in modern APIs.</p>
<p><a href="https://arxiv.org/abs/2302.04761">arXiv</a> | Week 3</p>
</div>
</details>

<details>
<summary><strong>Reflexion (Shinn et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Agents learn from verbal self-reflection on failures, storing insights in episodic memory to avoid repeating mistakes.</p>
<p><strong>Key Contribution</strong>: Introduces a framework for agents to improve through natural language feedback rather than gradient updates.</p>
<p><strong>Why It Matters</strong>: Enables agents to learn from experience within a session, critical for complex multi-step tasks.</p>
<p><a href="https://arxiv.org/abs/2303.11366">arXiv</a> | Week 4</p>
</div>
</details>

<details>
<summary><strong>AutoGen (Wu et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Framework for building multi-agent systems through conversational interactions between specialized agents.</p>
<p><strong>Key Contribution</strong>: Demonstrates that complex tasks can be solved by having agents with different roles collaborate through natural conversation.</p>
<p><strong>Why It Matters</strong>: Pioneered the conversational multi-agent paradigm used in many modern agent frameworks.</p>
<p><a href="https://arxiv.org/abs/2308.08155">arXiv</a> | Week 5</p>
</div>
</details>

<details>
<summary><strong>Self-RAG (Asai et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Train LLMs to adaptively retrieve information and self-reflect on generated content using special tokens.</p>
<p><strong>Key Contribution</strong>: Shows models can learn when to retrieve, what to retrieve, and how to critique their outputs for factuality.</p>
<p><strong>Why It Matters</strong>: Improves RAG accuracy by making retrieval decisions dynamic rather than always-on.</p>
<p><a href="https://arxiv.org/abs/2310.11511">arXiv</a> | Week 7</p>
</div>
</details>

<details>
<summary><strong>GraphRAG (Edge et al., 2024)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Use knowledge graphs to structure document relationships, enabling community-based summarization and multi-hop reasoning.</p>
<p><strong>Key Contribution</strong>: Outperforms naive RAG on global sensemaking queries that require synthesizing information across documents.</p>
<p><strong>Why It Matters</strong>: Addresses RAG limitations for complex queries requiring broad understanding of a corpus.</p>
<p><a href="https://microsoft.github.io/graphrag/">Microsoft</a> | Week 8</p>
</div>
</details>

<details>
<summary><strong>Chain-of-Verification (Dhuliawala et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Reduce hallucinations by having the model generate verification questions, answer them independently, and revise based on inconsistencies.</p>
<p><strong>Key Contribution</strong>: Provides a systematic approach to fact-checking generated content without external knowledge bases.</p>
<p><strong>Why It Matters</strong>: Critical technique for building trustworthy agents that can verify their own claims.</p>
<p><a href="https://arxiv.org/abs/2309.11495">arXiv</a> | Week 9</p>
</div>
</details>

<details>
<summary><strong>AgentBench (Liu et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Comprehensive benchmark for evaluating LLMs as agents across 8 distinct environments (web, DB, OS, games, etc.).</p>
<p><strong>Key Contribution</strong>: First systematic evaluation framework for agent capabilities, revealing significant gaps between top models.</p>
<p><strong>Why It Matters</strong>: Enables standardized comparison of agent capabilities and identifies areas for improvement.</p>
<p><a href="https://arxiv.org/abs/2308.03688">arXiv</a> | Week 10</p>
</div>
</details>

<details>
<summary><strong>Generative Agents (Park et al., 2023)</strong></summary>
<div class="paper-summary">
<p><strong>Core Idea</strong>: Simulate believable human behavior in a sandbox environment using memory, reflection, and planning architectures.</p>
<p><strong>Key Contribution</strong>: Demonstrates emergent social behaviors from simple agent architectures, including information spreading and relationship formation.</p>
<p><strong>Why It Matters</strong>: Opens possibilities for agent-based simulations of complex social systems.</p>
<p><a href="https://arxiv.org/abs/2304.03442">arXiv</a> | Week 12</p>
</div>
</details>

---

## Complete Paper List

### Agent Architectures

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| ReAct: Synergizing Reasoning and Acting | Yao et al. | 2023 | [arXiv](https://arxiv.org/abs/2210.03629) | 1 |
| A Survey on LLM-based Autonomous Agents | Wang et al. | 2024 | [arXiv](https://arxiv.org/abs/2308.11432) | 1 |
| The Rise of LLM-Based Agents | Xi et al. | 2023 | [arXiv](https://arxiv.org/abs/2309.07864) | 1 |

### Reasoning and Prompting

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| Chain-of-Thought Prompting | Wei et al. | 2022 | [arXiv](https://arxiv.org/abs/2201.11903) | 2 |
| Tree of Thoughts | Yao et al. | 2023 | [arXiv](https://arxiv.org/abs/2305.10601) | 2 |
| Self-Consistency Improves CoT | Wang et al. | 2023 | [arXiv](https://arxiv.org/abs/2203.11171) | 2 |

### Tool Use

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| Toolformer | Schick et al. | 2023 | [arXiv](https://arxiv.org/abs/2302.04761) | 3 |
| Gorilla: LLM Connected with APIs | Patil et al. | 2023 | [arXiv](https://arxiv.org/abs/2305.15334) | 3 |
| ToolLLM | Qin et al. | 2024 | [arXiv](https://arxiv.org/abs/2307.16789) | 3 |

### Planning and Reflection

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| Reflexion | Shinn et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.11366) | 4 |
| LATS: Language Agent Tree Search | Zhou et al. | 2024 | [arXiv](https://arxiv.org/abs/2310.04406) | 4 |
| Plan-and-Solve Prompting | Wang et al. | 2023 | [arXiv](https://arxiv.org/abs/2305.04091) | 4 |

### Multi-Agent Systems

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| AutoGen | Wu et al. | 2023 | [arXiv](https://arxiv.org/abs/2308.08155) | 5 |
| MetaGPT | Hong et al. | 2023 | [arXiv](https://arxiv.org/abs/2308.00352) | 5 |
| ChatDev | Qian et al. | 2024 | [arXiv](https://arxiv.org/abs/2307.07924) | 5 |
| Multi-Agent Collaboration Survey | Tran et al. | 2025 | [arXiv](https://arxiv.org/abs/2501.06322) | 5 |

### Retrieval-Augmented Generation

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| Self-RAG | Asai et al. | 2023 | [arXiv](https://arxiv.org/abs/2310.11511) | 7 |
| Corrective RAG | Yan et al. | 2024 | [arXiv](https://arxiv.org/abs/2401.15884) | 7 |
| RAPTOR | Sarthi et al. | 2024 | [arXiv](https://arxiv.org/abs/2401.18059) | 7 |
| RAG Survey | Gao et al. | 2024 | [arXiv](https://arxiv.org/abs/2312.10997) | 7 |

### Knowledge Graphs

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| GraphRAG | Edge et al. | 2024 | [Microsoft](https://microsoft.github.io/graphrag/) | 8 |
| Graph of Thoughts | Besta et al. | 2024 | [arXiv](https://arxiv.org/abs/2308.09687) | 8 |
| HippoRAG | Gutierrez et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.14831) | 8 |

### Hallucination and Safety

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| Chain-of-Verification | Dhuliawala et al. | 2023 | [arXiv](https://arxiv.org/abs/2309.11495) | 9 |
| FActScore | Min et al. | 2023 | [arXiv](https://arxiv.org/abs/2305.14251) | 9 |
| Self-Refine | Madaan et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.17651) | 9 |
| Hallucination Survey | Ji et al. | 2023 | [arXiv](https://arxiv.org/abs/2202.03629) | 9 |

### Evaluation and Benchmarks

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| AgentBench | Liu et al. | 2023 | [arXiv](https://arxiv.org/abs/2308.03688) | 10 |
| WebArena | Zhou et al. | 2024 | [arXiv](https://arxiv.org/abs/2307.13854) | 10 |
| GAIA Benchmark | Mialon et al. | 2024 | [arXiv](https://arxiv.org/abs/2311.12983) | 10 |
| SWE-bench | Jimenez et al. | 2024 | [arXiv](https://arxiv.org/abs/2310.06770) | 10 |

### Domain Applications

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| AlphaCodium | Ridnik et al. | 2024 | [arXiv](https://arxiv.org/abs/2401.08500) | 11 |
| MDAgents | Kim et al. | 2024 | [arXiv](https://arxiv.org/abs/2404.15488) | 11 |
| FinAgent Survey | Li et al. | 2024 | [arXiv](https://arxiv.org/abs/2402.18485) | 11 |

### Research Frontiers

| Paper | Authors | Year | Link | Week |
|:------|:--------|:-----|:-----|:-----|
| Generative Agents | Park et al. | 2023 | [arXiv](https://arxiv.org/abs/2304.03442) | 12 |
| Voyager | Wang et al. | 2023 | [arXiv](https://arxiv.org/abs/2305.16291) | 12 |
| Constitutional AI | Bai et al. | 2022 | [arXiv](https://arxiv.org/abs/2212.08073) | 12 |

---

## Reference Management

### Zotero Collection

Import our curated paper collection directly into Zotero:

<div style="background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 8px; margin: 1rem 0;">
<p><strong>Agentic AI Course Papers</strong></p>
<p>A shared Zotero collection with all course readings, organized by week.</p>
<p><a href="https://www.zotero.org/groups/agentic-ai-course" class="btn btn-primary">View Zotero Collection</a></p>
<p style="font-size: 0.85rem; color: var(--text-muted, #999); margin-top: 0.5rem;">
Join the group to sync papers to your library and add notes.
</p>
</div>

### BibTeX Export

Download all citations in BibTeX format for your papers:

```
Coming soon - bibliography.bib file with all course papers
```

---

## Reading Tips

1. **Start with abstracts** - Get the main idea before deep diving
2. **Focus on methods** - Understanding the approach is more valuable than memorizing results
3. **Take notes** - Write summaries in your own words
4. **Discuss with peers** - Different perspectives help understanding
5. **Implement key ideas** - The best way to learn is by doing

## Citation Format

When citing papers in your work, use the following format:

```bibtex
@article{yao2023react,
  title={ReAct: Synergizing Reasoning and Acting in Language Models},
  author={Yao, Shunyu and others},
  journal={arXiv preprint arXiv:2210.03629},
  year={2023}
}
```

<style>
.paper-summary {
  padding: 1rem;
  background: var(--bg-secondary, #f8f9fa);
  border-left: 3px solid #3333B2;
  margin: 0.5rem 0;
}

.paper-summary p {
  margin: 0.5rem 0;
}

.paper-summary a {
  color: #0066CC;
}

details.hidden {
  display: none;
}

#paper-search {
  background: var(--bg-secondary, white);
  color: var(--text-primary, #1a1a2e);
}
</style>

<script>
document.getElementById('paper-search').addEventListener('input', function(e) {
  const searchTerm = e.target.value.toLowerCase();

  // Search in details summaries
  document.querySelectorAll('details').forEach(function(detail) {
    const text = detail.textContent.toLowerCase();
    if (text.includes(searchTerm) || searchTerm === '') {
      detail.classList.remove('hidden');
    } else {
      detail.classList.add('hidden');
    }
  });

  // Search in tables
  document.querySelectorAll('table tbody tr').forEach(function(row) {
    const text = row.textContent.toLowerCase();
    if (text.includes(searchTerm) || searchTerm === '') {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
});
</script>
