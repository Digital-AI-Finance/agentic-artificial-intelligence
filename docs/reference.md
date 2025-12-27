---
layout: default
title: Quick Reference
nav_order: 26
---

# Quick Reference Cards

Printable one-page summaries for each week. Use Ctrl+P to print individual sections.

<style>
@media print {
  .no-print, nav, header, footer, .site-nav { display: none !important; }
  .ref-card { page-break-after: always; }
}
.ref-card {
  background: #fff;
  border: 2px solid #3333B2;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem 0;
}
.ref-card h3 { margin-top: 0; color: #3333B2; border-bottom: 2px solid #3333B2; padding-bottom: 0.5rem; }
.ref-card h4 { color: #0066CC; margin: 1rem 0 0.5rem 0; }
.ref-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
.ref-box { background: #f8f9fa; padding: 0.75rem; border-radius: 4px; }
.ref-box h5 { margin: 0 0 0.5rem 0; color: #333; }
.ref-box ul { margin: 0; padding-left: 1.2rem; font-size: 0.9rem; }
</style>

<div class="no-print" style="margin-bottom: 1rem;">
  <button onclick="window.print()" class="btn btn-primary">Print All Cards</button>
  <a href="#week-1" class="btn btn-outline">Jump to Week...</a>
</div>

---

<div class="ref-card" id="week-1">
<h3>Week 1: Introduction to Agentic AI</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Key Concepts</h5>
<ul>
<li>Agent = perceive + reason + act</li>
<li>ReAct = Reasoning + Acting</li>
<li>Trajectory = (s, a, o) sequence</li>
</ul>
</div>

<div class="ref-box">
<h5>ReAct Loop</h5>
<ul>
<li>Thought: reasoning step</li>
<li>Action: tool/API call</li>
<li>Observation: result</li>
</ul>
</div>

<div class="ref-box">
<h5>Key Papers</h5>
<ul>
<li>ReAct (Yao et al., 2023)</li>
<li>Agent Survey (Wang, 2024)</li>
</ul>
</div>

<div class="ref-box">
<h5>Code Pattern</h5>
<ul>
<li>while not done:</li>
<li>&nbsp;&nbsp;thought = think(obs)</li>
<li>&nbsp;&nbsp;action = act(thought)</li>
<li>&nbsp;&nbsp;obs = env.step(action)</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-2">
<h3>Week 2: LLM Foundations</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Prompting Strategies</h5>
<ul>
<li>Zero-shot: no examples</li>
<li>Few-shot: with examples</li>
<li>CoT: step-by-step</li>
</ul>
</div>

<div class="ref-box">
<h5>Chain-of-Thought</h5>
<ul>
<li>"Let's think step by step"</li>
<li>Emergent in 100B+ models</li>
<li>Best for math/logic</li>
</ul>
</div>

<div class="ref-box">
<h5>Advanced Methods</h5>
<ul>
<li>Self-Consistency: majority vote</li>
<li>ToT: tree exploration</li>
<li>Self-Ask: sub-questions</li>
</ul>
</div>

<div class="ref-box">
<h5>Trade-offs</h5>
<ul>
<li>CoT: +accuracy, +tokens</li>
<li>SC: +robust, +cost</li>
<li>ToT: +complex, +latency</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-3">
<h3>Week 3: Tool Use</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Function Calling</h5>
<ul>
<li>Define JSON schema</li>
<li>Model generates call</li>
<li>Execute and return</li>
</ul>
</div>

<div class="ref-box">
<h5>MCP Protocol</h5>
<ul>
<li>Tools: functions to call</li>
<li>Resources: data to read</li>
<li>Prompts: templates</li>
</ul>
</div>

<div class="ref-box">
<h5>Tool Design</h5>
<ul>
<li>Clear, specific names</li>
<li>Typed parameters</li>
<li>Detailed descriptions</li>
</ul>
</div>

<div class="ref-box">
<h5>Key Papers</h5>
<ul>
<li>Toolformer (Schick, 2023)</li>
<li>Gorilla (Patil, 2023)</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-4">
<h3>Week 4: Planning & Reasoning</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Reflexion</h5>
<ul>
<li>Actor: generates actions</li>
<li>Evaluator: success signal</li>
<li>Self-Reflect: verbal feedback</li>
</ul>
</div>

<div class="ref-box">
<h5>Memory Types</h5>
<ul>
<li>Short-term: current task</li>
<li>Long-term: persistent</li>
<li>Episodic: experiences</li>
</ul>
</div>

<div class="ref-box">
<h5>LATS</h5>
<ul>
<li>Tree search over actions</li>
<li>MCTS for exploration</li>
<li>Best path selection</li>
</ul>
</div>

<div class="ref-box">
<h5>Plan-and-Solve</h5>
<ul>
<li>1. Decompose problem</li>
<li>2. Plan subtasks</li>
<li>3. Execute each</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-5">
<h3>Week 5: Multi-Agent Systems</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Topologies</h5>
<ul>
<li>Hub-and-spoke: central</li>
<li>Mesh: peer-to-peer</li>
<li>Hierarchical: layers</li>
</ul>
</div>

<div class="ref-box">
<h5>Agent Roles</h5>
<ul>
<li>Orchestrator: coordinates</li>
<li>Specialist: domain expert</li>
<li>Critic: reviews output</li>
</ul>
</div>

<div class="ref-box">
<h5>Communication</h5>
<ul>
<li>Message passing</li>
<li>Shared blackboard</li>
<li>Structured protocols</li>
</ul>
</div>

<div class="ref-box">
<h5>Frameworks</h5>
<ul>
<li>AutoGen: conversational</li>
<li>MetaGPT: structured</li>
<li>CrewAI: role-based</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-6">
<h3>Week 6: Agent Frameworks</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>LangGraph</h5>
<ul>
<li>StateGraph: state machine</li>
<li>Nodes: functions</li>
<li>Edges: transitions</li>
<li>Checkpointing: save state</li>
</ul>
</div>

<div class="ref-box">
<h5>AutoGen</h5>
<ul>
<li>ConversableAgent</li>
<li>GroupChat patterns</li>
<li>Code execution</li>
</ul>
</div>

<div class="ref-box">
<h5>CrewAI</h5>
<ul>
<li>Role: agent identity</li>
<li>Goal: objective</li>
<li>Backstory: context</li>
</ul>
</div>

<div class="ref-box">
<h5>Selection Criteria</h5>
<ul>
<li>State needs?</li>
<li>Multi-agent?</li>
<li>Production ready?</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-7">
<h3>Week 7: Advanced RAG</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Self-RAG</h5>
<ul>
<li>Reflection tokens</li>
<li>Retrieve: yes/no</li>
<li>Relevance: check</li>
<li>Support: verify</li>
</ul>
</div>

<div class="ref-box">
<h5>CRAG</h5>
<ul>
<li>Correct: use docs</li>
<li>Incorrect: web search</li>
<li>Ambiguous: refine</li>
</ul>
</div>

<div class="ref-box">
<h5>RAPTOR</h5>
<ul>
<li>Hierarchical summaries</li>
<li>Tree structure</li>
<li>Multi-level retrieval</li>
</ul>
</div>

<div class="ref-box">
<h5>Query Enhancement</h5>
<ul>
<li>Decomposition</li>
<li>Expansion</li>
<li>Rewriting</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-8">
<h3>Week 8: GraphRAG</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Components</h5>
<ul>
<li>Entity extraction</li>
<li>Relationship detection</li>
<li>Graph construction</li>
</ul>
</div>

<div class="ref-box">
<h5>Search Types</h5>
<ul>
<li>Local: specific entities</li>
<li>Global: community themes</li>
</ul>
</div>

<div class="ref-box">
<h5>Community Detection</h5>
<ul>
<li>Cluster entities</li>
<li>Summarize clusters</li>
<li>Hierarchical index</li>
</ul>
</div>

<div class="ref-box">
<h5>HippoRAG</h5>
<ul>
<li>Hippocampus-inspired</li>
<li>Pattern separation</li>
<li>Associative retrieval</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-9">
<h3>Week 9: Hallucination Prevention</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Hallucination Types</h5>
<ul>
<li>Intrinsic: contradicts input</li>
<li>Extrinsic: unsupported</li>
<li>Factual: wrong facts</li>
</ul>
</div>

<div class="ref-box">
<h5>CoVe Pipeline</h5>
<ul>
<li>1. Generate response</li>
<li>2. Generate questions</li>
<li>3. Answer independently</li>
<li>4. Revise if needed</li>
</ul>
</div>

<div class="ref-box">
<h5>FActScore</h5>
<ul>
<li>Decompose to atoms</li>
<li>Verify each claim</li>
<li>Calculate precision</li>
</ul>
</div>

<div class="ref-box">
<h5>Mitigation</h5>
<ul>
<li>Retrieval grounding</li>
<li>Confidence calibration</li>
<li>Self-consistency</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-10">
<h3>Week 10: Agent Evaluation</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Benchmarks</h5>
<ul>
<li>AgentBench: 8 envs</li>
<li>SWE-bench: GitHub</li>
<li>WebArena: web tasks</li>
<li>GAIA: general AI</li>
</ul>
</div>

<div class="ref-box">
<h5>Metrics</h5>
<ul>
<li>Success rate</li>
<li>Pass@k</li>
<li>Task completion %</li>
</ul>
</div>

<div class="ref-box">
<h5>LLM-as-Judge</h5>
<ul>
<li>Automated scoring</li>
<li>Pairwise comparison</li>
<li>Rubric-based</li>
</ul>
</div>

<div class="ref-box">
<h5>Challenges</h5>
<ul>
<li>Contamination</li>
<li>Generalization</li>
<li>Cost</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-11">
<h3>Week 11: Domain Applications</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Code Agents</h5>
<ul>
<li>Devin: autonomous</li>
<li>AlphaCodium: flow</li>
<li>Sandboxing critical</li>
</ul>
</div>

<div class="ref-box">
<h5>Finance Agents</h5>
<ul>
<li>SEC compliance</li>
<li>Audit logging</li>
<li>Risk controls</li>
</ul>
</div>

<div class="ref-box">
<h5>Healthcare Agents</h5>
<ul>
<li>HIPAA compliance</li>
<li>Evidence-based</li>
<li>Human oversight</li>
</ul>
</div>

<div class="ref-box">
<h5>Safety Patterns</h5>
<ul>
<li>Sandboxing</li>
<li>Rate limiting</li>
<li>Approval gates</li>
</ul>
</div>
</div>
</div>

---

<div class="ref-card" id="week-12">
<h3>Week 12: Research Frontiers</h3>

<div class="ref-grid">
<div class="ref-box">
<h5>Generative Agents</h5>
<ul>
<li>Memory stream</li>
<li>Reflection</li>
<li>Planning</li>
<li>Emergent behavior</li>
</ul>
</div>

<div class="ref-box">
<h5>Voyager</h5>
<ul>
<li>Skill library</li>
<li>Curriculum learning</li>
<li>Open-ended exploration</li>
</ul>
</div>

<div class="ref-box">
<h5>Open Problems</h5>
<ul>
<li>Long-horizon planning</li>
<li>Grounded world models</li>
<li>Safe autonomy</li>
</ul>
</div>

<div class="ref-box">
<h5>Constitutional AI</h5>
<ul>
<li>Principle-based</li>
<li>Self-improvement</li>
<li>AI feedback</li>
</ul>
</div>
</div>
</div>
