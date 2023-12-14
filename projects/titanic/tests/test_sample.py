import pytest
from serving import hello


@pytest.fixture
def a():
    return 1


@pytest.fixture
def b():
    return 2


def test_func_3(a, b):
    assert hello.func(a, b) != 5
