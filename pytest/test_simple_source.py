# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('simple_source/*', '*.py')
def test_simple_source():
    """test code is performed in data_driven_test"""
