"""Test file for runner test task."""


def test_readme_title():
    """Test that README has correct title."""
    with open("README.md", "r") as f:
        content = f.read()
        assert "Transportation" in content
        assert "Transposrtation" not in content
