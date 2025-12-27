---
layout: default
title: FAQ
nav_order: 7
---

# Frequently Asked Questions

## Course Logistics

<details open>
<summary><strong>Who is this course for?</strong></summary>
<p>This is a PhD-level course designed for doctoral students and researchers interested in building autonomous AI systems. It's also suitable for advanced Master's students and industry practitioners with strong programming skills.</p>
</details>

<details>
<summary><strong>What are the prerequisites?</strong></summary>
<ul>
<li>Strong Python programming skills</li>
<li>Familiarity with machine learning concepts</li>
<li>Basic understanding of transformer architectures</li>
<li>Ability to read and understand research papers</li>
</ul>
</details>

<details>
<summary><strong>How much does API access cost?</strong></summary>
<p>Most exercises can be completed with $10-20 of API credits. Both OpenAI and Anthropic offer free credits for new accounts. We also use gpt-4o-mini which is very cost-effective.</p>
</details>

<details>
<summary><strong>Can I audit the course?</strong></summary>
<p>All materials are freely available online. You can follow along with lectures and notebooks at your own pace. For official credit, you must be enrolled at the institution.</p>
</details>

## Technical Setup

<details>
<summary><strong>What Python version do I need?</strong></summary>
<p>Python 3.11 or higher is recommended. Some features may work with Python 3.10, but 3.11+ is preferred for best compatibility.</p>
</details>

<details>
<summary><strong>Do I need a GPU?</strong></summary>
<p>No, all exercises use API-based models. A standard laptop is sufficient. For local model experiments (optional), a GPU would be helpful but not required.</p>
</details>

<details>
<summary><strong>Can I use Anthropic instead of OpenAI?</strong></summary>
<p>Yes! Most notebooks support both providers. Claude models work well for agent tasks. Check the specific notebook for provider options.</p>
</details>

<details>
<summary><strong>How do I set up my API keys?</strong></summary>
<p>Create a <code>.env</code> file in the project root with:</p>
<pre><code>OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here</code></pre>
<p>Never commit this file to version control!</p>
</details>

## Course Content

<details>
<summary><strong>What's the difference between an agent and a chatbot?</strong></summary>
<p>A chatbot responds to queries in a single turn. An agent can take multiple actions, use tools, maintain state across interactions, and pursue goals autonomously. Agents have a reasoning loop while chatbots are typically stateless.</p>
</details>

<details>
<summary><strong>Why do we need agent frameworks?</strong></summary>
<p>Frameworks like LangGraph handle common patterns: state management, error handling, tool orchestration, and multi-step workflows. They save development time and provide tested abstractions.</p>
</details>

<details>
<summary><strong>How do I prevent my agent from hallucinating?</strong></summary>
<p>See Week 9 for detailed techniques. Key strategies include: grounding responses in retrieved facts, using verification loops, implementing claim checking, and expressing uncertainty appropriately.</p>
</details>

<details>
<summary><strong>Which agent framework should I use?</strong></summary>
<p>It depends on your needs:</p>
<ul>
<li><strong>LangGraph</strong>: Best for complex, stateful workflows</li>
<li><strong>CrewAI</strong>: Best for role-based team collaboration</li>
<li><strong>AutoGen</strong>: Best for conversational multi-agent systems</li>
<li><strong>Plain Python</strong>: Best for learning and simple agents</li>
</ul>
</details>

## Assignments

<details>
<summary><strong>Can I use LLM assistants for assignments?</strong></summary>
<p>Yes, but you must disclose their use. The goal is learning - using an LLM to write all your code defeats the purpose. Use them for debugging, explanation, and exploration.</p>
</details>

<details>
<summary><strong>How are assignments graded?</strong></summary>
<p>Assignments are evaluated on:</p>
<ul>
<li>Correctness of implementation</li>
<li>Code quality and documentation</li>
<li>Understanding demonstrated in comments/reports</li>
<li>Creativity in extensions (bonus)</li>
</ul>
</details>

<details>
<summary><strong>Can I collaborate with others?</strong></summary>
<p>Discussion is encouraged, but submissions must be individual. Pair programming on understanding is fine; copying code is not.</p>
</details>

## Research

<details>
<summary><strong>What are good research directions in agentic AI?</strong></summary>
<p>Hot topics include:</p>
<ul>
<li>Long-horizon planning with uncertainty</li>
<li>Grounded world models for agents</li>
<li>Agent safety and alignment</li>
<li>Efficient tool learning</li>
<li>Multi-agent coordination at scale</li>
<li>Evaluation methodologies</li>
</ul>
</details>

<details>
<summary><strong>How do I find a research topic?</strong></summary>
<ol>
<li>Read recent papers from top venues (NeurIPS, ICML, ACL)</li>
<li>Identify limitations mentioned in papers</li>
<li>Look for gaps between theory and practice</li>
<li>Consider applications in your domain</li>
<li>Discuss with the instructor</li>
</ol>
</details>

## Getting Help

<details>
<summary><strong>Where can I ask questions?</strong></summary>
<ul>
<li><strong>Technical issues</strong>: <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/issues">GitHub Issues</a></li>
<li><strong>Course questions</strong>: <a href="https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions">GitHub Discussions</a></li>
<li><strong>Private matters</strong>: Email the instructor</li>
</ul>
</details>

<details>
<summary><strong>I'm stuck on a notebook. What should I do?</strong></summary>
<ol>
<li>Read the error message carefully</li>
<li>Check the troubleshooting section in Getting Started</li>
<li>Search for similar issues on GitHub</li>
<li>Post on GitHub Discussions with code and error</li>
<li>Attend office hours</li>
</ol>
</details>

---

*Don't see your question? Ask on [GitHub Discussions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/discussions)!*
