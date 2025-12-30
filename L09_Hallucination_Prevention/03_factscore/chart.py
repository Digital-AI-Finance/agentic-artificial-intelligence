"""
FActScore Evaluation Methodology
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

# FActScore comparison across models (synthetic based on paper patterns)
models = ["GPT-3.5", "GPT-4", "Claude 2", "Llama 2\n70B", "Claude 3\nOpus"]
factscore = [68, 82, 79, 62, 88]
supported = [72, 85, 81, 65, 90]

x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width / 2,
    factscore,
    width,
    label="FActScore",
    color=MLPURPLE,
    edgecolor="white",
    linewidth=1.5,
)
bars2 = ax.bar(
    x + width / 2,
    supported,
    width,
    label="% Supported Claims",
    color=MLORANGE,
    edgecolor="white",
    linewidth=1.5,
)

# Add value labels
for bar, val in zip(bars1, factscore):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{val}",
        ha="center",
        fontsize=14,
        fontweight="bold",
        color=MLPURPLE,
    )

ax.set_ylabel("Score (%)", fontsize=22)
ax.set_title(
    "FActScore: Factual Precision by Model", fontsize=24, fontweight="bold", color=MLPURPLE
)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=14)
ax.set_ylim(0, 100)
ax.legend(loc="lower right", fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
