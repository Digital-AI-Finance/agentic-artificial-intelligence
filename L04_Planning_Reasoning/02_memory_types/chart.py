"""
Memory Types Comparison
Week 4 - Planning and Reasoning
Compares working memory, episodic memory, and semantic memory in agents
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 24, 'axes.labelsize': 24, 'axes.titlesize': 26,
    'xtick.labelsize': 22, 'ytick.labelsize': 22, 'legend.fontsize': 22,
    'figure.figsize': (10, 6), 'figure.dpi': 150, 'font.family': 'sans-serif'
})

MLPURPLE = '#3333B2'
MLLAVENDER = '#ADADE0'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLGRAY = '#7F7F7F'

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(5, 5.7, 'Agent Memory Types', fontsize=15,
        fontweight='bold', ha='center', color=MLPURPLE)

# Three memory type boxes
memory_types = [
    ('Working Memory', 1.7, MLBLUE, [
        'Current context',
        'Active goals',
        'Scratchpad',
        'Short-term'
    ]),
    ('Episodic Memory', 5.0, MLORANGE, [
        'Past experiences',
        'Conversation history',
        'Trial outcomes',
        'Temporal ordering'
    ]),
    ('Semantic Memory', 8.3, MLGREEN, [
        'Facts & knowledge',
        'Learned patterns',
        'Tool descriptions',
        'Long-term storage'
    ])
]

for name, x, color, items in memory_types:
    # Main box
    box = FancyBboxPatch((x - 1.4, 1.5), 2.8, 3.5,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=color, linewidth=2)
    ax.add_patch(box)

    # Header
    header = FancyBboxPatch((x - 1.4, 4.4), 2.8, 0.6,
                            boxstyle="round,pad=0.02,rounding_size=0.2",
                            facecolor=color, edgecolor=color, linewidth=1)
    ax.add_patch(header)
    ax.text(x, 4.7, name, fontsize=10, ha='center', fontweight='bold', color='white')

    # Items
    for i, item in enumerate(items):
        y = 3.8 - i * 0.55
        ax.text(x, y, item, fontsize=9, ha='center', color=MLGRAY)

# Arrows showing data flow
ax.annotate('', xy=(3.3, 3.0), xytext=(3.6, 3.0),
            arrowprops=dict(arrowstyle='<->', color=MLGRAY, lw=1.5))
ax.annotate('', xy=(6.4, 3.0), xytext=(6.7, 3.0),
            arrowprops=dict(arrowstyle='<->', color=MLGRAY, lw=1.5))

# Labels under boxes
ax.text(1.7, 1.1, 'Context Window', fontsize=9, ha='center', color=MLBLUE, style='italic')
ax.text(5.0, 1.1, 'Vector Store', fontsize=9, ha='center', color=MLORANGE, style='italic')
ax.text(8.3, 1.1, 'Knowledge Base', fontsize=9, ha='center', color=MLGREEN, style='italic')

# Capacity labels
ax.text(1.7, 0.7, '~100K tokens', fontsize=8, ha='center', color=MLGRAY)
ax.text(5.0, 0.7, 'Unlimited', fontsize=8, ha='center', color=MLGRAY)
ax.text(8.3, 0.7, 'Unlimited', fontsize=8, ha='center', color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
