"""Test file for runner test task."""
from pathlib import Path


def test_readme_title():
    """Test that README has correct title."""
    readme_path = Path(__file__).parent / "README.md"
    with open(readme_path, "r") as f:
        content = f.read()
        assert "Transportation" in content
        assert "Transposrtation" not in content
