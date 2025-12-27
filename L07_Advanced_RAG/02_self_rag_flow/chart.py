"""
Self-RAG Decision Flow
Week 7 - Advanced RAG
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
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

ax.text(5, 5.7, 'Self-RAG: Adaptive Retrieval', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Decision nodes
nodes = [
    (1.5, 3.5, 'Query', MLPURPLE, 'rect'),
    (3.5, 3.5, 'Retrieve?', MLORANGE, 'diamond'),
    (5.5, 4.5, 'Retrieve', MLBLUE, 'rect'),
    (5.5, 2.5, 'Generate', MLBLUE, 'rect'),
    (7.5, 3.5, 'Critique', MLORANGE, 'diamond'),
    (9.0, 3.5, 'Output', MLGREEN, 'rect'),
]

for x, y, label, color, shape in nodes:
    if shape == 'diamond':
        # Diamond for decision
        diamond = plt.Polygon([(x, y+0.5), (x+0.6, y), (x, y-0.5), (x-0.6, y)],
                             facecolor='white', edgecolor=color, linewidth=2)
        ax.add_patch(diamond)
        ax.text(x, y, label, fontsize=11, ha='center', va='center', color=color, fontweight='bold')
    else:
        # Rectangle for action
        box = FancyBboxPatch((x-0.6, y-0.35), 1.2, 0.7,
                             boxstyle="round,pad=0.05", facecolor='white',
                             edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=12, ha='center', va='center', color=color, fontweight='bold')

# Arrows with labels
arrows = [
    (2.1, 3.5, 2.9, 3.5, ''),
    (4.1, 3.8, 4.9, 4.3, 'yes'),
    (4.1, 3.2, 4.9, 2.7, 'no'),
    (6.1, 4.5, 6.9, 3.8, ''),
    (6.1, 2.5, 6.9, 3.2, ''),
    (8.1, 3.5, 8.4, 3.5, 'pass'),
]

for x1, y1, x2, y2, label in arrows:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))
    if label:
        ax.text((x1+x2)/2 + 0.1, (y1+y2)/2 + 0.15, label, fontsize=10, color=MLGRAY)

# Retry loop
ax.annotate('', xy=(3.5, 2.9), xytext=(7.5, 2.9),
            arrowprops=dict(arrowstyle='->', color=MLRED, lw=1.5,
                          connectionstyle='arc3,rad=-0.3'))
ax.text(5.5, 1.8, 'fail: retry', fontsize=10, color=MLRED, ha='center')

# Critique tokens
ax.text(0.5, 1.2, 'Critique Tokens:', fontsize=12, fontweight='bold', color=MLGRAY)
ax.text(0.5, 0.8, '[Retrieve], [IsRel], [IsSup], [IsUse]', fontsize=11, color=MLORANGE)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
