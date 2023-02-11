import pytest

cnt = 0


@pytest.fixture(autouse=True)
def clean_test_file():
    global cnt
    with open('product_test_file.txt', 'w'):
        pass
    cnt += 1
