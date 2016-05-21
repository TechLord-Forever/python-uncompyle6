# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('ok_lib3.2*', '*.pyc', '*.pyo')
def test_ok_lib_3_2():
    """test code is performed in data_driven_test"""


@pytest.mark.skipif("sys.version_info != (3,2)")
@data_driven_test('ok_lib3.2*', '*.py')
def test_ok_lib_3_2_source():
    """test code is performed in data_driven_test"""
