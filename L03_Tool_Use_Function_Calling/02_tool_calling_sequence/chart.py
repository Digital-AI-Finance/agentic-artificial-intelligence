"""
Tool Calling Sequence Diagram
Week 3 - Tool Use and Function Calling
Visualizes the flow of a function calling interaction
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.size': 24, 'axes.labelsize': 24, 'axes.titlesize': 26,
    'xtick.labelsize': 22, 'ytick.labelsize': 22, 'legend.fontsize': 22,
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

ax.text(5, 5.7, 'Function Calling Sequence', fontsize=15,
        fontweight='bold', ha='center', color=MLPURPLE)

# Lifelines
lifelines = [
    ('User', 1.5, MLPURPLE),
    ('Application', 4.0, MLBLUE),
    ('LLM API', 6.5, MLORANGE),
    ('Tool', 8.5, MLGREEN)
]

for name, x, color in lifelines:
    # Header box
    box = FancyBboxPatch((x - 0.6, 4.8), 1.2, 0.5,
                         boxstyle="round,pad=0.02", facecolor='white',
                         edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, 5.05, name, fontsize=10, ha='center', fontweight='bold', color=color)
    # Lifeline
    ax.plot([x, x], [0.5, 4.8], color=color, linestyle='--', linewidth=1.5, alpha=0.5)

# Messages (arrows)
messages = [
    (1.5, 4.0, 4.3, '1. User query', MLPURPLE),
    (4.0, 6.5, 3.8, '2. Send with tools', MLBLUE),
    (6.5, 4.0, 3.3, '3. tool_call response', MLORANGE),
    (4.0, 8.5, 2.8, '4. Execute tool', MLBLUE),
    (8.5, 4.0, 2.3, '5. Tool result', MLGREEN),
    (4.0, 6.5, 1.8, '6. Send result', MLBLUE),
    (6.5, 4.0, 1.3, '7. Final response', MLORANGE),
    (4.0, 1.5, 0.8, '8. Answer to user', MLBLUE),
]

for x1, x2, y, label, color in messages:
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
    mid_x = (x1 + x2) / 2
    offset = 0.15 if x2 > x1 else -0.15
    ax.text(mid_x, y + 0.12, label, fontsize=8, ha='center', color=MLGRAY)

# Activation boxes
activations = [
    (4.0, 3.6, 1.5, MLBLUE),  # App processing
    (6.5, 3.5, 0.5, MLORANGE),  # LLM first call
    (8.5, 2.5, 0.5, MLGREEN),  # Tool execution
    (6.5, 1.5, 0.5, MLORANGE),  # LLM second call
]

for x, y, h, color in activations:
    rect = Rectangle((x - 0.1, y), 0.2, h, facecolor=color, alpha=0.3, edgecolor=color)
    ax.add_patch(rect)

plt.tight_layout()
plt.savefig(Path(__file__).parent / 'chart.pdf', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print(f"Chart saved to {Path(__file__).parent / 'chart.pdf'}")
