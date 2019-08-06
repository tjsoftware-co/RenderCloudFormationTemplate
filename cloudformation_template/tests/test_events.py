"""
All tests for codepipeline macros
"""

from .utils import _test_template


def test_codecommit_pipeline_rule_template():
    """
    Test if codecommit_pipeline_rule template is valid
    """
    _test_template('macros/events/codecommit_pipepline_rule.template')
