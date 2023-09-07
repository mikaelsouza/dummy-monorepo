import numpy
import polars


def array_addition(m: polars.DataFrame, n: polars.DataFrame) -> polars.DataFrame:
    return m + n


def main() -> None:
    data = numpy.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2],
        ]
    )
    data_df = polars.DataFrame(data, schema=["a", "b", "c", "d"])

    print(data_df)
    print(array_addition(data_df, data_df))


if __name__ == "__main__":
    main()
