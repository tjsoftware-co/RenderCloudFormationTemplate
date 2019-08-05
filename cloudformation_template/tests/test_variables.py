"""
Tests for checking if variables are read correctly from variables_dir
"""

import os
from cloudformation_template import CloudFormationTemplate


def test_collecting_variables():
    """
    Test of collecting variables from a variable dir
    """
    template_dir = os.path.join(os.path.dirname(__file__), 'test_templates')
    variables_dir = os.path.join(os.path.dirname(__file__), 'test_variables')

    cft = CloudFormationTemplate(template_dir=template_dir, variables_dir=variables_dir)
    assert sorted(cft.variables.keys()) == ['build', 'repositories', 'users']
