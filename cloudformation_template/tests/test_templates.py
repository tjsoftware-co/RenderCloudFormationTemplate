"""
General tests for templates validation (check if valid json are returned
and if not if valid error is raised
"""

import json
import pytest

from .utils import _test_template


def test_valid_template():
    """
    Test if valid template is correct saved
    """
    _test_template('test.template')


def test_invalid_template():
    """
    Test if invalid template is rendered
    """
    with pytest.raises(json.JSONDecodeError):
        _test_template('test_error.template')
