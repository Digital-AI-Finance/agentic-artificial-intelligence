"""
Prompting Strategy Comparison (GSM8K Performance)
Week 2 - LLM Foundations for Agents
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 20,
        "ytick.labelsize": 22,
        "legend.fontsize": 20,
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.family": "sans-serif",
    }
)

MLPURPLE = "#3333B2"
MLBLUE = "#0066CC"
MLORANGE = "#FF7F0E"
MLGREEN = "#2CA02C"

strategies = ["Zero-Shot", "Few-Shot", "Zero-Shot\nCoT", "Few-Shot\nCoT", "Self-\nConsistency"]
accuracy = [17.1, 33.7, 40.7, 58.3, 74.4]
colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN, "#D62728"]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(strategies, accuracy, color=colors, edgecolor="white", linewidth=2, width=0.7)

for bar, acc in zip(bars, accuracy):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{acc}%",
        ha="center",
        fontsize=18,
        fontweight="bold",
    )

ax.set_ylabel("Accuracy (%)", fontsize=22)
ax.set_ylim(0, 90)
ax.set_title("Prompting Strategies on GSM8K", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
