"""
Agent Role Specialization Matrix
Week 5 - Multi-Agent Architectures
Shows different agent roles in a multi-agent system
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 22,
        "ytick.labelsize": 22,
        "legend.fontsize": 22,
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.family": "sans-serif",
    }
)

MLPURPLE = "#3333B2"
MLLAVENDER = "#ADADE0"
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
    5, 5.7, "Agent Role Specialization", fontsize=15, fontweight="bold", ha="center", color=MLPURPLE
)

# Role boxes
roles = [
    (
        "Orchestrator",
        1.5,
        4.0,
        MLPURPLE,
        ["Task routing", "Workflow control", "Result aggregation"],
    ),
    (
        "Planner",
        4.0,
        4.0,
        MLBLUE,
        ["Task decomposition", "Strategy selection", "Resource allocation"],
    ),
    ("Executor", 6.5, 4.0, MLGREEN, ["Tool invocation", "Code execution", "API calls"]),
    ("Critic", 2.75, 1.5, MLORANGE, ["Output validation", "Quality checks", "Error detection"]),
    ("Specialist", 5.25, 1.5, MLRED, ["Domain expertise", "Knowledge retrieval", "Custom skills"]),
]

for name, x, y, color, skills in roles:
    # Main box
    box = FancyBboxPatch(
        (x - 1.0, y - 1.2),
        2.0,
        2.0,
        boxstyle="round,pad=0.05",
        facecolor="white",
        edgecolor=color,
        linewidth=2,
    )
    ax.add_patch(box)

    # Header
    header = FancyBboxPatch(
        (x - 1.0, y + 0.4),
        2.0,
        0.45,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor=color,
        edgecolor=color,
        linewidth=1,
    )
    ax.add_patch(header)
    ax.text(x, y + 0.62, name, fontsize=10, ha="center", fontweight="bold", color="white")

    # Skills
    for i, skill in enumerate(skills):
        ax.text(x, y - 0.1 - i * 0.35, skill, fontsize=8, ha="center", color=MLGRAY)

# Arrows showing interactions
arrow_pairs = [
    (1.5, 3.8, 4.0, 3.8),  # Orchestrator -> Planner
    (4.0, 3.8, 6.5, 3.8),  # Planner -> Executor
    (6.5, 2.8, 5.25, 2.1),  # Executor -> Specialist
    (5.25, 2.1, 2.75, 2.1),  # Specialist -> Critic
    (2.75, 2.7, 1.5, 2.8),  # Critic -> Orchestrator
]

for x1, y1, x2, y2 in arrow_pairs:
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.2, connectionstyle="arc3,rad=0.1"),
    )

# Legend
ax.text(8.5, 5.3, "Workflow:", fontsize=9, color=MLGRAY, fontweight="bold")
ax.text(8.5, 4.9, "1. Orchestrator routes", fontsize=8, color=MLGRAY)
ax.text(8.5, 4.5, "2. Planner decomposes", fontsize=8, color=MLGRAY)
ax.text(8.5, 4.1, "3. Executor acts", fontsize=8, color=MLGRAY)
ax.text(8.5, 3.7, "4. Critic validates", fontsize=8, color=MLGRAY)
ax.text(8.5, 3.3, "5. Loop or complete", fontsize=8, color=MLGRAY)

plt.tight_layout()
plt.savefig(
    Path(__file__).parent / "role_specialization.pdf",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'role_specialization.pdf'}")
