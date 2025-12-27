"""
Communication Topology Diagram
Week 5 - Multi-Agent Architectures
Shows different multi-agent communication patterns
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
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

fig, axes = plt.subplots(1, 3, figsize=(10, 4))

def draw_agent(ax, x, y, label, color):
    circle = Circle((x, y), 0.3, facecolor=color, edgecolor='white', linewidth=2, alpha=0.8)
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Topology 1: Centralized (Star)
ax1 = axes[0]
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Centralized (Star)', fontsize=12, fontweight='bold', color=MLPURPLE)

# Central orchestrator
draw_agent(ax1, 0, 0, 'O', MLPURPLE)
# Worker agents
positions = [(1.2, 0.7), (1.2, -0.7), (-1.2, 0.7), (-1.2, -0.7), (0, 1.3)]
for i, (x, y) in enumerate(positions):
    draw_agent(ax1, x, y, f'A{i+1}', MLBLUE)
    ax1.annotate('', xy=(x*0.7, y*0.7), xytext=(x*0.85, y*0.85),
                arrowprops=dict(arrowstyle='<->', color=MLGRAY, lw=1.5))

# Topology 2: Hierarchical
ax2 = axes[1]
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('Hierarchical', fontsize=12, fontweight='bold', color=MLPURPLE)

# Top level
draw_agent(ax2, 0, 1.2, 'M', MLPURPLE)
# Middle level
draw_agent(ax2, -0.9, 0, 'S1', MLORANGE)
draw_agent(ax2, 0.9, 0, 'S2', MLORANGE)
# Bottom level
for i, x in enumerate([-1.3, -0.5, 0.5, 1.3]):
    draw_agent(ax2, x, -1.2, f'W{i+1}', MLGREEN)

# Arrows
ax2.annotate('', xy=(-0.7, 0.3), xytext=(-0.2, 0.9),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))
ax2.annotate('', xy=(0.7, 0.3), xytext=(0.2, 0.9),
            arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1.5))
for x1, x2 in [(-1.3, -0.9), (-0.5, -0.9), (0.5, 0.9), (1.3, 0.9)]:
    ax2.annotate('', xy=(x1, -0.9), xytext=(x2, -0.3),
                arrowprops=dict(arrowstyle='->', color=MLGRAY, lw=1))

# Topology 3: Peer-to-Peer (Mesh)
ax3 = axes[2]
ax3.set_xlim(-2, 2)
ax3.set_ylim(-2, 2)
ax3.set_aspect('equal')
ax3.axis('off')
ax3.set_title('Peer-to-Peer (Mesh)', fontsize=12, fontweight='bold', color=MLPURPLE)

# All agents at same level
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
mesh_positions = [(1.1*np.cos(a), 1.1*np.sin(a)) for a in angles]

for i, (x, y) in enumerate(mesh_positions):
    draw_agent(ax3, x, y, f'P{i+1}', MLBLUE)

# Connect all pairs (mesh)
for i, (x1, y1) in enumerate(mesh_positions):
    for j, (x2, y2) in enumerate(mesh_positions):
        if i < j:
            ax3.plot([x1*0.75, x2*0.75], [y1*0.75, y2*0.75],
                    color=MLGRAY, alpha=0.3, lw=1)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
