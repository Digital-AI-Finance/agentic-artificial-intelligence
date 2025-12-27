"""
Agent State Management Patterns
Week 6 - Agent Frameworks and Tools
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
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

ax.text(5, 5.7, 'State Management Patterns', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Three patterns
patterns = [
    (1.7, 3.5, 'Stateless', MLPURPLE, [
        'No memory',
        'Each call independent',
        'Simple, scalable',
        'No context retention'
    ]),
    (5.0, 3.5, 'Session State', MLBLUE, [
        'In-memory state',
        'Conversation context',
        'Lost on restart',
        'Single session'
    ]),
    (8.3, 3.5, 'Persistent', MLGREEN, [
        'Database backed',
        'Cross-session memory',
        'Checkpointing',
        'Full history'
    ]),
]

for x, y, name, color, features in patterns:
    # Main box
    box = FancyBboxPatch((x - 1.4, y - 2.2), 2.8, 3.5,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=color, linewidth=3)
    ax.add_patch(box)

    # Header
    header = FancyBboxPatch((x - 1.4, y + 0.9), 2.8, 0.45,
                            boxstyle="round,pad=0.02,rounding_size=0.15",
                            facecolor=color, edgecolor=color, linewidth=1)
    ax.add_patch(header)
    ax.text(x, y + 1.12, name, fontsize=14, ha='center', fontweight='bold', color='white')

    # Features
    for i, feat in enumerate(features):
        ax.text(x, y + 0.4 - i * 0.55, feat, fontsize=11, ha='center', color=MLGRAY)

# Arrows showing progression
ax.annotate('', xy=(3.3, 3.5), xytext=(2.5, 3.5),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=2))
ax.annotate('', xy=(6.7, 3.5), xytext=(5.8, 3.5),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=2))

ax.text(2.9, 3.8, 'add memory', fontsize=10, color=MLGRAY, style='italic')
ax.text(6.25, 3.8, 'add persistence', fontsize=10, color=MLGRAY, style='italic')

# Complexity indicator
ax.text(1.7, 0.9, 'Simple', fontsize=12, ha='center', color=MLPURPLE, fontweight='bold')
ax.text(8.3, 0.9, 'Complex', fontsize=12, ha='center', color=MLGREEN, fontweight='bold')
ax.annotate('', xy=(8.0, 0.6), xytext=(2.0, 0.6),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
