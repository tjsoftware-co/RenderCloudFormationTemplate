"""
All tests for s3 macros
"""

from .utils import _test_template


def test_bucket_template():
    """
    Test if s3 bucket template is valid
    """
    _test_template('macros/s3/bucket.template')


def test_website_template():
    """
    Test if s3 bucket that create a hosted website is valid
    """
    _test_template('macros/s3/website.template')


def test_website_redirect_template():
    """
    Test if s3 bucket created correct website bucket that redirects all traffic to another bucket
    """
    _test_template('macros/s3/website_redirect.template')
