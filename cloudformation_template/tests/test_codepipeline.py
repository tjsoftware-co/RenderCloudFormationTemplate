"""
All tests for codepipeline macros
"""

from .utils import _test_template


def test_cloudformation_pipeline_template():
    """
    Test if valid template is correct saved
    """
    _test_template('macros/codepipeline/cloudformation_pipeline.template')
