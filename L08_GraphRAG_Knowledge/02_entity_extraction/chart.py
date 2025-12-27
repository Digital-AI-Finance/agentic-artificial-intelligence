"""
Entity and Relationship Extraction
Week 8 - GraphRAG and Knowledge
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

ax.text(5, 5.7, 'Entity Extraction Pipeline', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Document chunk
doc_box = FancyBboxPatch((0.5, 3.5), 3.0, 1.5,
                         boxstyle="round,pad=0.05", facecolor='#F5F5F5',
                         edgecolor=MLGRAY, linewidth=2)
ax.add_patch(doc_box)
ax.text(2.0, 4.7, 'Document Chunk', fontsize=12, ha='center', fontweight='bold', color=MLGRAY)
ax.text(2.0, 4.2, '"OpenAI released GPT-4', fontsize=10, ha='center', color=MLGRAY)
ax.text(2.0, 3.9, 'in March 2023..."', fontsize=10, ha='center', color=MLGRAY)

# LLM extraction
ax.annotate('', xy=(4.5, 4.2), xytext=(3.5, 4.2),
            arrowprops=dict(arrowstyle='->', color=MLPURPLE, lw=2))
ax.text(4.0, 4.6, 'LLM', fontsize=11, ha='center', color=MLPURPLE, fontweight='bold')

# Entities box
ent_box = FancyBboxPatch((4.8, 4.0), 2.2, 1.2,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=MLBLUE, linewidth=2)
ax.add_patch(ent_box)
ax.text(5.9, 4.9, 'Entities', fontsize=12, ha='center', fontweight='bold', color=MLBLUE)
ax.text(5.9, 4.5, 'OpenAI (ORG)', fontsize=10, ha='center', color=MLBLUE)
ax.text(5.9, 4.2, 'GPT-4 (PRODUCT)', fontsize=10, ha='center', color=MLBLUE)

# Relationships box
rel_box = FancyBboxPatch((4.8, 2.5), 2.2, 1.2,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=MLORANGE, linewidth=2)
ax.add_patch(rel_box)
ax.text(5.9, 3.4, 'Relations', fontsize=12, ha='center', fontweight='bold', color=MLORANGE)
ax.text(5.9, 3.0, 'OpenAI -[released]-> GPT-4', fontsize=9, ha='center', color=MLORANGE)
ax.text(5.9, 2.7, 'GPT-4 -[date]-> March 2023', fontsize=9, ha='center', color=MLORANGE)

# Graph output
ax.annotate('', xy=(8.0, 3.8), xytext=(7.0, 4.2),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))
ax.annotate('', xy=(8.0, 3.2), xytext=(7.0, 3.0),
            arrowprops=dict(arrowstyle='->', color=MLGREEN, lw=2))

# Mini graph
nodes = [(8.5, 3.8), (9.2, 3.2), (8.8, 2.6)]
ax.plot(8.5, 3.8, 'o', markersize=15, color=MLBLUE)
ax.plot(9.2, 3.2, 'o', markersize=15, color=MLBLUE)
ax.plot(8.8, 2.6, 'o', markersize=12, color=MLGREEN)
ax.plot([8.5, 9.2], [3.8, 3.2], '-', color=MLORANGE, linewidth=2)
ax.plot([9.2, 8.8], [3.2, 2.6], '-', color=MLORANGE, linewidth=2)
ax.text(8.8, 2.0, 'Knowledge\nGraph', fontsize=11, ha='center', color=MLGREEN, fontweight='bold')

# Extraction stats
ax.text(1.5, 1.5, 'Extraction Stats:', fontsize=12, fontweight='bold', color=MLGRAY)
ax.text(1.5, 1.1, 'Entities: ~50/chunk', fontsize=10, color=MLGRAY)
ax.text(1.5, 0.7, 'Relations: ~30/chunk', fontsize=10, color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
