"""
Agent Research Timeline
Week 12 - Research Frontiers
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

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
    5, 5.7, "Agent Research Timeline", fontsize=24, fontweight="bold", ha="center", color=MLPURPLE
)

# Timeline
ax.axhline(y=3.0, xmin=0.05, xmax=0.95, color=MLGRAY, linewidth=2)

# Milestones
milestones = [
    (1.0, "2022", "ReAct", MLPURPLE),
    (2.5, "2023", "AutoGPT\nToolformer", MLBLUE),
    (4.2, "2023", "Voyager\nMetaGPT", MLORANGE),
    (5.8, "2024", "Devin\nSWE-agent", MLGREEN),
    (7.5, "2024", "Claude CC\nAgentBench", MLPURPLE),
    (9.0, "2025+", "Research\nFrontier", MLBLUE),
]

for x, year, name, color in milestones:
    ax.plot(x, 3.0, "o", markersize=15, color=color, zorder=5)
    ax.text(x, 2.4, year, fontsize=11, ha="center", color=color, fontweight="bold")
    ax.text(x, 3.7, name, fontsize=10, ha="center", color=MLGRAY)

# Arrow
ax.annotate(
    "", xy=(9.5, 3.0), xytext=(0.5, 3.0), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)

# Key themes below
ax.text(
    5,
    1.0,
    "Themes: Reasoning > Tool Use > Multi-Agent > Production",
    fontsize=12,
    ha="center",
    color=MLPURPLE,
    fontweight="bold",
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "research_timeline.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'research_timeline.pdf'}")
