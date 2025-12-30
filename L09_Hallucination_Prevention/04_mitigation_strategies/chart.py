"""
Hallucination Mitigation Strategy Effectiveness
Week 9 - Hallucination Prevention
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 16,
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

# Mitigation strategies effectiveness
strategies = [
    "Baseline",
    "RAG",
    "Self-\nConsistency",
    "Chain-of-\nVerification",
    "Self-\nRefine",
    "Multi-\nAgent",
]
hallucination_rate = [25, 18, 15, 10, 12, 8]
latency_multiplier = [1.0, 1.3, 2.5, 2.8, 2.2, 4.0]

fig, ax1 = plt.subplots(figsize=(10, 6))

x = np.arange(len(strategies))

# Hallucination rate bars
bars = ax1.bar(x, hallucination_rate, color=MLPURPLE, edgecolor="white", linewidth=1.5, alpha=0.8)
ax1.set_xlabel("Mitigation Strategy", fontsize=22)
ax1.set_ylabel("Hallucination Rate (%)", fontsize=22, color=MLPURPLE)
ax1.tick_params(axis="y", labelcolor=MLPURPLE)
ax1.set_ylim(0, 30)

# Color bars by effectiveness
colors = [MLPURPLE, MLBLUE, MLBLUE, MLGREEN, MLGREEN, MLGREEN]
for bar, color in zip(bars, colors):
    bar.set_facecolor(color)

# Latency line on secondary axis
ax2 = ax1.twinx()
line = ax2.plot(x, latency_multiplier, "o-", color=MLORANGE, linewidth=3, markersize=10)
ax2.set_ylabel("Latency Multiplier", fontsize=22, color=MLORANGE)
ax2.tick_params(axis="y", labelcolor=MLORANGE)
ax2.set_ylim(0, 5)

ax1.set_xticks(x)
ax1.set_xticklabels(strategies, fontsize=13)
ax1.set_title("Mitigation Effectiveness vs Cost", fontsize=24, fontweight="bold", color=MLPURPLE)

ax1.spines["top"].set_visible(False)
ax1.grid(axis="y", alpha=0.3)

# Best trade-off annotation
ax1.annotate(
    "Best\ntrade-off",
    xy=(3, 10),
    xytext=(4, 20),
    arrowprops=dict(arrowstyle="->", color=MLGREEN, lw=1.5),
    fontsize=12,
    color=MLGREEN,
    ha="center",
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
