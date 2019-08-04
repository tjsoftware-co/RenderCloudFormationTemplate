"""
All tests for codecommit macros
"""

from .utils import _test_template


def test_repository_template():
    """
    Test if valid template is correct saved
    """
    _test_template('macros/codecommit/repository.template')
