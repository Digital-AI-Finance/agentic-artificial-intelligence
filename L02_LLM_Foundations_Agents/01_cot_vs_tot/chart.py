"""
Chain-of-Thought vs Tree-of-Thoughts Comparison
Week 2 - LLM Foundations for Agents
Visualizes the structural difference between linear CoT and branching ToT
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from pathlib import Path

# Chart settings for Beamer slides (scaled for 70% display)
plt.rcParams.update({
    'font.size': 24,
    'axes.labelsize': 24,
    'axes.titlesize': 26,
    'xtick.labelsize': 22,
    'ytick.labelsize': 22,
    'legend.fontsize': 22,
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'font.family': 'sans-serif'
})

# ML Course color palette
MLPURPLE = '#3333B2'
MLLAVENDER = '#ADADE0'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'
MLRED = '#D62728'
MLGRAY = '#7F7F7F'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

# ========== LEFT: Chain-of-Thought (Linear) ==========
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 6)
ax1.axis('off')
ax1.set_title('Chain-of-Thought (CoT)', fontsize=14, fontweight='bold', color=MLBLUE, pad=10)

# Draw linear chain
cot_nodes = [
    (2, 5.2, 'Question', MLPURPLE),
    (2, 4.2, 'Step 1', MLBLUE),
    (2, 3.2, 'Step 2', MLBLUE),
    (2, 2.2, 'Step 3', MLBLUE),
    (2, 1.2, 'Answer', MLGREEN),
]

for i, (x, y, label, color) in enumerate(cot_nodes):
    box = FancyBboxPatch((x - 0.6, y - 0.3), 1.2, 0.6,
                         boxstyle="round,pad=0.03,rounding_size=0.1",
                         facecolor='white', edgecolor=color, linewidth=2)
    ax1.add_patch(box)
    ax1.text(x, y, label, fontsize=11, ha='center', va='center',
             fontweight='bold', color=color)

    # Draw arrow to next node
    if i < len(cot_nodes) - 1:
        ax1.annotate('', xy=(2, cot_nodes[i+1][1] + 0.35), xytext=(2, y - 0.35),
                    arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=2))

# Add description
ax1.text(2, 0.4, 'Linear reasoning chain', fontsize=10, ha='center',
         color=MLGRAY, style='italic')
ax1.text(2, 0.1, 'One path to answer', fontsize=9, ha='center', color=MLGRAY)

# ========== RIGHT: Tree-of-Thoughts (Branching) ==========
ax2.set_xlim(0, 6)
ax2.set_ylim(0, 6)
ax2.axis('off')
ax2.set_title('Tree-of-Thoughts (ToT)', fontsize=14, fontweight='bold', color=MLORANGE, pad=10)

# Draw tree structure
# Level 0: Question
ax2.add_patch(FancyBboxPatch((2.4, 5.0), 1.2, 0.5,
                             boxstyle="round,pad=0.03,rounding_size=0.1",
                             facecolor='white', edgecolor=MLPURPLE, linewidth=2))
ax2.text(3, 5.25, 'Question', fontsize=10, ha='center', va='center',
         fontweight='bold', color=MLPURPLE)

# Level 1: Three branches
level1_x = [1.0, 3.0, 5.0]
for x in level1_x:
    ax2.add_patch(FancyBboxPatch((x - 0.5, 3.8), 1.0, 0.5,
                                 boxstyle="round,pad=0.03,rounding_size=0.1",
                                 facecolor='white', edgecolor=MLBLUE, linewidth=1.5))
    ax2.text(x, 4.05, 'Thought', fontsize=9, ha='center', va='center', color=MLBLUE)
    # Arrow from question
    ax2.annotate('', xy=(x, 4.3), xytext=(3, 5.0),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

# Level 2: Evaluate and expand
# Left branch (pruned - marked with X)
ax2.add_patch(FancyBboxPatch((0.5, 2.5), 1.0, 0.5,
                             boxstyle="round,pad=0.03,rounding_size=0.1",
                             facecolor='#FFE0E0', edgecolor=MLRED, linewidth=1.5))
ax2.text(1.0, 2.75, 'Eval: 0.3', fontsize=8, ha='center', va='center', color=MLRED)
ax2.annotate('', xy=(1.0, 3.0), xytext=(1.0, 3.8),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))
ax2.text(1.0, 2.1, 'Pruned', fontsize=8, ha='center', color=MLRED, style='italic')

# Middle branch (continues)
for x_offset in [-0.6, 0.6]:
    ax2.add_patch(FancyBboxPatch((2.4 + x_offset, 2.5), 1.0, 0.5,
                                 boxstyle="round,pad=0.03,rounding_size=0.1",
                                 facecolor='white', edgecolor=MLBLUE, linewidth=1.5))
    ax2.text(2.9 + x_offset, 2.75, 'Thought', fontsize=8, ha='center', va='center', color=MLBLUE)
    ax2.annotate('', xy=(2.9 + x_offset, 3.0), xytext=(3.0, 3.8),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

# Right branch (continues to answer)
ax2.add_patch(FancyBboxPatch((4.5, 2.5), 1.0, 0.5,
                             boxstyle="round,pad=0.03,rounding_size=0.1",
                             facecolor='#E0FFE0', edgecolor=MLGREEN, linewidth=1.5))
ax2.text(5.0, 2.75, 'Eval: 0.9', fontsize=8, ha='center', va='center', color=MLGREEN)
ax2.annotate('', xy=(5.0, 3.0), xytext=(5.0, 3.8),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))

# Final answer (from best branch)
ax2.add_patch(FancyBboxPatch((4.5, 1.2), 1.0, 0.5,
                             boxstyle="round,pad=0.03,rounding_size=0.1",
                             facecolor='white', edgecolor=MLGREEN, linewidth=2))
ax2.text(5.0, 1.45, 'Answer', fontsize=10, ha='center', va='center',
         fontweight='bold', color=MLGREEN)
ax2.annotate('', xy=(5.0, 1.7), xytext=(5.0, 2.5),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))

# Add description
ax2.text(3, 0.4, 'Explore multiple paths', fontsize=10, ha='center',
         color=MLGRAY, style='italic')
ax2.text(3, 0.1, 'Evaluate and prune', fontsize=9, ha='center', color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf',
            dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
