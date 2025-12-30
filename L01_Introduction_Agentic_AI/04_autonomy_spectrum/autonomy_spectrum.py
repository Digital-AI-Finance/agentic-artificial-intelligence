"""
Autonomy Levels Spectrum
Week 1 - Introduction to Agentic AI
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

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis("off")

# Gradient bar
from matplotlib.colors import LinearSegmentedColormap

colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN]
cmap = LinearSegmentedColormap.from_list("autonomy", colors, N=100)

for i in range(100):
    ax.axvspan(
        0.5 + i * 0.09, 0.5 + (i + 1) * 0.09, ymin=0.4, ymax=0.6, color=cmap(i / 100), alpha=0.8
    )

# Level markers
levels = [
    (1.0, "Rule-Based", "Fixed rules\nNo learning", MLPURPLE),
    (3.5, "Assistive", "Suggests actions\nHuman decides", MLBLUE),
    (6.0, "Supervised", "Acts with\napproval", MLORANGE),
    (8.5, "Autonomous", "Full autonomy\nSelf-directed", MLGREEN),
]

for x, name, desc, color in levels:
    ax.plot([x, x], [1.5, 2.2], color=color, linewidth=3)
    ax.plot(x, 2.2, "o", color=color, markersize=15)
    ax.text(x, 2.6, name, ha="center", fontsize=18, fontweight="bold", color=color)
    ax.text(x, 0.8, desc, ha="center", fontsize=14, color=MLGRAY)

# Arrow
ax.annotate(
    "", xy=(9.3, 1.85), xytext=(0.7, 1.85), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)

ax.text(5, 3.5, "Autonomy Spectrum", fontsize=24, fontweight="bold", ha="center", color=MLPURPLE)
ax.text(0.5, 1.85, "Low", fontsize=16, ha="right", color=MLGRAY)
ax.text(9.5, 1.85, "High", fontsize=16, ha="left", color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "autonomy_spectrum.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'autonomy_spectrum.pdf'}")
