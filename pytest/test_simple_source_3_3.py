# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


@pytest.mark.skipif("sys.version_info < (3,3)")
@data_driven_test('simple_source_3.3*', '*.py')
def test_simple_source_3_3():
    """test code is performed in data_driven_test"""
