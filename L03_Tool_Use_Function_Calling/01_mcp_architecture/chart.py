"""
Model Context Protocol (MCP) Architecture Diagram
Week 3 - Tool Use and Function Calling
Visualizes the MCP client-server architecture
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
    5,
    5.7,
    "Model Context Protocol (MCP) Architecture",
    fontsize=15,
    fontweight="bold",
    ha="center",
    color=MLPURPLE,
)

# Host Application (left)
host_box = FancyBboxPatch(
    (0.3, 2.0),
    2.8,
    2.5,
    boxstyle="round,pad=0.05",
    facecolor="#E8E8FF",
    edgecolor=MLPURPLE,
    linewidth=2,
)
ax.add_patch(host_box)
ax.text(1.7, 4.2, "Host Application", fontsize=11, fontweight="bold", ha="center", color=MLPURPLE)

# LLM inside host
llm_box = FancyBboxPatch(
    (0.5, 3.0),
    2.4,
    0.8,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLBLUE,
    linewidth=1.5,
)
ax.add_patch(llm_box)
ax.text(1.7, 3.4, "LLM", fontsize=10, ha="center", fontweight="bold", color=MLBLUE)

# MCP Client inside host
client_box = FancyBboxPatch(
    (0.5, 2.2),
    2.4,
    0.6,
    boxstyle="round,pad=0.02",
    facecolor="white",
    edgecolor=MLORANGE,
    linewidth=1.5,
)
ax.add_patch(client_box)
ax.text(1.7, 2.5, "MCP Client", fontsize=10, ha="center", color=MLORANGE)

# Protocol layer (middle)
ax.text(
    5, 3.5, "JSON-RPC 2.0", fontsize=10, ha="center", color=MLGRAY, fontweight="bold", rotation=0
)
ax.text(5, 3.1, "stdio / HTTP", fontsize=9, ha="center", color=MLGRAY)

# Arrows
ax.annotate(
    "", xy=(3.8, 3.3), xytext=(3.1, 3.3), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)
ax.annotate(
    "", xy=(3.1, 2.7), xytext=(3.8, 2.7), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)

ax.annotate(
    "", xy=(6.9, 3.3), xytext=(6.2, 3.3), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)
ax.annotate(
    "", xy=(6.2, 2.7), xytext=(6.9, 2.7), arrowprops=dict(arrowstyle="->", color=MLGRAY, lw=2)
)

# MCP Server (right)
server_box = FancyBboxPatch(
    (6.9, 1.5),
    2.8,
    3.5,
    boxstyle="round,pad=0.05",
    facecolor="#E8FFE8",
    edgecolor=MLGREEN,
    linewidth=2,
)
ax.add_patch(server_box)
ax.text(8.3, 4.7, "MCP Server", fontsize=11, fontweight="bold", ha="center", color=MLGREEN)

# Server components
components = [("Tools", 3.8, MLRED), ("Resources", 3.0, MLBLUE), ("Prompts", 2.2, MLORANGE)]
for name, y, color in components:
    box = FancyBboxPatch(
        (7.1, y),
        2.4,
        0.6,
        boxstyle="round,pad=0.02",
        facecolor="white",
        edgecolor=color,
        linewidth=1.5,
    )
    ax.add_patch(box)
    ax.text(8.3, y + 0.3, name, fontsize=10, ha="center", color=color)

# Legend at bottom
ax.text(1.7, 1.3, "Claude, GPT, etc.", fontsize=9, ha="center", color=MLGRAY, style="italic")
ax.text(5, 1.3, "Request/Response", fontsize=9, ha="center", color=MLGRAY, style="italic")
ax.text(8.3, 1.3, "External capabilities", fontsize=9, ha="center", color=MLGRAY, style="italic")

# Protocol flow labels
ax.text(4.5, 3.6, "call tool", fontsize=8, color=MLGRAY)
ax.text(4.5, 2.4, "result", fontsize=8, color=MLGRAY)

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
