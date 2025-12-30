"""
Human vs Automated Evaluation Correlation
Week 10 - Agent Evaluation
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
MLGRAY = "#7F7F7F"

np.random.seed(42)

# Simulated human vs automated evaluation scores
n_samples = 30
human_scores = np.random.uniform(30, 90, n_samples)
auto_scores = human_scores + np.random.normal(0, 8, n_samples)
auto_scores = np.clip(auto_scores, 0, 100)

fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot
ax.scatter(
    human_scores, auto_scores, s=150, c=MLPURPLE, alpha=0.7, edgecolors="white", linewidth=1.5
)

# Add correlation line
z = np.polyfit(human_scores, auto_scores, 1)
p = np.poly1d(z)
x_line = np.linspace(25, 95, 100)
ax.plot(
    x_line,
    p(x_line),
    "--",
    color=MLORANGE,
    linewidth=2.5,
    label=f"Fit (r={np.corrcoef(human_scores, auto_scores)[0,1]:.2f})",
)

# Perfect correlation line
ax.plot([25, 95], [25, 95], ":", color=MLGRAY, linewidth=2, label="Perfect correlation")

ax.set_xlabel("Human Evaluation Score", fontsize=22)
ax.set_ylabel("Automated Evaluation Score", fontsize=22)
ax.set_title("Human vs Automated Evaluation", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.set_xlim(25, 95)
ax.set_ylim(25, 95)
ax.legend(loc="lower right", fontsize=16)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "human_eval.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'human_eval.pdf'}")
