import pytest
from multiply import multiply


# счетчик: тест со списком - 1, тест с кортежем - 0, негативный тест - 0, тест с параметрами - 0
def test_multiply_list():
    test_list = [1, 2, 3, 4]
    assert multiply(test_list) == 24


# счетчик: тест со списком - 1, тест с кортежем - 1, негативный тест - 0, тест с параметрами - 0
def test_multiply_tuple():
    test_tuple = 1, 2, 3, 4
    assert multiply(test_tuple) == 24


negative_dataset = ['some str', [1, 2, 'a', 6]]


# счетчик: тест со списком - 2, тест с кортежем - 1, негативный тест - 1, тест с параметрами - 1
def test_negative():
    for test_data in negative_dataset:
        try:
            assert multiply(test_data)
        except TypeError:
            pass


# счетчик: тест со списком - 2, тест с кортежем - 2, негативный тест - 1, тест с параметрами - 1
def test_empty():
    test_tuple = ()
    assert multiply(test_tuple) is None


# счетчик: тест со списком - 3, тест с кортежем - 2, негативный тест - 1, тест с параметрами - 1
def test_one_value():
    test_list = [8]
    assert multiply(test_list) is None
