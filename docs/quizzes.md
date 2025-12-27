---
layout: default
title: Quizzes
nav_order: 19
---

# Concept Quizzes

Test your understanding of key course concepts with interactive quizzes.

{: .note }
> These quizzes are for self-assessment. Your answers are saved locally in your browser.

<div class="quiz-progress" style="background: var(--bg-secondary, #f8f9fa); padding: 1rem; border-radius: 8px; margin-bottom: 2rem;">
  <h3 style="margin-top: 0;">Your Progress</h3>
  <div class="progress-bar" style="height: 24px; background: #e9ecef; border-radius: 4px; overflow: hidden; margin-bottom: 0.5rem;">
    <div id="overall-progress" style="height: 100%; background: linear-gradient(90deg, #2CA02C, #0066CC); width: 0%; transition: width 0.3s;"></div>
  </div>
  <p id="progress-text" style="margin: 0; text-align: center; font-weight: 500;">Loading progress...</p>
</div>

---

## Week 1: Introduction to Agentic AI

Test your understanding of agents, ReAct, and trajectories.

{% include quiz.html id="week1" questions=site.data.quizzes.week1 %}

---

## Week 2: LLM Foundations

Test your understanding of prompting strategies.

{% include quiz.html id="week2" questions=site.data.quizzes.week2 %}

---

## Week 3: Tool Use

Test your understanding of function calling and tool integration.

{% include quiz.html id="week3" questions=site.data.quizzes.week3 %}

---

## Week 4: Planning and Reasoning

Test your understanding of Reflexion, LATS, and agent memory.

{% include quiz.html id="week4" questions=site.data.quizzes.week4 %}

---

## Week 5: Multi-Agent Systems

Test your understanding of multi-agent architectures.

{% include quiz.html id="week5" questions=site.data.quizzes.week5 %}

---

## Week 6: Agent Frameworks

Test your understanding of LangGraph, AutoGen, and CrewAI.

{% include quiz.html id="week6" questions=site.data.quizzes.week6 %}

---

## Week 7: Advanced RAG

Test your understanding of Self-RAG, CRAG, and adaptive retrieval.

{% include quiz.html id="week7" questions=site.data.quizzes.week7 %}

---

## Week 8: GraphRAG and Knowledge

Test your understanding of knowledge graphs and graph-based retrieval.

{% include quiz.html id="week8" questions=site.data.quizzes.week8 %}

---

## Week 9: Hallucination Prevention

Test your understanding of verification and factual accuracy.

{% include quiz.html id="week9" questions=site.data.quizzes.week9 %}

---

## Week 10: Agent Evaluation

Test your understanding of benchmarks and evaluation methods.

{% include quiz.html id="week10" questions=site.data.quizzes.week10 %}

---

## Week 11: Domain Applications

Test your understanding of code agents, financial agents, and safety.

{% include quiz.html id="week11" questions=site.data.quizzes.week11 %}

---

## Week 12: Research Frontiers

Test your understanding of Generative Agents, Voyager, and future directions.

{% include quiz.html id="week12" questions=site.data.quizzes.week12 %}

---

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Calculate progress from localStorage
  const weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
  const totalQuestions = 55; // Total questions across all weeks
  let answeredCorrectly = 0;

  weeks.forEach(week => {
    const key = `quiz-week${week}-correct`;
    const correct = parseInt(localStorage.getItem(key) || '0');
    answeredCorrectly += correct;
  });

  const percentage = Math.round((answeredCorrectly / totalQuestions) * 100);

  document.getElementById('overall-progress').style.width = percentage + '%';
  document.getElementById('progress-text').textContent =
    `${answeredCorrectly} of ${totalQuestions} questions answered correctly (${percentage}%)`;

  // Update progress when quizzes are completed
  window.updateQuizProgress = function() {
    let answered = 0;
    weeks.forEach(week => {
      const key = `quiz-week${week}-correct`;
      answered += parseInt(localStorage.getItem(key) || '0');
    });
    const pct = Math.round((answered / totalQuestions) * 100);
    document.getElementById('overall-progress').style.width = pct + '%';
    document.getElementById('progress-text').textContent =
      `${answered} of ${totalQuestions} questions answered correctly (${pct}%)`;
  };
});
</script>

<div style="margin-top: 2rem; padding: 1rem; background: var(--bg-secondary, #f8f9fa); border-radius: 8px;">
  <h4 style="margin-top: 0;">Reset Progress</h4>
  <p>Clear all saved quiz answers and start fresh.</p>
  <button onclick="if(confirm('Reset all quiz progress?')){localStorage.clear(); location.reload();}" class="btn btn-outline" style="border-color: #dc3545; color: #dc3545;">
    Reset All Progress
  </button>
</div>
