"""
LangGraph State Machine Flow
Week 6 - Agent Frameworks and Tools
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.family": "sans-serif",
    }
)

MLPURPLE = "#3333B2"
MLBLUE = "#0066CC"
MLORANGE = "#FF7F0E"
MLGREEN = "#2CA02C"
MLGRAY = "#7F7F7F"

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(
    5,
    5.7,
    "LangGraph: Graph-Based Agent Flow",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Nodes
nodes = [
    (1.5, 3.0, "START", MLGRAY, 0.5),
    (3.5, 4.5, "Agent", MLPURPLE, 0.7),
    (3.5, 1.5, "Tools", MLBLUE, 0.7),
    (6.5, 3.0, "Check", MLORANGE, 0.6),
    (8.5, 3.0, "END", MLGREEN, 0.5),
]

for x, y, name, color, radius in nodes:
    circle = Circle((x, y), radius, facecolor="white", edgecolor=color, linewidth=3)
    ax.add_patch(circle)
    ax.text(x, y, name, fontsize=14, ha="center", va="center", fontweight="bold", color=color)

# Edges with labels
edges = [
    (2.0, 3.0, 2.8, 4.2, "input", MLGRAY),
    (4.2, 4.5, 5.9, 3.3, "response", MLPURPLE),
    (3.5, 3.8, 3.5, 2.2, "call", MLPURPLE),
    (3.5, 2.2, 3.5, 3.8, "result", MLBLUE),
    (6.5, 2.4, 3.5, 1.5, "continue", MLORANGE),
    (7.1, 3.0, 8.0, 3.0, "done", MLGREEN),
]

for x1, y1, x2, y2, label, color in edges:
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color=color, lw=2, connectionstyle="arc3,rad=0.15"),
    )
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + 0.2
    ax.text(mx, my, label, fontsize=11, ha="center", color=color, style="italic")

# State box
state_box = FancyBboxPatch(
    (0.3, 0.2),
    2.5,
    1.0,
    boxstyle="round,pad=0.05",
    facecolor="#F5F5F5",
    edgecolor=MLPURPLE,
    linewidth=2,
    linestyle="--",
)
ax.add_patch(state_box)
ax.text(1.55, 0.7, "State: TypedDict", fontsize=12, ha="center", fontweight="bold", color=MLPURPLE)
ax.text(1.55, 0.4, "messages, context", fontsize=10, ha="center", color=MLGRAY)

# Key features
ax.text(7.5, 5.2, "Key Features:", fontsize=13, fontweight="bold", color=MLGRAY)
ax.text(7.5, 4.8, "- Cyclic graphs", fontsize=11, color=MLGRAY)
ax.text(7.5, 4.4, "- Checkpointing", fontsize=11, color=MLGRAY)
ax.text(7.5, 4.0, "- Human-in-loop", fontsize=11, color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "langgraph_flow.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'langgraph_flow.pdf'}")
