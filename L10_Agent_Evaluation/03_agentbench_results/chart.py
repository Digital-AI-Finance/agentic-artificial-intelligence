"""
AgentBench Results Comparison
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

# AgentBench environment results (synthetic based on paper patterns)
environments = ["OS", "DB", "KG", "Cards", "LTP", "House", "Web\nShop", "Web\nBrowse"]
gpt4 = [42, 38, 55, 78, 65, 45, 52, 35]
gpt35 = [28, 22, 35, 62, 48, 32, 38, 22]
claude = [38, 35, 48, 72, 58, 42, 48, 32]

x = np.arange(len(environments))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width, gpt4, width, label="GPT-4", color=MLPURPLE, edgecolor="white", linewidth=1
)
bars2 = ax.bar(x, gpt35, width, label="GPT-3.5", color=MLBLUE, edgecolor="white", linewidth=1)
bars3 = ax.bar(
    x + width, claude, width, label="Claude", color=MLORANGE, edgecolor="white", linewidth=1
)

ax.set_ylabel("Success Rate (%)", fontsize=22)
ax.set_title(
    "AgentBench: Performance by Environment", fontsize=24, fontweight="bold", color=MLPURPLE
)
ax.set_xticks(x)
ax.set_xticklabels(environments, fontsize=12)
ax.set_ylim(0, 100)
ax.legend(loc="upper right", fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

# Add average line
avg_gpt4 = np.mean(gpt4)
ax.axhline(y=avg_gpt4, color=MLPURPLE, linestyle="--", linewidth=1.5, alpha=0.7)
ax.text(7.5, avg_gpt4 + 2, f"GPT-4 avg: {avg_gpt4:.0f}%", fontsize=10, color=MLPURPLE)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
