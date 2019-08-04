"""
All tests for iam macros
"""

from .utils import _test_template


def test_role_template():
    """
    Test if valid template is correct saved
    """
    _test_template('macros/iam/role.template')
