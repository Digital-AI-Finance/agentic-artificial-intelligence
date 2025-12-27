---
layout: default
title: Glossary
nav_order: 6
---

# Glossary

A comprehensive glossary of terms used in agentic AI.

<input type="text" id="glossary-search" placeholder="Search terms..." style="width: 100%; padding: 0.75rem; border: 1px solid #ddd; border-radius: 4px; margin-bottom: 1.5rem; font-size: 1rem;">

<div id="glossary-list">
{% assign sorted_terms = site.data.glossary | sort: "term" %}
{% for item in sorted_terms %}
<div class="glossary-item" data-term="{{ item.term | downcase }}">
  <h3 id="{{ item.term | slugify }}">{{ item.term }}</h3>
  <p>{{ item.definition }}</p>
  {% if item.related.size > 0 %}
  <p class="related-terms">
    <strong>Related:</strong>
    {% for related in item.related %}
    <a href="#{{ related | slugify }}">{{ related }}</a>{% unless forloop.last %}, {% endunless %}
    {% endfor %}
  </p>
  {% endif %}
  <p class="week-reference">
    <a href="{{ '/weeks/week-' | append: item.week | relative_url }}">Week {{ item.week }}</a>
  </p>
</div>
{% endfor %}
</div>

<style>
.glossary-item {
  padding: 1rem;
  margin-bottom: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #3333B2;
}

.glossary-item h3 {
  margin-top: 0;
  color: #3333B2;
}

.glossary-item p {
  margin-bottom: 0.5rem;
}

.related-terms a {
  display: inline-block;
  margin-right: 0.5rem;
  padding: 0.15rem 0.5rem;
  background: #e9ecef;
  border-radius: 4px;
  font-size: 0.85rem;
  text-decoration: none;
}

.related-terms a:hover {
  background: #3333B2;
  color: white;
}

.week-reference {
  font-size: 0.85rem;
  color: #666;
}

.hidden {
  display: none;
}
</style>

<script>
document.getElementById('glossary-search').addEventListener('input', function(e) {
  const searchTerm = e.target.value.toLowerCase();
  const items = document.querySelectorAll('.glossary-item');

  items.forEach(function(item) {
    const term = item.getAttribute('data-term');
    const text = item.textContent.toLowerCase();

    if (term.includes(searchTerm) || text.includes(searchTerm)) {
      item.classList.remove('hidden');
    } else {
      item.classList.add('hidden');
    }
  });
});
</script>
