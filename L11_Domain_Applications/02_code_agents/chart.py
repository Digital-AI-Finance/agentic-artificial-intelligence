"""
Code Agent Benchmark Performance
Week 11 - Domain Applications
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
MLGRAY = "#7F7F7F"

# SWE-bench performance (synthetic based on paper patterns)
agents = ["GPT-4", "Claude 3\nOpus", "Devin", "OpenDevin", "SWE-agent", "AutoCodeRover"]
swe_bench = [15.2, 18.5, 13.8, 10.2, 12.5, 19.0]
swe_lite = [22.5, 28.0, 21.5, 16.8, 19.5, 26.5]

x = np.arange(len(agents))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width / 2,
    swe_bench,
    width,
    label="SWE-bench",
    color=MLPURPLE,
    edgecolor="white",
    linewidth=1.5,
)
bars2 = ax.bar(
    x + width / 2,
    swe_lite,
    width,
    label="SWE-bench Lite",
    color=MLORANGE,
    edgecolor="white",
    linewidth=1.5,
)

ax.set_ylabel("Resolution Rate (%)", fontsize=22)
ax.set_title("Code Agents: SWE-bench Performance", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.set_xticks(x)
ax.set_xticklabels(agents, fontsize=12)
ax.set_ylim(0, 35)
ax.legend(loc="upper right", fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

# Human performance reference
ax.axhline(y=4.8, color=MLGRAY, linestyle=":", linewidth=2)
ax.text(5.5, 6, "Human (4.8%)", fontsize=10, color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "chart.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
