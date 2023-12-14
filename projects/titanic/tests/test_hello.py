import pytest
from serving import hello


@pytest.fixture
def a():
    return 1


@pytest.fixture
def b():
    return 2


def test_func(a, b):
    assert hello.func(a, b) == 3
