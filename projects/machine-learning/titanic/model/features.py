"""Feature engineering helpers for the Titanic survival task.

``preprocess`` turns a raw Titanic dataframe (as produced by the dataset
downloaded via ``scripts/get-dataset.sh``) into a numeric feature matrix that
can be fed straight into a scikit-learn model. It is shared by the training
script and the serving application so both apply exactly the same
transformation.
"""

import pandas as pd

FEATURE_COLUMNS = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

SEX_MAP = {"male": 0, "female": 1}
EMBARKED_MAP = {"S": 0, "C": 1, "Q": 2}
DEFAULT_EMBARKED = "S"


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Return a numeric, feature-only dataframe ready for a scikit-learn model.

    * Missing ``Age`` / ``Fare`` are filled with the column median.
    * Missing ``Embarked`` is filled with the most common value (``"S"``).
    * ``Sex`` and ``Embarked`` are encoded as integers.
    """
    data = df.copy()
    data["Age"] = data["Age"].fillna(data["Age"].median())
    data["Fare"] = data["Fare"].fillna(data["Fare"].median())
    data["Embarked"] = data["Embarked"].fillna(DEFAULT_EMBARKED)
    data["Sex"] = data["Sex"].map(SEX_MAP).fillna(0).astype(int)
    data["Embarked"] = data["Embarked"].map(EMBARKED_MAP).fillna(0).astype(int)
    return data[FEATURE_COLUMNS]
