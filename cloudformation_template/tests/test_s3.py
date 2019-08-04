from .utils import _test_template


def test_bucket_template():
    """
    Test if valid template is correct saved
    """
    _test_template('macros/s3/bucket.template')
