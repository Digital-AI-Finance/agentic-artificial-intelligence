"""
Agent Framework Feature Comparison
Week 6 - Agent Frameworks and Tools
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 18,
        "ytick.labelsize": 22,
        "legend.fontsize": 16,
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.family": "sans-serif",
    }
)

MLPURPLE = "#3333B2"
MLBLUE = "#0066CC"
MLORANGE = "#FF7F0E"
MLGREEN = "#2CA02C"
MLRED = "#D62728"

# Framework comparison (radar chart)
categories = [
    "Ease of Use",
    "Flexibility",
    "Multi-Agent",
    "Tool Support",
    "State Mgmt",
    "Production",
]
N = len(categories)

# Scores (0-1 scale)
langchain = [0.9, 0.7, 0.6, 0.95, 0.7, 0.8]
langgraph = [0.7, 0.95, 0.9, 0.9, 0.95, 0.85]
autogen = [0.6, 0.8, 0.95, 0.75, 0.7, 0.7]
crewai = [0.85, 0.6, 0.85, 0.7, 0.6, 0.65]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

for values, label, color in [
    (langchain, "LangChain", MLPURPLE),
    (langgraph, "LangGraph", MLBLUE),
    (autogen, "AutoGen", MLORANGE),
    (crewai, "CrewAI", MLGREEN),
]:
    values = values + values[:1]
    ax.plot(angles, values, "o-", linewidth=3, label=label, color=color)
    ax.fill(angles, values, alpha=0.1, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=16)
ax.set_ylim(0, 1)
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(["0.25", "0.5", "0.75", "1.0"], size=14)
ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.0), fontsize=16)
ax.set_title("Agent Framework Comparison", size=24, fontweight="bold", color=MLPURPLE, pad=20)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "framework_comparison.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'framework_comparison.pdf'}")
