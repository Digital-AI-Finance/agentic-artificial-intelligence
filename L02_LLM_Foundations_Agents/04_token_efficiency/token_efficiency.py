"""
Token Efficiency vs Accuracy Tradeoff
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
        "xtick.labelsize": 22,
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

methods = ["Zero-Shot", "Few-Shot", "CoT", "Self-Consistency\n(k=5)"]
tokens = [50, 200, 150, 750]
accuracy = [17, 34, 58, 74]
colors = [MLPURPLE, MLBLUE, MLORANGE, MLGREEN]

fig, ax = plt.subplots(figsize=(10, 6))

for i, (t, a, m, c) in enumerate(zip(tokens, accuracy, methods, colors)):
    ax.scatter(t, a, s=500, c=c, alpha=0.8, edgecolors="white", linewidth=2, zorder=5)
    ax.annotate(
        m,
        (t, a),
        textcoords="offset points",
        xytext=(0, 20),
        ha="center",
        fontsize=16,
        color=c,
        fontweight="bold",
    )

ax.set_xlabel("Tokens per Query (avg)", fontsize=22)
ax.set_ylabel("Accuracy (%)", fontsize=22)
ax.set_title("Cost vs Accuracy Tradeoff", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.set_xlim(0, 900)
ax.set_ylim(0, 90)
ax.grid(True, alpha=0.3)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "token_efficiency.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'token_efficiency.pdf'}")
