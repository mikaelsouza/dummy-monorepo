import polars
from calculator import add


def func(a: polars.DataFrame, b: polars.DataFrame) -> polars.DataFrame:
    return a + b


data = polars.DataFrame([1, 2, 3])
func(data, data)
print(data)
print(add.add(1, 2))
