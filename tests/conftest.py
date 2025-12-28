"""Pytest configuration for chart tests."""
import pytest


def pytest_configure(config):
    """Add custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )


@pytest.fixture(scope="session")
def project_root():
    """Return project root directory."""
    from pathlib import Path
    return Path(__file__).parent.parent
