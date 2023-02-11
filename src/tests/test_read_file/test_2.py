import pytest

from src.lesson_1 import read_file


def create_test_data(test_data):
    with open('product_test_file.txt', 'a') as file:
        file.writelines(test_data)


@pytest.mark.parametrize("path, result", [('product_test_file.txt',
                                           ['hello\n', 'world\n', '1\n', '2\n', '3\n'])])
def test_correct_path(path, result):
    test_data = ['hello\n', 'world\n', '1\n', '2\n', '3\n']
    create_test_data(test_data)
    assert read_file(path) == result


#@pytest.mark.parametrize("path, result", [('product_test_file.txt',
#                                           ['hello\n', 'world\n', '1\n', '2\n', '3\n'])])
def test_correct_path_2():
    test_data = ['hello\n', 'world\n', '244\n', '1\n', '2\n', '3\n']
    create_test_data(test_data)
    assert read_file('product_test_file.txt') == test_data
