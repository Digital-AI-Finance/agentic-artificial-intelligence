"""
CRAG (Corrective RAG) Architecture
Week 7 - Advanced RAG
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

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
MLRED = "#D62728"
MLGRAY = "#7F7F7F"

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(
    5,
    5.7,
    "CRAG: Corrective RAG Architecture",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Main flow
components = [
    (1.2, 3.5, "Query", MLPURPLE),
    (3.0, 3.5, "Retriever", MLBLUE),
    (5.0, 3.5, "Evaluator", MLORANGE),
    (8.0, 3.5, "Generator", MLGREEN),
]

for x, y, name, color in components:
    box = FancyBboxPatch(
        (x - 0.7, y - 0.4),
        1.4,
        0.8,
        boxstyle="round,pad=0.05",
        facecolor="white",
        edgecolor=color,
        linewidth=2.5,
    )
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=13, ha="center", va="center", fontweight="bold", color=color)

# Main arrows
ax.annotate(
    "", xy=(2.3, 3.5), xytext=(1.9, 3.5), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)
ax.annotate(
    "", xy=(4.3, 3.5), xytext=(3.7, 3.5), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)

# Three evaluation outcomes
outcomes = [
    (5.0, 4.8, "Correct", MLGREEN, (6.5, 4.5), "Use docs"),
    (5.0, 3.5, "Ambiguous", MLORANGE, (6.5, 3.5), "Refine"),
    (5.0, 2.2, "Incorrect", MLRED, (6.5, 2.5), "Web search"),
]

for x, y, label, color, (tx, ty), action in outcomes:
    ax.annotate(
        "", xy=(tx, ty), xytext=(5.7, y), arrowprops=dict(arrowstyle="->", color=color, lw=1.5)
    )
    ax.text(tx, ty, action, fontsize=10, ha="left", color=color)

# Merge to generator
ax.annotate(
    "", xy=(7.3, 3.5), xytext=(7.0, 4.3), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)
ax.annotate(
    "", xy=(7.3, 3.5), xytext=(7.0, 3.5), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)
ax.annotate(
    "", xy=(7.3, 3.5), xytext=(7.0, 2.7), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)

# Web search box
web_box = FancyBboxPatch(
    (5.8, 1.6),
    1.4,
    0.6,
    boxstyle="round,pad=0.05",
    facecolor="#FFF0E0",
    edgecolor=MLRED,
    linewidth=1.5,
    linestyle="--",
)
ax.add_patch(web_box)
ax.text(6.5, 1.9, "Web", fontsize=11, ha="center", color=MLRED)

# Evaluation scores
ax.text(5.0, 1.0, "Confidence Scores:", fontsize=11, fontweight="bold", color=MLGRAY)
ax.text(
    5.0,
    0.6,
    "Correct > 0.7 | Ambiguous 0.3-0.7 | Incorrect < 0.3",
    fontsize=10,
    ha="center",
    color=MLGRAY,
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
