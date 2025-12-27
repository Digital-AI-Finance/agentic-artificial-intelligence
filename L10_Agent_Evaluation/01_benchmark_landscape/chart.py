"""
Agent Benchmark Landscape
Week 10 - Agent Evaluation
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

ax.text(5, 5.7, 'Agent Benchmark Landscape', fontsize=24,
        fontweight='bold', ha='center', color=MLPURPLE)

# Benchmark categories
benchmarks = [
    (2.0, 4.0, 'AgentBench', MLPURPLE, ['8 environments', 'OS, DB, Web', 'Multi-step tasks']),
    (5.0, 4.0, 'WebArena', MLBLUE, ['Web browsing', 'E-commerce', 'Realistic sites']),
    (8.0, 4.0, 'SWE-bench', MLORANGE, ['Code tasks', 'GitHub issues', 'Real repos']),
    (2.0, 1.5, 'GAIA', MLGREEN, ['Real-world QA', 'Multi-modal', '3 difficulty levels']),
    (5.0, 1.5, 'ToolBench', MLPURPLE, ['16k+ APIs', 'Tool selection', 'Multi-tool']),
    (8.0, 1.5, 'OSWorld', MLBLUE, ['Desktop OS', 'GUI tasks', 'Screenshots']),
]

for x, y, name, color, features in benchmarks:
    box = FancyBboxPatch((x-1.2, y-1.0), 2.4, 1.8,
                         boxstyle="round,pad=0.05", facecolor='white',
                         edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y+0.5, name, fontsize=13, ha='center', fontweight='bold', color=color)
    for i, feat in enumerate(features):
        ax.text(x, y - 0.1 - i * 0.35, feat, fontsize=9, ha='center', color=MLGRAY)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
