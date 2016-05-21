# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('bytecode_3.2*', '*.pyc')
def test_bytecode_3_2(test, sub_test):
    """test code is performed in data_driven_test"""
