"""
Hierarchical Planning Diagram
Week 4 - Planning and Reasoning
Shows task decomposition from high-level goals to executable actions
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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

ax.text(5, 5.7, 'Hierarchical Task Decomposition', fontsize=15,
        fontweight='bold', ha='center', color=MLPURPLE)

# Level 0: Goal
goal_box = FancyBboxPatch((3.5, 4.8), 3.0, 0.6,
                          boxstyle="round,pad=0.05", facecolor='#E8E8FF',
                          edgecolor=MLPURPLE, linewidth=2)
ax.add_patch(goal_box)
ax.text(5, 5.1, 'Goal: Book a Trip', fontsize=11, ha='center',
        fontweight='bold', color=MLPURPLE)

# Level 1: High-level plans
level1_tasks = [
    ('Research\nDestinations', 1.5, MLBLUE),
    ('Book\nFlights', 5.0, MLBLUE),
    ('Reserve\nHotel', 8.5, MLBLUE)
]

for name, x, color in level1_tasks:
    box = FancyBboxPatch((x - 0.9, 3.3), 1.8, 0.9,
                         boxstyle="round,pad=0.03", facecolor='#E8F4FF',
                         edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 3.75, name, fontsize=9, ha='center', color=color, fontweight='bold')

    # Arrow from goal
    ax.annotate('', xy=(x, 4.2), xytext=(5, 4.8),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

# Level 2: Sub-tasks (for "Book Flights")
level2_tasks = [
    ('Search\nOptions', 3.5, MLORANGE),
    ('Compare\nPrices', 5.0, MLORANGE),
    ('Select\nFlight', 6.5, MLORANGE)
]

for name, x, color in level2_tasks:
    box = FancyBboxPatch((x - 0.7, 1.9), 1.4, 0.8,
                         boxstyle="round,pad=0.02", facecolor='#FFF4E8',
                         edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 2.3, name, fontsize=8, ha='center', color=color)

    # Arrow from parent
    ax.annotate('', xy=(x, 2.7), xytext=(5.0, 3.3),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.2))

# Level 3: Actions (for "Search Options")
level3_actions = [
    ('Call API', 2.8, MLGREEN),
    ('Parse\nResults', 4.2, MLGREEN)
]

for name, x, color in level3_actions:
    box = FancyBboxPatch((x - 0.6, 0.6), 1.2, 0.7,
                         boxstyle="round,pad=0.02", facecolor='#E8FFE8',
                         edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 0.95, name, fontsize=8, ha='center', color=color)

    # Arrow from parent
    ax.annotate('', xy=(x, 1.3), xytext=(3.5, 1.9),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1))

# Level labels
levels = [
    ('Goal', 5.4, MLPURPLE),
    ('Plans', 4.0, MLBLUE),
    ('Sub-tasks', 2.6, MLORANGE),
    ('Actions', 1.1, MLGREEN)
]

for name, y, color in levels:
    ax.text(0.3, y, name, fontsize=10, ha='left', color=color, fontweight='bold')

# Annotations
ax.text(9.5, 3.75, 'Decompose', fontsize=9, ha='center', color=MLGRAY, style='italic')
ax.annotate('', xy=(9.5, 3.0), xytext=(9.5, 4.5),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
