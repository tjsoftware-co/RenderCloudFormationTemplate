"""
All tests for iam macros
"""

from .utils import _test_template


def test_alb_security_group():
    """
    Test if alx security group template is valid
    """
    _test_template('macros/ec2/alb_security_group.template')


def test_container_instances_security_group():
    """
    Test if alx security group template is valid
    """
    _test_template('macros/ec2/container_instances_security_group.template')

