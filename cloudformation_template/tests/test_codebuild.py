"""
All tests for codebuild macros
"""

from .utils import _test_template


def test_codepipeline_build_template():
    """
    Test if codepipeline build template is valid
    """
    _test_template('macros/codebuild/codepipeline_build.template')


def test_codepipeline_build_with_variables_template():
    """
    Test if codepipeline build template is valid
    """
    _test_template('macros/codebuild/codepipeline_build_with_variables.template')
