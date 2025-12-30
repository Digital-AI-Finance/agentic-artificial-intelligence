"""
Agent Orchestration Patterns
Week 6 - Agent Frameworks and Tools
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
MLGRAY = "#7F7F7F"

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(
    5, 5.7, "Orchestration Patterns", fontsize=24, fontweight="bold", ha="center", color=MLPURPLE
)

# Pattern 1: Sequential
ax.text(2.5, 4.8, "Sequential", fontsize=14, ha="center", fontweight="bold", color=MLPURPLE)
seq_nodes = [(1.0, 4.0), (2.0, 4.0), (3.0, 4.0), (4.0, 4.0)]
for i, (x, y) in enumerate(seq_nodes):
    circle = Circle((x, y), 0.3, facecolor="white", edgecolor=MLPURPLE, linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, str(i + 1), fontsize=12, ha="center", va="center", color=MLPURPLE)
    if i < len(seq_nodes) - 1:
        ax.annotate(
            "",
            xy=(x + 0.7, y),
            xytext=(x + 0.3, y),
            arrowprops=dict(arrowstyle="->", color=MLPURPLE, lw=1.5),
        )

# Pattern 2: Parallel
ax.text(7.5, 4.8, "Parallel", fontsize=14, ha="center", fontweight="bold", color=MLBLUE)
ax.add_patch(Circle((6.0, 4.0), 0.3, facecolor="white", edgecolor=MLBLUE, linewidth=2))
ax.text(6.0, 4.0, "S", fontsize=12, ha="center", va="center", color=MLBLUE)
for i, y_off in enumerate([-0.6, 0, 0.6]):
    ax.add_patch(Circle((7.5, 4.0 + y_off), 0.25, facecolor="white", edgecolor=MLBLUE, linewidth=2))
    ax.annotate(
        "",
        xy=(7.25, 4.0 + y_off),
        xytext=(6.3, 4.0),
        arrowprops=dict(arrowstyle="->", color=MLBLUE, lw=1),
    )
    ax.annotate(
        "",
        xy=(8.7, 4.0),
        xytext=(7.75, 4.0 + y_off),
        arrowprops=dict(arrowstyle="->", color=MLBLUE, lw=1),
    )
ax.add_patch(Circle((9.0, 4.0), 0.3, facecolor="white", edgecolor=MLBLUE, linewidth=2))
ax.text(9.0, 4.0, "E", fontsize=12, ha="center", va="center", color=MLBLUE)

# Pattern 3: Router
ax.text(2.5, 2.3, "Router", fontsize=14, ha="center", fontweight="bold", color=MLORANGE)
ax.add_patch(Circle((1.5, 1.5), 0.35, facecolor="white", edgecolor=MLORANGE, linewidth=2))
ax.text(1.5, 1.5, "R", fontsize=12, ha="center", va="center", color=MLORANGE, fontweight="bold")
for i, (x, y) in enumerate([(3.0, 2.2), (3.0, 1.5), (3.0, 0.8)]):
    ax.add_patch(Circle((x, y), 0.25, facecolor="white", edgecolor=MLORANGE, linewidth=2))
    ax.annotate(
        "",
        xy=(x - 0.25, y),
        xytext=(1.85, 1.5),
        arrowprops=dict(arrowstyle="->", color=MLORANGE, lw=1),
    )

# Pattern 4: Hierarchical
ax.text(7.5, 2.3, "Hierarchical", fontsize=14, ha="center", fontweight="bold", color=MLGREEN)
ax.add_patch(Circle((7.5, 1.8), 0.35, facecolor="white", edgecolor=MLGREEN, linewidth=2))
ax.text(7.5, 1.8, "M", fontsize=12, ha="center", va="center", color=MLGREEN, fontweight="bold")
for i, x in enumerate([6.3, 7.5, 8.7]):
    ax.add_patch(Circle((x, 0.8), 0.25, facecolor="white", edgecolor=MLGREEN, linewidth=2))
    ax.text(x, 0.8, "W", fontsize=10, ha="center", va="center", color=MLGREEN)
    ax.annotate(
        "", xy=(x, 1.05), xytext=(7.5, 1.45), arrowprops=dict(arrowstyle="->", color=MLGREEN, lw=1)
    )

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
