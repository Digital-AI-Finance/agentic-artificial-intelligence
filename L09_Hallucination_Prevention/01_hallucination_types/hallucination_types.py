"""
Hallucination Types in LLM Agents
Week 9 - Hallucination Prevention
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
MLRED = "#D62728"
MLGRAY = "#7F7F7F"

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

ax.text(
    5,
    5.7,
    "Types of LLM Hallucinations",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Hallucination types
types = [
    (2.0, 4.0, "Factual", MLRED, ["Wrong facts", "Fabricated data", "False citations"]),
    (
        5.0,
        4.0,
        "Faithfulness",
        MLORANGE,
        ["Ignores context", "Contradicts source", "Adds unsupported"],
    ),
    (8.0, 4.0, "Instruction", MLBLUE, ["Wrong format", "Missed constraints", "Task drift"]),
]

for x, y, name, color, examples in types:
    # Main box
    box = FancyBboxPatch(
        (x - 1.3, y - 1.8),
        2.6,
        2.8,
        boxstyle="round,pad=0.05",
        facecolor="white",
        edgecolor=color,
        linewidth=2.5,
    )
    ax.add_patch(box)

    # Header
    header = FancyBboxPatch(
        (x - 1.3, y + 0.6),
        2.6,
        0.45,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor=color,
        edgecolor=color,
        linewidth=1,
    )
    ax.add_patch(header)
    ax.text(x, y + 0.82, name, fontsize=14, ha="center", fontweight="bold", color="white")

    # Examples
    for i, ex in enumerate(examples):
        ax.text(x, y + 0.1 - i * 0.5, ex, fontsize=11, ha="center", color=MLGRAY)

# Severity indicator
ax.text(2.0, 1.8, "High Risk", fontsize=11, ha="center", color=MLRED, fontweight="bold")
ax.text(5.0, 1.8, "Medium Risk", fontsize=11, ha="center", color=MLORANGE, fontweight="bold")
ax.text(8.0, 1.8, "Lower Risk", fontsize=11, ha="center", color=MLBLUE, fontweight="bold")

# Arrow
ax.annotate(
    "", xy=(8.5, 1.5), xytext=(1.5, 1.5), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)
ax.text(5.0, 1.2, "Detectability", fontsize=11, ha="center", color=MLGRAY, style="italic")

plt.tight_layout()
plt.savefig(Path(__file__).parent / "hallucination_types.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'hallucination_types.pdf'}")
