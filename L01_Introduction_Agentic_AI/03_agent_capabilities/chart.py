"""
Agent Capabilities Radar Chart
Week 1 - Introduction to Agentic AI
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 22,
        "ytick.labelsize": 22,
        "legend.fontsize": 22,
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.family": "sans-serif",
    }
)

MLPURPLE = "#3333B2"
MLBLUE = "#0066CC"
MLORANGE = "#FF7F0E"

categories = ["Perception", "Reasoning", "Planning", "Action", "Learning", "Communication"]
N = len(categories)

# Agent types comparison
llm_values = [0.3, 0.8, 0.4, 0.2, 0.1, 0.9]
react_agent = [0.5, 0.85, 0.7, 0.8, 0.3, 0.85]
full_agent = [0.9, 0.9, 0.9, 0.95, 0.7, 0.9]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

for values, label, color in [
    (llm_values, "Base LLM", MLPURPLE),
    (react_agent, "ReAct Agent", MLBLUE),
    (full_agent, "Full Agent", MLORANGE),
]:
    values = values + values[:1]
    ax.plot(angles, values, "o-", linewidth=3, label=label, color=color)
    ax.fill(angles, values, alpha=0.15, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=18)
ax.set_ylim(0, 1)
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(["0.25", "0.5", "0.75", "1.0"], size=16)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0), fontsize=18)
ax.set_title("Agent Capabilities Comparison", size=24, fontweight="bold", color=MLPURPLE, pad=20)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
