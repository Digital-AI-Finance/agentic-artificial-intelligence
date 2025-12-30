"""
GraphRAG Query Routing
Week 8 - GraphRAG and Knowledge
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

# Query type performance comparison
query_types = ["Entity\nLookup", "Relationship\nQuery", "Summarization", "Global\nQuestion"]
vector_rag = [85, 55, 40, 25]
graph_rag = [80, 90, 75, 85]
hybrid = [88, 92, 78, 82]

x = np.arange(len(query_types))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(
    x - width,
    vector_rag,
    width,
    label="Vector RAG",
    color=MLPURPLE,
    edgecolor="white",
    linewidth=1.5,
)
bars2 = ax.bar(
    x, graph_rag, width, label="GraphRAG", color=MLORANGE, edgecolor="white", linewidth=1.5
)
bars3 = ax.bar(
    x + width, hybrid, width, label="Hybrid", color=MLGREEN, edgecolor="white", linewidth=1.5
)

ax.set_ylabel("Accuracy (%)", fontsize=22)
ax.set_title(
    "Query Type Performance by RAG Approach", fontsize=24, fontweight="bold", color=MLPURPLE
)
ax.set_xticks(x)
ax.set_xticklabels(query_types, fontsize=14)
ax.set_ylim(0, 100)
ax.legend(loc="upper right", fontsize=14)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(Path(__file__).parent / "query_routing.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'query_routing.pdf'}")
