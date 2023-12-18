import pytest
import polars
from serving import hello


@pytest.fixture
def a():
    return polars.DataFrame([[1]])


@pytest.fixture
def b():
    return polars.DataFrame([[2]])


def test_func(a, b):
    result = polars.DataFrame([[3]])
    assert hello.func(a, b).frame_equal(result)


def test_func_2(a, b):
    result = polars.DataFrame([[4]])
    assert not hello.func(a, b).frame_equal(result)
