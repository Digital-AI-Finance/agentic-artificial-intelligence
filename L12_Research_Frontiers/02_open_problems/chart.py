"""
Open Research Problems in Agents
Week 12 - Research Frontiers
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
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
MLRED = '#D62728'
MLGRAY = '#7F7F7F'

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(5, 5.7, 'Open Research Problems', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Problems as interconnected nodes
problems = [
    (2.0, 4.0, 'Long-Horizon\nPlanning', MLPURPLE),
    (5.0, 4.5, 'World\nModels', MLBLUE),
    (8.0, 4.0, 'Scalable\nAlignment', MLORANGE),
    (2.0, 2.0, 'Persistent\nMemory', MLGREEN),
    (5.0, 1.5, 'Multi-Modal\nAgents', MLPURPLE),
    (8.0, 2.0, 'Evaluation\nMetrics', MLBLUE),
]

for x, y, name, color in problems:
    box = FancyBboxPatch((x-1.0, y-0.5), 2.0, 1.0,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=color, linewidth=2.5)
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=11, ha='center', va='center', fontweight='bold', color=color)

# Connections
connections = [
    (2.0, 4.0, 5.0, 4.5),
    (5.0, 4.5, 8.0, 4.0),
    (2.0, 2.0, 5.0, 1.5),
    (5.0, 1.5, 8.0, 2.0),
    (2.0, 4.0, 2.0, 2.0),
    (8.0, 4.0, 8.0, 2.0),
    (5.0, 4.5, 5.0, 1.5),
]

for x1, y1, x2, y2 in connections:
    ax.plot([x1, x2], [y1, y2], '--', color=MLGRAY, alpha=0.4, linewidth=1.5)

# Central note
ax.text(5, 0.5, 'Interconnected challenges requiring holistic solutions',
        fontsize=11, ha='center', color=MLGRAY, style='italic')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
