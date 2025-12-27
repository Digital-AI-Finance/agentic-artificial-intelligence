"""
Reflexion Loop Architecture
Week 4 - Planning and Reasoning
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
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

ax.text(5, 5.7, 'Reflexion: Self-Improvement Loop', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Components in a cycle
components = [
    (2.0, 3.0, 'Actor', 'Generate\naction', MLPURPLE),
    (5.0, 4.5, 'Environment', 'Execute\naction', MLBLUE),
    (8.0, 3.0, 'Evaluator', 'Assess\noutcome', MLORANGE),
    (5.0, 1.5, 'Self-Reflection', 'Generate\nfeedback', MLGREEN),
]

for x, y, name, desc, color in components:
    # Circle node
    circle = Circle((x, y), 0.8, facecolor='white', edgecolor=color, linewidth=3)
    ax.add_patch(circle)
    ax.text(x, y + 0.1, name, fontsize=14, ha='center', fontweight='bold', color=color)
    ax.text(x, y - 0.35, desc, fontsize=10, ha='center', color=MLGRAY)

# Arrows connecting components
arrows = [
    (2.8, 3.3, 4.2, 4.2, 'trajectory'),
    (5.8, 4.2, 7.2, 3.3, 'result'),
    (7.2, 2.7, 5.8, 1.8, 'reward'),
    (4.2, 1.8, 2.8, 2.7, 'memory'),
]

for x1, y1, x2, y2, label in arrows:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=2,
                              connectionstyle='arc3,rad=0.1'))
    # Label on arrow
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx, my + 0.2, label, fontsize=11, ha='center', color=MLGRAY, style='italic')

# Memory box
mem_box = FancyBboxPatch((0.3, 0.3), 2.2, 1.0, boxstyle="round,pad=0.05",
                         facecolor='#F0F0F0', edgecolor=MLGREEN, linewidth=2, linestyle='--')
ax.add_patch(mem_box)
ax.text(1.4, 0.8, 'Long-term Memory', fontsize=12, ha='center', fontweight='bold', color=MLGREEN)
ax.text(1.4, 0.5, '(past reflections)', fontsize=10, ha='center', color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
