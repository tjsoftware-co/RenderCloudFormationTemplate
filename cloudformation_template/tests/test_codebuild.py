"""
All tests for codebuild macros
"""

from .utils import _test_template


def test_codepipeline_build_template():
    """
    Test if valid template is correct saved
    """
    _test_template('macros/codebuild/codepipeline_build.template')
