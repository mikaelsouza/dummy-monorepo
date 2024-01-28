import pandas
from calculator import add


def func(a: pandas.DataFrame, b: pandas.DataFrame) -> pandas.DataFrame:
    return a + b


data = pandas.DataFrame([1, 2, 3])
func(data, data)
print(data)
print(add.add(1, 2))
