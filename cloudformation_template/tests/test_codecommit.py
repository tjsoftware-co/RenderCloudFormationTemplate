"""
All tests for codecommit macros
"""

from .utils import _test_template


def test_repository_template():
    """
    Test if codecommit repository template is valid
    """
    _test_template('macros/codecommit/repository.template')
