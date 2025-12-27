---
layout: default
title: Code Playground
nav_order: 24
---

# Python Code Playground

Run Python code directly in your browser using Pyodide. No installation required.

<div id="playground-loading" style="text-align: center; padding: 2rem;">
  Loading Python environment...
</div>

<div id="playground" style="display: none;">
  <div style="margin-bottom: 1rem;">
    <label for="example-select">Load Example:</label>
    <select id="example-select" onchange="loadExample(this.value)" style="padding: 0.5rem; margin-left: 0.5rem;">
      <option value="">-- Select Example --</option>
      <option value="react">ReAct Agent Loop</option>
      <option value="cot">Chain-of-Thought</option>
      <option value="tool">Tool Calling</option>
      <option value="memory">Memory System</option>
    </select>
  </div>

  <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 300px;">
      <h4>Code</h4>
      <textarea id="code-input" style="width: 100%; height: 300px; font-family: monospace; padding: 1rem; border: 1px solid #ddd; border-radius: 4px;">
# Welcome to the Agentic AI Code Playground!
# Try running some Python code

import random

class SimpleAgent:
    """A minimal agent implementation"""

    def __init__(self, name):
        self.name = name
        self.memory = []

    def think(self, observation):
        thought = f"Processing: {observation}"
        self.memory.append(thought)
        return thought

    def act(self, thought):
        actions = ["search", "calculate", "respond"]
        action = random.choice(actions)
        return f"Action: {action}"

    def run(self, task):
        print(f"Agent {self.name} starting task: {task}")
        thought = self.think(task)
        print(thought)
        action = self.act(thought)
        print(action)
        return action

# Create and run agent
agent = SimpleAgent("Demo")
result = agent.run("Analyze this data")
print(f"Result: {result}")
print(f"Memory: {agent.memory}")
      </textarea>
    </div>

    <div style="flex: 1; min-width: 300px;">
      <h4>Output</h4>
      <pre id="code-output" style="width: 100%; height: 300px; background: #1e1e1e; color: #fff; padding: 1rem; border-radius: 4px; overflow: auto; margin: 0;"></pre>
    </div>
  </div>

  <div style="margin-top: 1rem;">
    <button onclick="runCode()" class="btn btn-primary" id="run-btn">Run Code</button>
    <button onclick="clearOutput()" class="btn btn-outline">Clear Output</button>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
<script>
let pyodide = null;

async function initPyodide() {
  pyodide = await loadPyodide();
  document.getElementById('playground-loading').style.display = 'none';
  document.getElementById('playground').style.display = 'block';
}

async function runCode() {
  const code = document.getElementById('code-input').value;
  const output = document.getElementById('code-output');
  const btn = document.getElementById('run-btn');

  btn.disabled = true;
  btn.textContent = 'Running...';
  output.textContent = '';

  try {
    // Redirect stdout
    pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
    `);

    await pyodide.runPythonAsync(code);

    const stdout = pyodide.runPython('sys.stdout.getvalue()');
    output.textContent = stdout || '(No output)';
  } catch (err) {
    output.textContent = 'Error: ' + err.message;
    output.style.color = '#ff6b6b';
  }

  btn.disabled = false;
  btn.textContent = 'Run Code';
}

function clearOutput() {
  document.getElementById('code-output').textContent = '';
  document.getElementById('code-output').style.color = '#fff';
}

const examples = {
  react: `# ReAct Agent Pattern
class ReActAgent:
    def __init__(self):
        self.trajectory = []

    def think(self, observation):
        thought = f"Analyzing: {observation}"
        self.trajectory.append(("thought", thought))
        return thought

    def act(self, thought):
        action = "search[query]"
        self.trajectory.append(("action", action))
        return action

    def observe(self, action):
        observation = "Result from action"
        self.trajectory.append(("observation", observation))
        return observation

    def run(self, task, max_steps=3):
        obs = task
        for step in range(max_steps):
            print(f"Step {step + 1}")
            thought = self.think(obs)
            print(f"  Thought: {thought}")
            action = self.act(thought)
            print(f"  Action: {action}")
            obs = self.observe(action)
            print(f"  Observation: {obs}")
        return self.trajectory

agent = ReActAgent()
trajectory = agent.run("Find information about AI agents")
print(f"\\nTotal steps: {len(trajectory)}")`,

  cot: `# Chain-of-Thought Prompting Simulation
def chain_of_thought(problem):
    """Simulate CoT reasoning"""
    steps = []

    # Step 1: Understand the problem
    steps.append(f"1. Understanding: {problem}")

    # Step 2: Break down
    steps.append("2. Breaking down into sub-problems...")

    # Step 3: Solve each part
    steps.append("3. Solving step by step:")
    steps.append("   - First, identify key components")
    steps.append("   - Then, apply relevant knowledge")
    steps.append("   - Finally, combine results")

    # Step 4: Conclude
    steps.append("4. Conclusion: Problem solved!")

    return steps

problem = "How do agents use reasoning?"
result = chain_of_thought(problem)
for step in result:
    print(step)`,

  tool: `# Tool Calling Simulation
class Tool:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def call(self, *args):
        return self.func(*args)

# Define tools
calculator = Tool("calculator", lambda x, y: x + y)
searcher = Tool("search", lambda q: f"Results for: {q}")

class ToolAgent:
    def __init__(self, tools):
        self.tools = {t.name: t for t in tools}

    def use_tool(self, name, *args):
        if name in self.tools:
            result = self.tools[name].call(*args)
            print(f"Tool '{name}' returned: {result}")
            return result
        return None

agent = ToolAgent([calculator, searcher])
agent.use_tool("calculator", 5, 3)
agent.use_tool("search", "AI agents")`,

  memory: `# Agent Memory System
from collections import deque

class Memory:
    def __init__(self, capacity=5):
        self.short_term = deque(maxlen=capacity)
        self.long_term = []

    def add_short(self, item):
        self.short_term.append(item)
        print(f"Added to short-term: {item}")

    def consolidate(self):
        """Move important items to long-term"""
        if self.short_term:
            item = self.short_term[0]
            self.long_term.append(item)
            print(f"Consolidated to long-term: {item}")

    def recall(self, query):
        """Search memory"""
        results = [m for m in self.long_term if query.lower() in m.lower()]
        return results

memory = Memory(capacity=3)
memory.add_short("User asked about agents")
memory.add_short("Explained ReAct pattern")
memory.add_short("Discussed tool use")
memory.consolidate()
print(f"\\nLong-term memory: {memory.long_term}")
print(f"Short-term memory: {list(memory.short_term)}")`
};

function loadExample(name) {
  if (examples[name]) {
    document.getElementById('code-input').value = examples[name];
    clearOutput();
  }
}

initPyodide();
</script>

---

## About the Playground

This playground uses [Pyodide](https://pyodide.org/) to run Python directly in your browser via WebAssembly. Features:

- **No installation required** - runs entirely in browser
- **Standard Python** - numpy, scipy available
- **Safe execution** - sandboxed environment

### Limitations

- No network access from code
- Large libraries may take time to load
- Some Python features may not work (file I/O, etc.)

### Use Cases

- Experiment with agent patterns
- Test algorithm implementations
- Learn Python concepts interactively
