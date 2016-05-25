# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('ok_lib2.7*', '*.pyc', '*.pyo')
def test_ok_lib_2_7(test, sub_test):
    """test code is performed in data_driven_test"""
    pass


@pytest.mark.skipif("sys.version_info != (2,7)")
@data_driven_test('ok_lib2.7*', '*.py')
def test_ok_lib_2_7_source(test, sub_test):
    """test code is performed in data_driven_test"""
