---
layout: default
title: Framework Comparison
nav_order: 25
---

# Agent Framework Comparison

Interactive comparison of popular agent frameworks. Click headers to sort, use filters to narrow results.

<div class="comparison-controls" style="margin-bottom: 1rem; display: flex; gap: 1rem; flex-wrap: wrap;">
  <input type="text" id="framework-search" placeholder="Search frameworks..." oninput="filterFrameworks()" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; min-width: 200px;">
  <select id="category-filter" onchange="filterFrameworks()" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
    <option value="">All Categories</option>
    <option value="single">Single Agent</option>
    <option value="multi">Multi-Agent</option>
    <option value="rag">RAG</option>
  </select>
</div>

<div class="table-responsive" style="overflow-x: auto;">
<table id="framework-table" class="sortable-table">
<thead>
<tr>
  <th onclick="sortTable(0)" style="cursor: pointer;">Framework <span class="sort-icon">↕</span></th>
  <th onclick="sortTable(1)" style="cursor: pointer;">Category <span class="sort-icon">↕</span></th>
  <th onclick="sortTable(2)" style="cursor: pointer;">Language <span class="sort-icon">↕</span></th>
  <th onclick="sortTable(3)" style="cursor: pointer;">State Mgmt <span class="sort-icon">↕</span></th>
  <th onclick="sortTable(4)" style="cursor: pointer;">Multi-Agent <span class="sort-icon">↕</span></th>
  <th onclick="sortTable(5)" style="cursor: pointer;">Learning Curve <span class="sort-icon">↕</span></th>
</tr>
</thead>
<tbody>
<tr data-category="single">
  <td><strong>LangGraph</strong></td>
  <td>Single Agent</td>
  <td>Python, JS</td>
  <td>Excellent</td>
  <td>Limited</td>
  <td>Medium</td>
</tr>
<tr data-category="multi">
  <td><strong>AutoGen</strong></td>
  <td>Multi-Agent</td>
  <td>Python</td>
  <td>Good</td>
  <td>Excellent</td>
  <td>Medium</td>
</tr>
<tr data-category="multi">
  <td><strong>CrewAI</strong></td>
  <td>Multi-Agent</td>
  <td>Python</td>
  <td>Basic</td>
  <td>Excellent</td>
  <td>Easy</td>
</tr>
<tr data-category="multi">
  <td><strong>MetaGPT</strong></td>
  <td>Multi-Agent</td>
  <td>Python</td>
  <td>Good</td>
  <td>Excellent</td>
  <td>Hard</td>
</tr>
<tr data-category="single">
  <td><strong>Semantic Kernel</strong></td>
  <td>Single Agent</td>
  <td>C#, Python</td>
  <td>Good</td>
  <td>Limited</td>
  <td>Medium</td>
</tr>
<tr data-category="rag">
  <td><strong>LlamaIndex</strong></td>
  <td>RAG</td>
  <td>Python</td>
  <td>Basic</td>
  <td>Limited</td>
  <td>Easy</td>
</tr>
<tr data-category="rag">
  <td><strong>Haystack</strong></td>
  <td>RAG</td>
  <td>Python</td>
  <td>Good</td>
  <td>Limited</td>
  <td>Medium</td>
</tr>
<tr data-category="single">
  <td><strong>TaskWeaver</strong></td>
  <td>Single Agent</td>
  <td>Python</td>
  <td>Good</td>
  <td>Limited</td>
  <td>Medium</td>
</tr>
</tbody>
</table>
</div>

<script>
let sortDirection = {};

function sortTable(columnIndex) {
  const table = document.getElementById('framework-table');
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));

  sortDirection[columnIndex] = !sortDirection[columnIndex];

  rows.sort((a, b) => {
    const aVal = a.cells[columnIndex].textContent.trim();
    const bVal = b.cells[columnIndex].textContent.trim();
    const result = aVal.localeCompare(bVal);
    return sortDirection[columnIndex] ? result : -result;
  });

  rows.forEach(row => tbody.appendChild(row));
}

function filterFrameworks() {
  const search = document.getElementById('framework-search').value.toLowerCase();
  const category = document.getElementById('category-filter').value;
  const rows = document.querySelectorAll('#framework-table tbody tr');

  rows.forEach(row => {
    const text = row.textContent.toLowerCase();
    const rowCategory = row.dataset.category;
    const matchesSearch = text.includes(search);
    const matchesCategory = !category || rowCategory === category;
    row.style.display = matchesSearch && matchesCategory ? '' : 'none';
  });
}
</script>

---

## RAG Strategy Comparison

| Strategy | When to Use | Pros | Cons |
|:---------|:------------|:-----|:-----|
| **Naive RAG** | Simple Q&A | Simple, fast | Limited accuracy |
| **Self-RAG** | Quality-critical | Self-correcting | Token overhead |
| **CRAG** | Noisy data | Robust | Extra retrieval |
| **GraphRAG** | Complex queries | Global context | Build time |
| **RAPTOR** | Hierarchical docs | Multi-level | Memory usage |

---

## Benchmark Comparison

| Benchmark | Focus | Tasks | Human Baseline |
|:----------|:------|:------|:---------------|
| **AgentBench** | General | 8 environments | Partial |
| **SWE-bench** | Coding | GitHub issues | Yes |
| **WebArena** | Web | 812 tasks | Yes |
| **GAIA** | General | 466 tasks | Yes |
| **OSWorld** | Desktop | 369 tasks | Yes |

---

## Selection Guide

### Choose LangGraph if:
- You need fine-grained control over agent flow
- State persistence and checkpointing are important
- You're building production systems

### Choose AutoGen if:
- Multi-agent collaboration is the focus
- You want conversation-based agents
- Code execution is needed

### Choose CrewAI if:
- You want role-based agent teams
- Quick prototyping is priority
- Simple setup is important

### Choose LlamaIndex if:
- RAG is your primary use case
- You need document processing
- Integration with vector stores is key
