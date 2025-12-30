"""
RAG Evolution Timeline
Week 7 - Advanced RAG
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

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
    5, 5.7, "Evolution of RAG Systems", fontsize=24, fontweight="bold", ha="center", color=MLPURPLE
)

# Timeline
ax.axhline(y=3.0, xmin=0.05, xmax=0.95, color=MLGRAY, linewidth=2)

# Evolution stages
stages = [
    (1.5, "Naive RAG", "2020", MLPURPLE, ["Simple retrieval", "Top-k docs", "No refinement"]),
    (4.0, "Advanced RAG", "2023", MLBLUE, ["Query rewrite", "Reranking", "Hybrid search"]),
    (
        6.5,
        "Self-RAG",
        "2024",
        MLORANGE,
        ["Self-reflection", "Adaptive retrieval", "Critique tokens"],
    ),
    (9.0, "Agentic RAG", "2024+", MLGREEN, ["Multi-step", "Tool integration", "Planning"]),
]

for x, name, year, color, features in stages:
    # Node on timeline
    ax.plot(x, 3.0, "o", markersize=20, color=color, zorder=5)
    ax.text(
        x, 3.0, year[:2], fontsize=10, ha="center", va="center", color="white", fontweight="bold"
    )

    # Label above
    ax.text(x, 3.6, name, fontsize=13, ha="center", fontweight="bold", color=color)

    # Features below
    for i, feat in enumerate(features):
        ax.text(x, 2.4 - i * 0.4, feat, fontsize=10, ha="center", color=MLGRAY)

# Arrow showing progression
ax.annotate(
    "", xy=(9.3, 3.0), xytext=(1.2, 3.0), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)

# Capability indicator
ax.text(1.5, 0.8, "Low", fontsize=12, ha="center", color=MLPURPLE)
ax.text(9.0, 0.8, "High", fontsize=12, ha="center", color=MLGREEN)
ax.text(
    5.25, 0.5, "Capability & Complexity", fontsize=11, ha="center", color=MLGRAY, style="italic"
)
ax.annotate(
    "", xy=(8.5, 0.8), xytext=(2.0, 0.8), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "rag_evolution.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'rag_evolution.pdf'}")
