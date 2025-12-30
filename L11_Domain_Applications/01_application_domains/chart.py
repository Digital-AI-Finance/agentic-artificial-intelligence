"""
Agent Application Domains
Week 11 - Domain Applications
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
    5, 5.7, "Agent Application Domains", fontsize=24, fontweight="bold", ha="center", color=MLPURPLE
)

# Domain circles with size indicating maturity
domains = [
    (2.0, 3.5, 1.2, "Software\nDev", MLPURPLE, "High"),
    (5.0, 4.2, 1.0, "Customer\nSupport", MLBLUE, "High"),
    (8.0, 3.5, 0.9, "Data\nAnalysis", MLORANGE, "Medium"),
    (3.0, 1.5, 0.8, "Healthcare", MLGREEN, "Emerging"),
    (5.5, 1.8, 0.85, "Finance", MLORANGE, "Medium"),
    (7.5, 1.3, 0.7, "Legal", MLBLUE, "Early"),
]

for x, y, size, name, color, maturity in domains:
    circle = Circle((x, y), size, facecolor="white", edgecolor=color, linewidth=3, alpha=0.9)
    ax.add_patch(circle)
    ax.text(x, y, name, fontsize=12, ha="center", va="center", fontweight="bold", color=color)
    ax.text(x, y - size - 0.2, maturity, fontsize=9, ha="center", color=MLGRAY)

# Maturity legend
ax.text(0.3, 0.5, "Size = Maturity", fontsize=11, color=MLGRAY, style="italic")

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
