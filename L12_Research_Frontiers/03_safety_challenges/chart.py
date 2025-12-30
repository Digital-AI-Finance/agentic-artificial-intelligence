"""
Agent Safety Challenge Severity
Week 12 - Research Frontiers
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
        "legend.fontsize": 14,
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

# Safety challenges
challenges = [
    "Prompt\nInjection",
    "Tool\nMisuse",
    "Goal\nHijacking",
    "Deception",
    "Unintended\nActions",
    "Cascading\nFailures",
]
severity = [85, 72, 68, 55, 78, 82]
mitigation_difficulty = [60, 75, 80, 90, 65, 70]

x = np.arange(len(challenges))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width / 2, severity, width, label="Severity", color=MLRED, edgecolor="white", linewidth=1.5
)
bars2 = ax.bar(
    x + width / 2,
    mitigation_difficulty,
    width,
    label="Mitigation Difficulty",
    color=MLORANGE,
    edgecolor="white",
    linewidth=1.5,
)

ax.set_ylabel("Score (0-100)", fontsize=22)
ax.set_title("Agent Safety Challenges", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.set_xticks(x)
ax.set_xticklabels(challenges, fontsize=12)
ax.set_ylim(0, 100)
ax.legend(loc="upper right", fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

# Priority zone
ax.axhspan(70, 100, alpha=0.1, color=MLRED)
ax.text(5.5, 92, "High Priority", fontsize=10, color=MLRED)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
