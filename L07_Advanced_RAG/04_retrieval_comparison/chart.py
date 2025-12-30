"""
RAG Retrieval Strategy Comparison
Week 7 - Advanced RAG
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 18,
        "ytick.labelsize": 22,
        "legend.fontsize": 16,
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

# Comparison data (synthetic based on research patterns)
strategies = ["Naive\nRAG", "Query\nRewrite", "HyDE", "Self-RAG", "CRAG", "Agentic\nRAG"]
accuracy = [62, 68, 71, 78, 76, 82]
latency = [1.0, 1.2, 1.5, 2.2, 1.8, 3.5]  # Relative latency

x = np.arange(len(strategies))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# Accuracy bars
bars1 = ax1.bar(
    x - width / 2,
    accuracy,
    width,
    label="Accuracy (%)",
    color=MLPURPLE,
    edgecolor="white",
    linewidth=1.5,
)
ax1.set_xlabel("Strategy", fontsize=22)
ax1.set_ylabel("Accuracy (%)", fontsize=22, color=MLPURPLE)
ax1.tick_params(axis="y", labelcolor=MLPURPLE)
ax1.set_ylim(50, 90)

# Latency bars on secondary axis
ax2 = ax1.twinx()
bars2 = ax2.bar(
    x + width / 2,
    latency,
    width,
    label="Latency (relative)",
    color=MLORANGE,
    edgecolor="white",
    linewidth=1.5,
)
ax2.set_ylabel("Latency (relative)", fontsize=22, color=MLORANGE)
ax2.tick_params(axis="y", labelcolor=MLORANGE)
ax2.set_ylim(0, 4.5)

ax1.set_xticks(x)
ax1.set_xticklabels(strategies, fontsize=14)
ax1.set_title("RAG Strategy: Accuracy vs Latency", fontsize=24, fontweight="bold", color=MLPURPLE)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=14)

ax1.spines["top"].set_visible(False)
ax1.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
