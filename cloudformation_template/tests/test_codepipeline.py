"""
All tests for codepipeline macros
"""

from .utils import _test_template


def test_cloudformation_pipeline_template():
    """
    Test if cloudformation_pipeline template is valid
    """
    _test_template('macros/codepipeline/cloudformation_pipeline.template')


def test_codecommit_to_s3_template():
    """
    Test if codecommit_to_s3 template is valid
    """
    _test_template('macros/codepipeline/codecommit_to_s3.template')
