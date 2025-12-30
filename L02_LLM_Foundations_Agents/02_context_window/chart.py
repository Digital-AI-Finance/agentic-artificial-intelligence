"""
Context Window Impact on Agent Capabilities
Week 2 - LLM Foundations for Agents
Visualizes how context window size affects agent performance
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Chart settings for Beamer slides (scaled for 70% display)
plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 11,
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

# Context window sizes (in K tokens)
models = ["GPT-3.5\n4K", "GPT-3.5\n16K", "GPT-4\n8K", "GPT-4\n32K", "GPT-4\n128K", "Claude 3\n200K"]
context_sizes = [4, 16, 8, 32, 128, 200]

# Simulated capability scores (0-100) for different agent tasks
# These represent approximate relative performance
capabilities = {
    "Single-turn QA": [95, 95, 98, 98, 98, 98],
    "Multi-step reasoning": [60, 75, 80, 90, 95, 95],
    "Long document analysis": [30, 60, 45, 80, 95, 98],
    "Complex agent tasks": [40, 55, 60, 75, 90, 92],
}

x = np.arange(len(models))
width = 0.2
multiplier = 0

colors = [MLBLUE, MLORANGE, MLGREEN, MLPURPLE]

for i, (attribute, measurement) in enumerate(capabilities.items()):
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors[i], alpha=0.85)
    multiplier += 1

# Add context size annotation on top
for i, (model, size) in enumerate(zip(models, context_sizes)):
    ax.annotate(
        f"{size}K", xy=(i + 0.3, 102), fontsize=9, ha="center", color=MLGRAY, fontweight="bold"
    )

ax.set_ylabel("Capability Score (%)", fontsize=13)
ax.set_xlabel("Model / Context Window", fontsize=13)
ax.set_title(
    "Context Window Impact on Agent Capabilities", fontsize=15, fontweight="bold", color=MLPURPLE
)
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(models, fontsize=10)
ax.legend(loc="lower right", fontsize=10, framealpha=0.9)
ax.set_ylim(0, 110)
ax.set_yticks([0, 25, 50, 75, 100])
ax.axhline(y=100, color=MLGRAY, linestyle="--", alpha=0.3, linewidth=1)

# Add grid for readability
ax.yaxis.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Add annotation for key insight
ax.annotate(
    "Larger context enables\ncomplex agent workflows",
    xy=(4.5, 45),
    fontsize=10,
    ha="center",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=MLGRAY, alpha=0.8),
)

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
