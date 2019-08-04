import json
import os

from cloudformation_template import CloudFormationTemplate


def test_cloudformation_pipeline_template():
    """
    Test if valid template is correct saved
    """
    template_dir = os.path.join(os.path.dirname(__file__), 'test_templates')
    variables_dir = os.path.join(os.path.dirname(__file__), 'test_variables')

    cft = CloudFormationTemplate(template_dir=template_dir, variables_dir=variables_dir)
    template = cft.render_template('macros/codepipeline/cloudformation_pipeline.template')
    json.loads(template)
