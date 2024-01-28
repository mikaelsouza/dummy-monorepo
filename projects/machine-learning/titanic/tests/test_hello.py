import pytest
import pandas
from serving import hello


@pytest.fixture
def a():
    return pandas.DataFrame([[1]])


@pytest.fixture
def b():
    return pandas.DataFrame([[2]])


def test_func(a, b):
    result = pandas.DataFrame([[3]])
    assert hello.func(a, b).equals(result)


def test_func_2(a, b):
    result = pandas.DataFrame([[4]])
    assert not hello.func(a, b).equals(result)
