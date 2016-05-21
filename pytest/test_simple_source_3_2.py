# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


@pytest.mark.skipif("sys.version_info < (3,2)")
@data_driven_test('simple_source_3.2*', '*.py')
def test_simple_source_3_2():
    """test code is performed in data_driven_test"""
