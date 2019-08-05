"""
All tests for iam macros
"""

from .utils import _test_template


def test_role_template():
    """
    Test if role template is valid
    """
    _test_template('macros/iam/role.template')


def test_user_template():
    """
    Test if user template is valid
    """
    _test_template('macros/iam/user.template')


def test_group_template():
    """
    Test if group template is valid
    """
    _test_template('macros/iam/group.template')


def test_policy_template():
    """
    Test if policy template is valid
    """
    _test_template('macros/iam/policy.template')


def test_codecommit_repository_policy_template():
    """
    Test if policy for codecommit repository is correctly rendered
    """
    _test_template('macros/iam/codecommit_repository_policy.template')
