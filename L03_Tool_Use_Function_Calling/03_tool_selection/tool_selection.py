"""
Tool Selection Accuracy by Domain
Week 3 - Tool Use and Function Calling
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update(
    {
        "font.size": 24,
        "axes.labelsize": 24,
        "axes.titlesize": 26,
        "xtick.labelsize": 20,
        "ytick.labelsize": 22,
        "legend.fontsize": 20,
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.family": "sans-serif",
    }
)

MLPURPLE = "#3333B2"
MLBLUE = "#0066CC"
MLORANGE = "#FF7F0E"
MLGREEN = "#2CA02C"

# Tool selection accuracy by domain (synthetic based on ToolLLM paper patterns)
domains = ["Math", "Code", "Web", "File I/O", "Database", "API"]
gpt4_acc = [92, 88, 85, 90, 82, 78]
gpt35_acc = [78, 72, 68, 75, 65, 60]
opensource_acc = [65, 58, 52, 62, 48, 45]

x = np.arange(len(domains))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width, gpt4_acc, width, label="GPT-4", color=MLPURPLE, edgecolor="white", linewidth=1.5
)
bars2 = ax.bar(x, gpt35_acc, width, label="GPT-3.5", color=MLBLUE, edgecolor="white", linewidth=1.5)
bars3 = ax.bar(
    x + width,
    opensource_acc,
    width,
    label="Open Source",
    color=MLORANGE,
    edgecolor="white",
    linewidth=1.5,
)

ax.set_ylabel("Accuracy (%)", fontsize=22)
ax.set_xlabel("Tool Domain", fontsize=22)
ax.set_title("Tool Selection Accuracy by Domain", fontsize=24, fontweight="bold", color=MLPURPLE)
ax.set_xticks(x)
ax.set_xticklabels(domains, fontsize=18)
ax.set_ylim(0, 100)
ax.legend(loc="upper right", fontsize=18)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "tool_selection.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'tool_selection.pdf'}")
