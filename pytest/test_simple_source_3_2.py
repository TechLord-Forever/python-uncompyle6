# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


# FIXME: Probably should split the source tests into python versions, so that
# we can do skipif on versions where the compilation is known to fail, for
# example due py2/py3 differences.


@pytest.mark.skipif("sys.version_info < (3,3)")
@data_driven_test('simple_source_3.3*', '*.py')
def test_simple_source_3_3(test, sub_test):
    """test code is performed in data_driven_test"""
