# pytest
import pytest
# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('ok_lib3.3*', '*.pyc', '*.pyo')
def test_ok_lib_3_3():
    """test code is performed in data_driven_test"""


@pytest.mark.skipif("sys.version_info != (3,3)")
@data_driven_test('ok_lib3.3*', '*.py')
def test_ok_lib_3_3_source():
    """test code is performed in data_driven_test"""
