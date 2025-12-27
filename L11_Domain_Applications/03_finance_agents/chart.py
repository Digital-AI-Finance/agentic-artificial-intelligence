"""
Finance Agent Use Cases
Week 11 - Domain Applications
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
MLGRAY = '#7F7F7F'

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

ax.text(5, 5.7, 'Finance Agent Applications', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Use cases in a grid
use_cases = [
    (2.0, 4.0, 'Research', MLPURPLE, ['Market analysis', 'News synthesis', 'Report generation']),
    (5.0, 4.0, 'Trading', MLBLUE, ['Strategy backtest', 'Risk assessment', 'Portfolio opt']),
    (8.0, 4.0, 'Compliance', MLORANGE, ['Regulatory check', 'Audit support', 'Documentation']),
    (2.0, 1.5, 'Advisory', MLGREEN, ['Client profiling', 'Recommendation', 'Explain decisions']),
    (5.0, 1.5, 'Operations', MLPURPLE, ['Data extraction', 'Reconciliation', 'Exception handling']),
    (8.0, 1.5, 'Risk Mgmt', MLBLUE, ['Scenario analysis', 'Stress testing', 'Early warning']),
]

for x, y, name, color, features in use_cases:
    box = FancyBboxPatch((x-1.2, y-0.9), 2.4, 1.6,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y+0.4, name, fontsize=13, ha='center', fontweight='bold', color=color)
    for i, feat in enumerate(features):
        ax.text(x, y - 0.1 - i * 0.35, feat, fontsize=9, ha='center', color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
