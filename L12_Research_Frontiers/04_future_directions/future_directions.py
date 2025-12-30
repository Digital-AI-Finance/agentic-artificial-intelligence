"""
Future Research Directions
Week 12 - Research Frontiers
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
    5,
    5.7,
    "Future Research Directions",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Near-term (1-2 years)
near_box = FancyBboxPatch(
    (0.5, 3.2),
    2.8,
    2.0,
    boxstyle="round,pad=0.05",
    facecolor="#E8EAF6",
    edgecolor=MLPURPLE,
    linewidth=2,
)
ax.add_patch(near_box)
ax.text(1.9, 4.9, "Near-term", fontsize=14, ha="center", fontweight="bold", color=MLPURPLE)
near_items = ["Better benchmarks", "Production tools", "Human-agent collab"]
for i, item in enumerate(near_items):
    ax.text(1.9, 4.4 - i * 0.4, item, fontsize=10, ha="center", color=MLGRAY)

# Mid-term (2-5 years)
mid_box = FancyBboxPatch(
    (3.6, 3.2),
    2.8,
    2.0,
    boxstyle="round,pad=0.05",
    facecolor="#E3F2FD",
    edgecolor=MLBLUE,
    linewidth=2,
)
ax.add_patch(mid_box)
ax.text(5.0, 4.9, "Mid-term", fontsize=14, ha="center", fontweight="bold", color=MLBLUE)
mid_items = ["World models", "Persistent learning", "Multi-agent systems"]
for i, item in enumerate(mid_items):
    ax.text(5.0, 4.4 - i * 0.4, item, fontsize=10, ha="center", color=MLGRAY)

# Long-term (5+ years)
long_box = FancyBboxPatch(
    (6.7, 3.2),
    2.8,
    2.0,
    boxstyle="round,pad=0.05",
    facecolor="#FFF3E0",
    edgecolor=MLORANGE,
    linewidth=2,
)
ax.add_patch(long_box)
ax.text(8.1, 4.9, "Long-term", fontsize=14, ha="center", fontweight="bold", color=MLORANGE)
long_items = ["Embodied agents", "General autonomy", "Agent societies"]
for i, item in enumerate(long_items):
    ax.text(8.1, 4.4 - i * 0.4, item, fontsize=10, ha="center", color=MLGRAY)

# Arrows
ax.annotate(
    "", xy=(3.4, 4.2), xytext=(3.0, 4.2), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)
ax.annotate(
    "", xy=(6.5, 4.2), xytext=(6.1, 4.2), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)

# Cross-cutting themes
ax.text(
    5,
    2.5,
    "Cross-cutting: Safety | Alignment | Interpretability | Evaluation",
    fontsize=12,
    ha="center",
    color=MLGREEN,
    fontweight="bold",
)

# Call to action
ax.text(
    5,
    1.5,
    "Key insight: Progress requires interdisciplinary collaboration",
    fontsize=11,
    ha="center",
    color=MLPURPLE,
    style="italic",
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "future_directions.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'future_directions.pdf'}")
