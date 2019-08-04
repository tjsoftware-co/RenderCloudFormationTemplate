"""
Helper functions for tests
"""

import json
import os

from cloudformation_template import CloudFormationTemplate


def _test_template(template_name):
    """
    Test if provided template can render without an error
    """
    template_dir = os.path.join(os.path.dirname(__file__), 'test_templates')
    variables_dir = os.path.join(os.path.dirname(__file__), 'test_variables')

    cft = CloudFormationTemplate(template_dir=template_dir, variables_dir=variables_dir)
    template = cft.render_template(template_name=template_name)
    json.loads(template)
