"""
Agent Evaluation Dimensions
Week 10 - Agent Evaluation
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 24, 'axes.labelsize': 24, 'axes.titlesize': 26,
    'xtick.labelsize': 22, 'ytick.labelsize': 22, 'legend.fontsize': 18,
    'figure.figsize': (10, 6), 'figure.dpi': 150, 'font.family': 'sans-serif'
})

MLPURPLE = '#3333B2'
MLBLUE = '#0066CC'
MLORANGE = '#FF7F0E'
MLGREEN = '#2CA02C'

# Evaluation dimensions radar
categories = ['Task Success', 'Efficiency', 'Safety', 'Robustness', 'Interpretability', 'Generalization']
N = len(categories)

# Different agent profiles
gpt4_agent = [0.75, 0.6, 0.7, 0.65, 0.8, 0.7]
claude_agent = [0.72, 0.65, 0.85, 0.7, 0.85, 0.68]
opensource = [0.55, 0.7, 0.5, 0.45, 0.6, 0.5]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

for values, label, color in [(gpt4_agent, 'GPT-4 Agent', MLPURPLE),
                              (claude_agent, 'Claude Agent', MLORANGE),
                              (opensource, 'Open Source', MLBLUE)]:
    values = values + values[:1]
    ax.plot(angles, values, 'o-', linewidth=3, label=label, color=color)
    ax.fill(angles, values, alpha=0.1, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=15)
ax.set_ylim(0, 1)
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['0.25', '0.5', '0.75', '1.0'], size=14)
ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.0), fontsize=16)
ax.set_title('Agent Evaluation Dimensions', size=24, fontweight='bold', color=MLPURPLE, pad=20)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
