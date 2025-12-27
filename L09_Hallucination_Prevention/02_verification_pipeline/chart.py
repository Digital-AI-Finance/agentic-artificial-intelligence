"""
Verification Pipeline for Hallucination Detection
Week 9 - Hallucination Prevention
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

ax.text(5, 5.7, 'Chain-of-Verification Pipeline', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Pipeline stages
stages = [
    (1.5, 3.5, 'Generate\nResponse', MLPURPLE),
    (3.5, 3.5, 'Extract\nClaims', MLBLUE),
    (5.5, 3.5, 'Generate\nQuestions', MLORANGE),
    (7.5, 3.5, 'Verify\nIndependently', MLGREEN),
    (9.0, 3.5, 'Revise', MLPURPLE),
]

for x, y, name, color in stages:
    box = FancyBboxPatch((x-0.7, y-0.5), 1.4, 1.0,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, name, fontsize=11, ha='center', va='center', fontweight='bold', color=color)

# Arrows
for i in range(len(stages)-1):
    x1 = stages[i][0] + 0.7
    x2 = stages[i+1][0] - 0.7
    ax.annotate('', xy=(x2, 3.5), xytext=(x1, 3.5),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

# Example flow below
ax.text(0.5, 2.0, 'Example:', fontsize=12, fontweight='bold', color=MLGRAY)

examples = [
    (1.5, 1.5, '"Paris is capital of France"', MLPURPLE),
    (3.5, 1.5, '[Paris, France, capital]', MLBLUE),
    (5.5, 1.5, '"What is France capital?"', MLORANGE),
    (7.5, 1.5, '"Paris" (verified)', MLGREEN),
]

for x, y, text, color in examples:
    ax.text(x, y, text, fontsize=9, ha='center', color=color)

# Verification result
ax.text(9.0, 1.5, 'Correct!', fontsize=10, ha='center', color=MLGREEN, fontweight='bold')

# Key insight
ax.text(5.0, 0.5, 'Key: Independent verification prevents confirmation bias',
        fontsize=11, ha='center', color=MLGRAY, style='italic')

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
