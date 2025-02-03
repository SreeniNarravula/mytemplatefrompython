"""Unit tests for my_module.py."""

import project_name


def test_main():
    """Test main function."""
    project_name.main()


def test_version():
    """Test version function."""
    assert project_name.__version__ == '0.1.0'
