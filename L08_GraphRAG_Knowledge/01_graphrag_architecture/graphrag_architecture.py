"""
GraphRAG Architecture Overview
Week 8 - GraphRAG and Knowledge
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
    "GraphRAG: Knowledge Graph + RAG",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Pipeline stages
stages = [
    (1.5, 3.5, "Documents", MLPURPLE),
    (3.5, 3.5, "Extract\nEntities", MLBLUE),
    (5.5, 3.5, "Build\nGraph", MLORANGE),
    (7.5, 3.5, "Community\nSummaries", MLGREEN),
]

for x, y, name, color in stages:
    box = FancyBboxPatch(
        (x - 0.8, y - 0.5),
        1.6,
        1.0,
        boxstyle="round,pad=0.05",
        facecolor="white",
        edgecolor=color,
        linewidth=2.5,
    )
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=12, ha="center", va="center", fontweight="bold", color=color)

# Arrows
for i in range(len(stages) - 1):
    x1 = stages[i][0] + 0.8
    x2 = stages[i + 1][0] - 0.8
    ax.annotate(
        "", xy=(x2, 3.5), xytext=(x1, 3.5), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
    )

# Knowledge graph visualization (simplified)
kg_center = (5.5, 1.5)
nodes = [(5.5, 1.5), (4.5, 1.8), (6.5, 1.8), (5.0, 0.9), (6.0, 0.9)]
for x, y in nodes:
    ax.plot(x, y, "o", markersize=12, color=MLORANGE, zorder=5)

# Edges
edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 3), (2, 4)]
for i, j in edges:
    ax.plot(
        [nodes[i][0], nodes[j][0]],
        [nodes[i][1], nodes[j][1]],
        "-",
        color=MLORANGE,
        alpha=0.5,
        linewidth=1.5,
    )

ax.text(5.5, 0.3, "Knowledge Graph", fontsize=12, ha="center", color=MLORANGE, fontweight="bold")

# Query path
ax.text(9.0, 2.5, "Query", fontsize=12, ha="center", color=MLPURPLE, fontweight="bold")
ax.annotate(
    "", xy=(7.8, 2.8), xytext=(9.0, 2.3), arrowprops=dict(arrowstyle="->", color=MLPURPLE, lw=1.5)
)
ax.annotate(
    "", xy=(9.0, 4.2), xytext=(8.2, 3.5), arrowprops=dict(arrowstyle="->", color=MLGREEN, lw=1.5)
)
ax.text(9.0, 4.5, "Answer", fontsize=12, ha="center", color=MLGREEN, fontweight="bold")

plt.tight_layout()
plt.savefig(Path(__file__).parent / "graphrag_architecture.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'graphrag_architecture.pdf'}")
