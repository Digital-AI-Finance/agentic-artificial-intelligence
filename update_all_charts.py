"""
Update all existing charts with proper font scaling and create new charts.
Font size 24pt base -> 14pt when displayed at 60%
"""
import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Standard font settings for 60% display scaling
FONT_SETTINGS = """plt.rcParams.update({
    'font.size': 24, 'axes.labelsize': 24, 'axes.titlesize': 26,
    'xtick.labelsize': 22, 'ytick.labelsize': 22, 'legend.fontsize': 22,
    'figure.figsize': (10, 6), 'figure.dpi': 150, 'font.family': 'sans-serif'
})"""

OLD_FONT_PATTERN = """plt.rcParams.update({
    'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
    'figure.figsize': (10, 6), 'figure.dpi': 150, 'font.family': 'sans-serif'
})"""

def update_chart_fonts():
    """Update font settings in all existing chart.py files."""
    chart_files = list(BASE_DIR.glob("L*/*/chart.py"))

    for chart_file in chart_files:
        content = chart_file.read_text(encoding='utf-8')
        if OLD_FONT_PATTERN in content:
            new_content = content.replace(OLD_FONT_PATTERN, FONT_SETTINGS)
            chart_file.write_text(new_content, encoding='utf-8')
            print(f"Updated: {chart_file}")
        elif "'font.size': 14" in content:
            # Handle slight variations
            new_content = content.replace("'font.size': 14", "'font.size': 24")
            new_content = new_content.replace("'axes.labelsize': 14", "'axes.labelsize': 24")
            new_content = new_content.replace("'axes.titlesize': 16", "'axes.titlesize': 26")
            new_content = new_content.replace("'xtick.labelsize': 13", "'xtick.labelsize': 22")
            new_content = new_content.replace("'ytick.labelsize': 13", "'ytick.labelsize': 22")
            new_content = new_content.replace("'legend.fontsize': 13", "'legend.fontsize': 22")
            chart_file.write_text(new_content, encoding='utf-8')
            print(f"Updated (variant): {chart_file}")

def regenerate_charts():
    """Regenerate all chart PDFs."""
    chart_files = list(BASE_DIR.glob("L*/*/chart.py"))

    for chart_file in chart_files:
        print(f"Regenerating: {chart_file}")
        subprocess.run(["python", str(chart_file)], cwd=chart_file.parent)

if __name__ == "__main__":
    print("Updating chart fonts...")
    update_chart_fonts()
    print("\nRegenerating charts...")
    regenerate_charts()
    print("\nDone!")
