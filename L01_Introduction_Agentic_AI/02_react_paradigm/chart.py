"""
ReAct Paradigm Cycle Visualization
Week 1 - Introduction to Agentic AI
Visualizes the Thought -> Action -> Observation loop (Yao et al., 2023)
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch

# Chart settings for Beamer slides (scaled for 70% display)
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

# ML Course color palette
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

# Title
ax.text(
    5,
    5.7,
    "ReAct: Reasoning + Acting Paradigm",
    fontsize=16,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)
ax.text(5, 5.3, "(Yao et al., ICLR 2023)", fontsize=11, ha="center", color=MLGRAY, style="italic")

# ========== ReAct Cycle (circular layout) ==========
center_x, center_y = 3.5, 2.8
radius = 1.8

# Calculate positions for 3 nodes (Thought, Action, Observation)
angles = [90, 330, 210]  # degrees
positions = {}
labels = ["Thought", "Action", "Observation"]
colors = [MLBLUE, MLGREEN, MLORANGE]
descriptions = ["Reason about\ncurrent state", "Execute tool\nor API call", "Receive\nfeedback"]

for i, (label, angle, color, desc) in enumerate(zip(labels, angles, colors, descriptions)):
    rad = np.radians(angle)
    x = center_x + radius * np.cos(rad)
    y = center_y + radius * np.sin(rad)
    positions[label] = (x, y)

    # Draw node
    node = FancyBboxPatch(
        (x - 0.7, y - 0.4),
        1.4,
        0.8,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor="white",
        edgecolor=color,
        linewidth=2.5,
    )
    ax.add_patch(node)
    ax.text(x, y, label, fontsize=12, ha="center", va="center", fontweight="bold", color=color)

    # Add description below/beside each node
    if label == "Thought":
        ax.text(x, y + 0.7, desc, fontsize=9, ha="center", va="bottom", color=MLGRAY)
    elif label == "Action":
        ax.text(x + 0.9, y, desc, fontsize=9, ha="left", va="center", color=MLGRAY)
    else:  # Observation
        ax.text(x - 0.9, y, desc, fontsize=9, ha="right", va="center", color=MLGRAY)


# Draw arrows between nodes (curved)
def draw_curved_arrow(start, end, color, rad=0.3):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=2.5, connectionstyle=f"arc3,rad={rad}"),
    )


# Thought -> Action
draw_curved_arrow(
    (positions["Thought"][0] + 0.5, positions["Thought"][1] - 0.4),
    (positions["Action"][0] - 0.3, positions["Action"][1] + 0.4),
    MLPURPLE,
    0.2,
)

# Action -> Observation
draw_curved_arrow(
    (positions["Action"][0] - 0.7, positions["Action"][1] + 0.1),
    (positions["Observation"][0] + 0.7, positions["Observation"][1] + 0.1),
    MLPURPLE,
    0.2,
)

# Observation -> Thought
draw_curved_arrow(
    (positions["Observation"][0] + 0.3, positions["Observation"][1] + 0.4),
    (positions["Thought"][0] - 0.5, positions["Thought"][1] - 0.4),
    MLPURPLE,
    0.2,
)

# Center label
ax.text(
    center_x,
    center_y,
    "ReAct\nLoop",
    fontsize=11,
    ha="center",
    va="center",
    color=MLPURPLE,
    fontweight="bold",
)

# ========== Right side: Example trace ==========
example_x = 7.5
ax.text(
    example_x, 4.8, "Example Trace", fontsize=13, fontweight="bold", ha="center", color=MLPURPLE
)

# Trace box
trace_box = FancyBboxPatch(
    (5.8, 0.8),
    3.8,
    3.7,
    boxstyle="round,pad=0.05",
    facecolor="#F8F8F8",
    edgecolor=MLGRAY,
    linewidth=1,
)
ax.add_patch(trace_box)

# Example trace content
trace_items = [
    ("T1:", "I need to find the capital", MLBLUE),
    ("", "of France to answer this.", MLBLUE),
    ("A1:", "Search[capital of France]", MLGREEN),
    ("O1:", "Paris is the capital of", MLORANGE),
    ("", "France, located on Seine.", MLORANGE),
    ("T2:", "Paris is the answer.", MLBLUE),
    ("A2:", "Finish[Paris]", MLGREEN),
]

y_pos = 4.2
for prefix, text, color in trace_items:
    if prefix:
        ax.text(6.0, y_pos, prefix, fontsize=9, fontweight="bold", color=color, family="monospace")
    ax.text(
        6.5, y_pos, text, fontsize=9, color="black" if not prefix else color, family="monospace"
    )
    y_pos -= 0.45

# Legend at bottom
legend_y = 0.3
ax.text(1.5, legend_y, "T = Thought", fontsize=10, color=MLBLUE, fontweight="bold")
ax.text(4.0, legend_y, "A = Action", fontsize=10, color=MLGREEN, fontweight="bold")
ax.text(6.5, legend_y, "O = Observation", fontsize=10, color=MLORANGE, fontweight="bold")

plt.tight_layout()
plt.savefig(
    Path(__file__).parent / "chart.pdf",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)
plt.close()

print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
