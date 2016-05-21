# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('ok_lib2.6*', '*.pyc', '*.pyo')
def test_ok_lib_2_6():
    """test code is performed in data_driven_test"""


@pytest.mark.skipif("sys.version_info != (2,6)")
@data_driven_test('ok_lib2.6*', '*.py')
def test_ok_lib_2_6_source():
    """test code is performed in data_driven_test"""
