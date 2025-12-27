"""
Healthcare Agent Considerations
Week 11 - Domain Applications
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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

ax.text(5, 5.7, 'Healthcare Agent Considerations', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Balance scale visualization
ax.plot([5, 5], [4.5, 2.5], '-', color=MLGRAY, linewidth=3)
ax.plot([5], [4.5], '^', markersize=20, color=MLGRAY)

# Benefits (left)
benefits_box = FancyBboxPatch((1.0, 2.0), 3.0, 2.5,
                              boxstyle="round,pad=0.05", facecolor='#E8F5E9',
                              edgecolor=MLGREEN, linewidth=2)
ax.add_patch(benefits_box)
ax.text(2.5, 4.2, 'Benefits', fontsize=14, ha='center', fontweight='bold', color=MLGREEN)
benefits = ['Clinical decision support', 'Admin automation', 'Literature synthesis', '24/7 availability']
for i, b in enumerate(benefits):
    ax.text(2.5, 3.7 - i * 0.45, b, fontsize=10, ha='center', color=MLGRAY)

ax.plot([4, 5], [3.2, 2.7], '-', color=MLGREEN, linewidth=2)

# Risks (right)
risks_box = FancyBboxPatch((6.0, 2.0), 3.0, 2.5,
                           boxstyle="round,pad=0.05", facecolor='#FFEBEE',
                           edgecolor=MLRED, linewidth=2)
ax.add_patch(risks_box)
ax.text(7.5, 4.2, 'Risks', fontsize=14, ha='center', fontweight='bold', color=MLRED)
risks = ['Hallucination danger', 'Privacy concerns', 'Liability unclear', 'Over-reliance']
for i, r in enumerate(risks):
    ax.text(7.5, 3.7 - i * 0.45, r, fontsize=10, ha='center', color=MLGRAY)

ax.plot([6, 5], [3.2, 2.7], '-', color=MLRED, linewidth=2)

# Key message
ax.text(5, 1.2, 'Human oversight essential | Narrow use cases first',
        fontsize=12, ha='center', color=MLPURPLE, fontweight='bold')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
