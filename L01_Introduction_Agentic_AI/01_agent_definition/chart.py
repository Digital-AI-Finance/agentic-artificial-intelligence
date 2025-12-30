"""
Agent vs LLM Comparison Chart
Week 1 - Introduction to Agentic AI
Visualizes the key differences between standard LLM inference and agentic behavior
"""

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

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
    "LLM vs Agent: Architectural Comparison",
    fontsize=16,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# ========== LEFT SIDE: Standard LLM ==========
# Box for LLM
llm_box = FancyBboxPatch(
    (0.3, 1.5),
    4,
    3.5,
    boxstyle="round,pad=0.05,rounding_size=0.2",
    facecolor=MLLAVENDER,
    edgecolor=MLPURPLE,
    linewidth=2,
)
ax.add_patch(llm_box)
ax.text(2.3, 4.7, "Standard LLM", fontsize=14, fontweight="bold", ha="center", color=MLPURPLE)

# LLM components
ax.text(2.3, 4.0, "Input", fontsize=11, ha="center", color="black")
ax.annotate(
    "", xy=(2.3, 3.4), xytext=(2.3, 3.8), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)

# LLM core
llm_core = FancyBboxPatch(
    (1.0, 2.4),
    2.6,
    0.9,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLBLUE,
    linewidth=2,
)
ax.add_patch(llm_core)
ax.text(2.3, 2.85, "LLM Model", fontsize=11, ha="center", fontweight="bold", color=MLBLUE)

ax.annotate(
    "", xy=(2.3, 2.0), xytext=(2.3, 2.4), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)
ax.text(2.3, 1.7, "Output", fontsize=11, ha="center", color="black")

# Characteristics
ax.text(0.5, 0.9, "Single-turn", fontsize=10, color=MLGRAY)
ax.text(0.5, 0.5, "No memory", fontsize=10, color=MLGRAY)
ax.text(2.5, 0.9, "No tools", fontsize=10, color=MLGRAY)
ax.text(2.5, 0.5, "Reactive only", fontsize=10, color=MLGRAY)

# ========== RIGHT SIDE: Agent ==========
# Box for Agent
agent_box = FancyBboxPatch(
    (5.5, 0.3),
    4.2,
    4.7,
    boxstyle="round,pad=0.05,rounding_size=0.2",
    facecolor="#E8F4E8",
    edgecolor=MLGREEN,
    linewidth=2,
)
ax.add_patch(agent_box)
ax.text(7.6, 4.7, "LLM Agent", fontsize=14, fontweight="bold", ha="center", color=MLGREEN)

# Agent components - Perception
percept_box = FancyBboxPatch(
    (5.8, 3.8),
    1.5,
    0.6,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLORANGE,
    linewidth=1.5,
)
ax.add_patch(percept_box)
ax.text(6.55, 4.05, "Perceive", fontsize=10, ha="center", color=MLORANGE)

# Agent components - Reasoning (LLM)
reason_box = FancyBboxPatch(
    (7.6, 3.8),
    1.5,
    0.6,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLBLUE,
    linewidth=1.5,
)
ax.add_patch(reason_box)
ax.text(8.35, 4.05, "Reason", fontsize=10, ha="center", color=MLBLUE)

# Agent components - LLM Core
llm_agent = FancyBboxPatch(
    (6.3, 2.6),
    2.6,
    0.8,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLBLUE,
    linewidth=2,
)
ax.add_patch(llm_agent)
ax.text(7.6, 2.95, "LLM Core", fontsize=11, ha="center", fontweight="bold", color=MLBLUE)

# Agent components - Memory
memory_box = FancyBboxPatch(
    (5.8, 1.5),
    1.3,
    0.7,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLPURPLE,
    linewidth=1.5,
)
ax.add_patch(memory_box)
ax.text(6.45, 1.8, "Memory", fontsize=10, ha="center", color=MLPURPLE)

# Agent components - Tools
tools_box = FancyBboxPatch(
    (7.4, 1.5),
    1.3,
    0.7,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLRED,
    linewidth=1.5,
)
ax.add_patch(tools_box)
ax.text(8.05, 1.8, "Tools", fontsize=10, ha="center", color=MLRED)

# Agent components - Action
action_box = FancyBboxPatch(
    (6.6, 0.5),
    2.0,
    0.6,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLGREEN,
    linewidth=1.5,
)
ax.add_patch(action_box)
ax.text(7.6, 0.75, "Act", fontsize=10, ha="center", color=MLGREEN)

# Arrows connecting agent components
# Perceive -> LLM
ax.annotate(
    "", xy=(6.8, 3.4), xytext=(6.55, 3.8), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)
# Reason -> LLM
ax.annotate(
    "", xy=(8.0, 3.4), xytext=(8.35, 3.8), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)
# LLM -> Memory
ax.annotate(
    "", xy=(6.45, 2.2), xytext=(6.8, 2.6), arrowprops=dict(arrowstyle="<->", color=MLGRAY, lw=1.5)
)
# LLM -> Tools
ax.annotate(
    "", xy=(8.05, 2.2), xytext=(8.0, 2.6), arrowprops=dict(arrowstyle="<->", color=MLGRAY, lw=1.5)
)
# LLM -> Action
ax.annotate(
    "", xy=(7.6, 1.1), xytext=(7.6, 2.6), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=1.5)
)

# Feedback loop (Action back to Perceive)
ax.annotate(
    "",
    xy=(5.9, 3.8),
    xytext=(5.9, 1.1),
    arrowprops=dict(arrowstyle="->", color=MLGREEN, lw=1.5, connectionstyle="arc3,rad=0.3"),
)

# Center divider
ax.axvline(x=5, color=MLGRAY, linestyle="--", alpha=0.5, ymin=0.1, ymax=0.85)

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
