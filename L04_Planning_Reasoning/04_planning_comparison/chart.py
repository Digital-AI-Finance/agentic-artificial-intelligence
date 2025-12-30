"""
Planning Strategy Performance Comparison
Week 4 - Planning and Reasoning
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
        "legend.fontsize": 18,
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

# Planning strategies comparison (synthetic based on research patterns)
strategies = ["Direct", "CoT", "Plan-and-Solve", "Reflexion", "LATS"]
webshop = [45, 52, 58, 67, 72]
alfworld = [38, 48, 55, 71, 78]
hotpotqa = [42, 58, 62, 69, 75]

x = np.arange(len(strategies))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width, webshop, width, label="WebShop", color=MLPURPLE, edgecolor="white", linewidth=1.5
)
bars2 = ax.bar(x, alfworld, width, label="ALFWorld", color=MLBLUE, edgecolor="white", linewidth=1.5)
bars3 = ax.bar(
    x + width, hotpotqa, width, label="HotpotQA", color=MLORANGE, edgecolor="white", linewidth=1.5
)

ax.set_ylabel("Success Rate (%)", fontsize=22)
ax.set_title("Planning Strategy Performance", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.set_xticks(x)
ax.set_xticklabels(strategies, fontsize=16)
ax.set_ylim(0, 90)
ax.legend(loc="upper left", fontsize=16)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

# Add trend line annotation
ax.annotate(
    "", xy=(4.3, 75), xytext=(0, 42), arrowprops=dict(arrowstyle="->", color=MLGREEN, lw=2, ls="--")
)
ax.text(
    2.5, 35, "Improvement with planning", fontsize=14, color=MLGREEN, fontweight="bold", ha="center"
)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
