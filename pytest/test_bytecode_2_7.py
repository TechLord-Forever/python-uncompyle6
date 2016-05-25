# uncompyle6
from data_driven_test import data_driven_test


@data_driven_test('bytecode_2.7*', '*.pyc')
def test_bytecode_2_7(test, sub_test):
    """test code is performed in data_driven_test"""
    pass
