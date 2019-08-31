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


def test_vpc():
    """
    Test if vpc  template is valid
    """
    _test_template('macros/ec2/vpc.template')


def test_internet_gateway():
    """
    Test if internet gateway template is valid
    """
    _test_template('macros/ec2/internet_gateway.template')


def test_internet_gateway_attachment():
    """
    Test if internet gateway attachment template is valid
    """
    _test_template('macros/ec2/internet_gateway_attachment.template')


def test_subnet():
    """
    Test if subnet template is valid
    """
    _test_template('macros/ec2/subnet.template')
