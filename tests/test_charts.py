"""
Unit tests for chart generation scripts.
Validates that all chart scripts run without errors and produce PDF output.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

# Project root directory
ROOT = Path(__file__).parent.parent


def discover_chart_scripts():
    """Find all chart Python files in lecture folders.

    Charts are named after their folder, e.g.:
    - 01_agent_definition/agent_definition.py
    - 02_react_paradigm/react_paradigm.py
    """
    charts = []
    for lesson_dir in ROOT.glob("L*_*"):
        if lesson_dir.is_dir():
            for chart_dir in lesson_dir.glob("*_*"):
                if chart_dir.is_dir():
                    # Extract expected name from folder (e.g., "01_agent_definition" -> "agent_definition")
                    match = re.match(r"^\d+[a-z]?_(.+)$", chart_dir.name)
                    if match:
                        chart_name = match.group(1)
                        chart_py = chart_dir / f"{chart_name}.py"
                        if chart_py.exists():
                            charts.append(chart_py)
    return sorted(charts)


CHART_SCRIPTS = discover_chart_scripts()


@pytest.mark.parametrize(
    "chart_path", CHART_SCRIPTS, ids=lambda p: f"{p.parent.parent.name}/{p.parent.name}"
)
def test_chart_generates_pdf(chart_path: Path, tmp_path: Path):
    """Test that chart script runs successfully and creates matching PDF."""
    chart_dir = chart_path.parent
    chart_name = chart_path.stem  # e.g., "agent_definition"
    expected_pdf = chart_dir / f"{chart_name}.pdf"

    # Run the chart script
    result = subprocess.run(
        [sys.executable, str(chart_path)],
        cwd=str(chart_dir),
        capture_output=True,
        text=True,
        timeout=60,
    )

    # Check script ran successfully
    assert (
        result.returncode == 0
    ), f"Script failed:\nstdout: {result.stdout}\nstderr: {result.stderr}"

    # Check PDF was created/updated
    assert expected_pdf.exists(), f"PDF not created: {expected_pdf}"

    # Verify PDF has content (> 1KB)
    assert expected_pdf.stat().st_size > 1024, f"PDF too small: {expected_pdf.stat().st_size} bytes"


def test_all_charts_discovered():
    """Verify we found a reasonable number of chart scripts."""
    assert len(CHART_SCRIPTS) >= 40, f"Expected 40+ charts, found {len(CHART_SCRIPTS)}"


def test_chart_script_has_docstring():
    """Check that chart scripts have documentation."""
    for chart_path in CHART_SCRIPTS[:5]:  # Sample first 5
        content = chart_path.read_text(encoding="utf-8")
        assert '"""' in content or "'''" in content, f"No docstring in {chart_path}"


def test_chart_uses_standard_colors():
    """Verify charts use the ML color palette."""
    ml_colors = ["MLPURPLE", "MLBLUE", "MLORANGE", "MLGREEN"]
    for chart_path in CHART_SCRIPTS[:5]:  # Sample first 5
        content = chart_path.read_text(encoding="utf-8")
        has_color = any(color in content for color in ml_colors)
        assert has_color, f"Chart {chart_path} doesn't use ML color palette"


def test_chart_saves_to_correct_location():
    """Verify charts save to Path(__file__).parent / '<name>.pdf'."""
    for chart_path in CHART_SCRIPTS[:5]:
        content = chart_path.read_text(encoding="utf-8")
        assert (
            "Path(__file__).parent" in content
        ), f"Chart {chart_path} may not save to correct location"
        # Verify it saves to a descriptive name (not chart.pdf)
        assert (
            f'"{chart_path.stem}.pdf"' in content or f"'{chart_path.stem}.pdf'" in content
        ), f"Chart {chart_path} should save to {chart_path.stem}.pdf"
