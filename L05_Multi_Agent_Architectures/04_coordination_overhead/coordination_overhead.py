"""
Multi-Agent Coordination Overhead Analysis
Week 5 - Multi-Agent Architectures
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

# Number of agents vs metrics
agents = [1, 2, 3, 4, 5, 6, 8, 10]
task_performance = [60, 72, 80, 85, 86, 85, 82, 78]
coordination_cost = [0, 15, 28, 42, 58, 75, 95, 120]
net_efficiency = [60, 57, 52, 43, 28, 10, -13, -42]

fig, ax1 = plt.subplots(figsize=(10, 6))

# Performance line
line1 = ax1.plot(
    agents,
    task_performance,
    "o-",
    linewidth=3,
    markersize=10,
    color=MLGREEN,
    label="Task Performance",
)
ax1.set_xlabel("Number of Agents", fontsize=22)
ax1.set_ylabel("Task Performance (%)", fontsize=22, color=MLGREEN)
ax1.tick_params(axis="y", labelcolor=MLGREEN)
ax1.set_ylim(0, 100)

# Coordination cost on secondary axis
ax2 = ax1.twinx()
line2 = ax2.plot(
    agents,
    coordination_cost,
    "s--",
    linewidth=3,
    markersize=10,
    color=MLORANGE,
    label="Coordination Cost",
)
ax2.set_ylabel("Coordination Cost (tokens/1k)", fontsize=22, color=MLORANGE)
ax2.tick_params(axis="y", labelcolor=MLORANGE)
ax2.set_ylim(0, 150)

# Optimal zone
ax1.axvspan(3, 5, alpha=0.15, color=MLBLUE, label="Optimal Zone")
ax1.axvline(x=4, color=MLBLUE, linestyle=":", linewidth=2, alpha=0.7)
ax1.text(4, 95, "Optimal", fontsize=16, ha="center", color=MLBLUE, fontweight="bold")

# Title
ax1.set_title("Agents vs Coordination Overhead", fontsize=24, fontweight="bold", color=MLPURPLE)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="center right", fontsize=16)

ax1.spines["top"].set_visible(False)
ax1.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "coordination_overhead.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'coordination_overhead.pdf'}")
