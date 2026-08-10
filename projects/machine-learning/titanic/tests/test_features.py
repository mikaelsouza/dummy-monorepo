import pandas as pd

from model.features import FEATURE_COLUMNS, preprocess


def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Pclass": 3,
                "Sex": "male",
                "Age": None,
                "SibSp": 0,
                "Parch": 0,
                "Fare": None,
                "Embarked": None,
                "Survived": 0,
            },
            {
                "Pclass": 1,
                "Sex": "female",
                "Age": 30.0,
                "SibSp": 1,
                "Parch": 0,
                "Fare": 80.0,
                "Embarked": "C",
                "Survived": 1,
            },
        ]
    )


def test_preprocess_outputs_expected_columns():
    out = preprocess(sample_df())
    assert list(out.columns) == FEATURE_COLUMNS
    assert len(out) == 2


def test_preprocess_fills_missing_values():
    out = preprocess(sample_df())
    assert not out["Age"].isna().any()
    assert not out["Fare"].isna().any()
    assert not out["Embarked"].isna().any()


def test_preprocess_encodes_categoricals():
    out = preprocess(sample_df())
    assert set(out["Sex"]) == {0, 1}
    assert out.loc[1, "Embarked"] == 1  # "C"
    assert out.loc[1, "Sex"] == 1  # "female"
