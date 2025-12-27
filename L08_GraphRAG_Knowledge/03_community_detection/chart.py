"""
Community Detection and Summarization
Week 8 - GraphRAG and Knowledge
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 24, 'axes.labelsize': 24, 'axes.titlesize': 26,
    'figure.figsize': (10, 6), 'figure.dpi': 150, 'font.family': 'sans-serif'
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLGRAY = '#7F7F7F'

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(5, 5.7, 'Hierarchical Community Detection', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Community 1 (left)
c1_nodes = [(1.5, 3.5), (2.2, 4.0), (2.2, 3.0), (0.8, 4.0), (0.8, 3.0)]
for x, y in c1_nodes:
    ax.plot(x, y, 'o', markersize=12, color=MLPURPLE)
for i in range(len(c1_nodes)):
    for j in range(i+1, len(c1_nodes)):
        if np.random.random() > 0.3:
            ax.plot([c1_nodes[i][0], c1_nodes[j][0]], [c1_nodes[i][1], c1_nodes[j][1]],
                    '-', color=MLPURPLE, alpha=0.3, linewidth=1)
comm1 = Circle((1.5, 3.5), 1.0, facecolor='none', edgecolor=MLPURPLE, linewidth=2, linestyle='--')
ax.add_patch(comm1)
ax.text(1.5, 2.2, 'Community 1', fontsize=11, ha='center', color=MLPURPLE, fontweight='bold')

# Community 2 (center)
c2_nodes = [(5.0, 4.0), (5.7, 3.5), (4.3, 3.5), (5.0, 3.0), (5.5, 4.3)]
for x, y in c2_nodes:
    ax.plot(x, y, 'o', markersize=12, color=MLBLUE)
for i in range(len(c2_nodes)):
    for j in range(i+1, len(c2_nodes)):
        if np.random.random() > 0.3:
            ax.plot([c2_nodes[i][0], c2_nodes[j][0]], [c2_nodes[i][1], c2_nodes[j][1]],
                    '-', color=MLBLUE, alpha=0.3, linewidth=1)
comm2 = Circle((5.0, 3.5), 1.0, facecolor='none', edgecolor=MLBLUE, linewidth=2, linestyle='--')
ax.add_patch(comm2)
ax.text(5.0, 2.2, 'Community 2', fontsize=11, ha='center', color=MLBLUE, fontweight='bold')

# Community 3 (right)
c3_nodes = [(8.5, 3.5), (9.2, 4.0), (9.2, 3.0), (7.8, 4.0), (7.8, 3.0)]
for x, y in c3_nodes:
    ax.plot(x, y, 'o', markersize=12, color=MLORANGE)
for i in range(len(c3_nodes)):
    for j in range(i+1, len(c3_nodes)):
        if np.random.random() > 0.3:
            ax.plot([c3_nodes[i][0], c3_nodes[j][0]], [c3_nodes[i][1], c3_nodes[j][1]],
                    '-', color=MLORANGE, alpha=0.3, linewidth=1)
comm3 = Circle((8.5, 3.5), 1.0, facecolor='none', edgecolor=MLORANGE, linewidth=2, linestyle='--')
ax.add_patch(comm3)
ax.text(8.5, 2.2, 'Community 3', fontsize=11, ha='center', color=MLORANGE, fontweight='bold')

# Inter-community edges
ax.plot([2.2, 4.3], [3.5, 3.5], '-', color=MLGRAY, alpha=0.5, linewidth=1.5)
ax.plot([5.7, 7.8], [3.5, 3.5], '-', color=MLGRAY, alpha=0.5, linewidth=1.5)

# Summaries below
sum_box = FancyBboxPatch((0.5, 0.3), 9.0, 1.3,
                         boxstyle="round,pad=0.05", facecolor='#F5F5F5',
                         edgecolor=MLGREEN, linewidth=2)
ax.add_patch(sum_box)
ax.text(5.0, 1.3, 'Community Summaries (LLM-generated)', fontsize=12,
        ha='center', fontweight='bold', color=MLGREEN)
ax.text(2.0, 0.8, 'C1: "AI models..."', fontsize=10, ha='center', color=MLPURPLE)
ax.text(5.0, 0.8, 'C2: "Training data..."', fontsize=10, ha='center', color=MLBLUE)
ax.text(8.0, 0.8, 'C3: "Applications..."', fontsize=10, ha='center', color=MLORANGE)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
