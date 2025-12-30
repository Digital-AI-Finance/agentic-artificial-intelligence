"""
Function Calling API Comparison
Week 3 - Tool Use and Function Calling
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
    5,
    5.7,
    "Function Calling API Comparison",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Provider boxes
providers = [
    (
        "OpenAI",
        1.5,
        3.5,
        MLPURPLE,
        ["tools parameter", "JSON Schema", "Parallel calls", "Strict mode"],
    ),
    (
        "Anthropic",
        5.0,
        3.5,
        MLBLUE,
        ["tool_use blocks", "Input schema", "Sequential", "Prefill support"],
    ),
    (
        "Google",
        8.5,
        3.5,
        MLORANGE,
        ["function_calling", "OpenAPI spec", "Grounding", "Code execution"],
    ),
]

for name, x, y, color, features in providers:
    # Main box
    box = FancyBboxPatch(
        (x - 1.3, y - 2.0),
        2.6,
        3.2,
        boxstyle="round,pad=0.05",
        facecolor="white",
        edgecolor=color,
        linewidth=3,
    )
    ax.add_patch(box)

    # Header
    header = FancyBboxPatch(
        (x - 1.3, y + 0.8),
        2.6,
        0.45,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor=color,
        edgecolor=color,
        linewidth=1,
    )
    ax.add_patch(header)
    ax.text(x, y + 1.02, name, fontsize=16, ha="center", fontweight="bold", color="white")

    # Features
    for i, feat in enumerate(features):
        ax.text(x, y + 0.3 - i * 0.55, feat, fontsize=12, ha="center", color=MLGRAY)

# Common features arrow
ax.annotate(
    "", xy=(8.0, 1.0), xytext=(2.0, 1.0), arrowprops=dict(arrowstyle="<->", color=MLGREEN, lw=2)
)
ax.text(
    5,
    0.6,
    "All support: JSON schemas, streaming, error handling",
    fontsize=14,
    ha="center",
    color=MLGREEN,
    fontweight="bold",
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
