import json
import os
import pytest

from cloudformation_template import CloudFormationTemplate


def test_valid_template():
    """
    Test if valid template is correct saved
    """
    template_dir = os.path.join(os.path.dirname(__file__), 'test_templates')
    variables_dir = os.path.join(os.path.dirname(__file__), 'test_variables')

    cft = CloudFormationTemplate(template_dir=template_dir, variables_dir=variables_dir)
    template = cft.render_template('test.template')
    json.loads(template)


def test_invalid_template():
    """
    Test if invalid template is rendered
    """
    template_dir = os.path.join(os.path.dirname(__file__), 'test_templates')
    variables_dir = os.path.join(os.path.dirname(__file__), 'test_variables')

    cft = CloudFormationTemplate(template_dir=template_dir, variables_dir=variables_dir)
    template = cft.render_template('test_error.template')
    with pytest.raises(json.JSONDecodeError):
        json.loads(template)





