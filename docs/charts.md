---
layout: default
title: Chart Gallery
nav_order: 23
---

# Chart Gallery

Browse all 48 course visualizations. Each chart is a standalone Python-generated PDF that can be downloaded or viewed.

<div class="chart-controls">
  <div class="filter-group">
    <label for="week-filter">Filter by Week:</label>
    <select id="week-filter" onchange="filterCharts()">
      <option value="all">All Weeks</option>
      {% for week in site.data.charts %}
      <option value="{{ week.week }}">Week {{ week.week }}: {{ week.title }}</option>
      {% endfor %}
    </select>
  </div>
  <div class="filter-group">
    <label for="type-filter">Filter by Type:</label>
    <select id="type-filter" onchange="filterCharts()">
      <option value="all">All Types</option>
      <option value="diagram">Diagrams</option>
      <option value="flowchart">Flowcharts</option>
      <option value="comparison">Comparisons</option>
      <option value="architecture">Architectures</option>
      <option value="timeline">Timelines</option>
      <option value="plot">Plots</option>
      <option value="network">Networks</option>
      <option value="radar">Radar Charts</option>
      <option value="taxonomy">Taxonomies</option>
    </select>
  </div>
  <div class="filter-group">
    <label for="search-filter">Search:</label>
    <input type="text" id="search-filter" placeholder="Search charts..." oninput="filterCharts()">
  </div>
</div>

<div class="chart-count">
  Showing <span id="visible-count">48</span> of 48 charts
</div>

---

{% for week in site.data.charts %}
## Week {{ week.week }}: {{ week.title }}

<div class="chart-grid" data-week="{{ week.week }}">
{% for chart in week.charts %}
<div class="chart-card" data-week="{{ week.week }}" data-type="{{ chart.type }}" data-name="{{ chart.name | downcase }}" data-description="{{ chart.description | downcase }}" data-topics="{{ chart.topics | join: ' ' }}">
  <div class="chart-preview">
    <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/{{ week.folder }}/{{ chart.id }}/chart.pdf" target="_blank" title="View PDF">
      <div class="chart-placeholder">
        <span class="chart-icon">{{ chart.type | slice: 0 | upcase }}</span>
      </div>
    </a>
  </div>
  <div class="chart-info">
    <h4>{{ chart.name }}</h4>
    <p class="chart-description">{{ chart.description }}</p>
    <div class="chart-meta">
      <span class="chart-type">{{ chart.type }}</span>
      <span class="chart-week">Week {{ week.week }}</span>
    </div>
    <div class="chart-actions">
      <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/raw/main/{{ week.folder }}/{{ chart.id }}/chart.pdf" class="btn-download" title="Download PDF">
        PDF
      </a>
      <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/blob/main/{{ week.folder }}/{{ chart.id }}/chart.py" class="btn-source" title="View Source">
        Source
      </a>
    </div>
  </div>
</div>
{% endfor %}
</div>

{% unless forloop.last %}
---
{% endunless %}
{% endfor %}

---

## Using These Charts

### In Presentations

All charts are designed for Beamer slides at 0.55-0.65 textwidth:

```latex
\includegraphics[width=0.55\textwidth]{01_chart_name/chart.pdf}
```

### Regenerating Charts

Each chart has a standalone Python script:

```bash
# Run single chart
python L01_Introduction_Agentic_AI/01_agent_definition/chart.py

# Regenerate all charts
for f in L*/*/chart.py; do python "$f"; done
```

### Chart Specifications

| Property | Value |
|----------|-------|
| Figure Size | (10, 6) |
| DPI | 300 (print quality) |
| Font Size | 14pt base (scaled for 70% display) |
| Colors | MLPURPLE=#3333B2, MLBLUE=#0066CC, MLORANGE=#FF7F0E |

---

<style>
.chart-controls {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
  padding: 1rem;
  background: var(--bg-secondary, #f8f9fa);
  border-radius: 8px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.filter-group label {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-muted, #666);
}

.filter-group select,
.filter-group input {
  padding: 0.5rem;
  border: 1px solid var(--border-color, #ddd);
  border-radius: 4px;
  font-size: 0.9rem;
  min-width: 180px;
}

.chart-count {
  font-size: 0.9rem;
  color: var(--text-muted, #666);
  margin-bottom: 1rem;
}

.chart-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.chart-card {
  background: var(--bg-secondary, #f8f9fa);
  border: 1px solid var(--border-color, #ddd);
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.chart-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.chart-card.hidden {
  display: none;
}

.chart-preview {
  background: #fff;
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 120px;
  border-bottom: 1px solid var(--border-color, #ddd);
}

.chart-placeholder {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3333B2 0%, #0066CC 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.chart-icon {
  font-size: 2rem;
  font-weight: bold;
  color: white;
}

.chart-info {
  padding: 1rem;
}

.chart-info h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
  color: var(--text-primary, #333);
}

.chart-description {
  font-size: 0.85rem;
  color: var(--text-muted, #666);
  margin: 0 0 0.75rem 0;
  line-height: 1.4;
}

.chart-meta {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.chart-type,
.chart-week {
  font-size: 0.75rem;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  background: var(--bg-tertiary, #e9ecef);
  color: var(--text-muted, #666);
}

.chart-type {
  background: #3333B2;
  color: white;
}

.chart-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-download,
.btn-source {
  flex: 1;
  padding: 0.5rem;
  text-align: center;
  font-size: 0.8rem;
  font-weight: 500;
  text-decoration: none;
  border-radius: 4px;
  transition: background 0.2s;
}

.btn-download {
  background: #0066CC;
  color: white;
}

.btn-download:hover {
  background: #0052a3;
}

.btn-source {
  background: var(--bg-tertiary, #e9ecef);
  color: var(--text-primary, #333);
}

.btn-source:hover {
  background: var(--border-color, #ddd);
}

@media (max-width: 600px) {
  .chart-controls {
    flex-direction: column;
  }

  .filter-group select,
  .filter-group input {
    width: 100%;
  }

  .chart-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<script>
function filterCharts() {
  const weekFilter = document.getElementById('week-filter').value;
  const typeFilter = document.getElementById('type-filter').value;
  const searchFilter = document.getElementById('search-filter').value.toLowerCase();

  const cards = document.querySelectorAll('.chart-card');
  let visibleCount = 0;

  cards.forEach(card => {
    const week = card.dataset.week;
    const type = card.dataset.type;
    const name = card.dataset.name;
    const description = card.dataset.description;
    const topics = card.dataset.topics;

    const matchesWeek = weekFilter === 'all' || week === weekFilter;
    const matchesType = typeFilter === 'all' || type === typeFilter;
    const matchesSearch = searchFilter === '' ||
      name.includes(searchFilter) ||
      description.includes(searchFilter) ||
      topics.includes(searchFilter);

    if (matchesWeek && matchesType && matchesSearch) {
      card.classList.remove('hidden');
      visibleCount++;
    } else {
      card.classList.add('hidden');
    }
  });

  document.getElementById('visible-count').textContent = visibleCount;

  // Show/hide week sections based on visible cards
  document.querySelectorAll('.chart-grid').forEach(grid => {
    const visibleCards = grid.querySelectorAll('.chart-card:not(.hidden)');
    const weekHeader = grid.previousElementSibling;
    if (weekHeader && weekHeader.tagName === 'H2') {
      weekHeader.style.display = visibleCards.length > 0 ? '' : 'none';
    }
  });
}
</script>
