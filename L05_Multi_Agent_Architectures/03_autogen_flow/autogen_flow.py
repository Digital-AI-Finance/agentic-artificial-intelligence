"""
AutoGen Conversation Flow
Week 5 - Multi-Agent Architectures
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

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
    "AutoGen Conversation Pattern",
    fontsize=24,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Agents
agents = [
    (1.5, 4.0, "User\nProxy", MLPURPLE),
    (5.0, 4.0, "Assistant", MLBLUE),
    (8.5, 4.0, "Critic", MLORANGE),
]

for x, y, name, color in agents:
    box = FancyBboxPatch(
        (x - 0.9, y - 0.6),
        1.8,
        1.2,
        boxstyle="round,pad=0.05",
        facecolor="white",
        edgecolor=color,
        linewidth=3,
    )
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=14, ha="center", va="center", fontweight="bold", color=color)

# Conversation flow
messages = [
    (2.4, 4.3, 4.1, 4.3, "1. Task", MLPURPLE),
    (4.1, 3.9, 2.4, 3.9, "2. Plan", MLBLUE),
    (5.9, 4.3, 7.6, 4.3, "3. Review", MLBLUE),
    (7.6, 3.9, 5.9, 3.9, "4. Feedback", MLORANGE),
    (4.1, 3.5, 2.4, 3.5, "5. Result", MLBLUE),
]

for x1, y1, x2, y2, label, color in messages:
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=color, lw=2)
    )
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx, my + 0.25, label, fontsize=12, ha="center", color=color, fontweight="bold")

# Code execution box
code_box = FancyBboxPatch(
    (3.5, 1.2),
    3.0,
    1.4,
    boxstyle="round,pad=0.05",
    facecolor="#F5F5F5",
    edgecolor=MLGREEN,
    linewidth=2,
)
ax.add_patch(code_box)
ax.text(5.0, 1.9, "Code Executor", fontsize=14, ha="center", fontweight="bold", color=MLGREEN)
ax.text(5.0, 1.5, "Docker / Local / Jupyter", fontsize=11, ha="center", color=MLGRAY)

# Arrow from assistant to code
ax.annotate(
    "", xy=(5.0, 2.6), xytext=(5.0, 3.4), arrowprops=dict(arrowstyle="->", color=MLGREEN, lw=2)
)

# Legend
ax.text(0.5, 0.8, "Key Features:", fontsize=13, fontweight="bold", color=MLGRAY)
ax.text(
    0.5,
    0.4,
    "- Multi-turn conversations\n- Code execution\n- Human-in-loop",
    fontsize=11,
    color=MLGRAY,
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "autogen_flow.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'autogen_flow.pdf'}")
