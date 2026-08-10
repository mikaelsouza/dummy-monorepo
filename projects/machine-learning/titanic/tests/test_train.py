import os

import joblib
import pandas as pd

from model.features import preprocess
from model.train import train_model


def mini_titanic_df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"Pclass": 3, "Sex": "male", "Age": 22.0, "SibSp": 1, "Parch": 0, "Fare": 7.25, "Embarked": "S", "Survived": 0},
            {"Pclass": 1, "Sex": "female", "Age": 38.0, "SibSp": 1, "Parch": 0, "Fare": 71.28, "Embarked": "C", "Survived": 1},
            {"Pclass": 3, "Sex": "male", "Age": 26.0, "SibSp": 0, "Parch": 0, "Fare": 7.92, "Embarked": "S", "Survived": 0},
            {"Pclass": 1, "Sex": "female", "Age": 35.0, "SibSp": 0, "Parch": 1, "Fare": 53.10, "Embarked": "S", "Survived": 1},
            {"Pclass": 3, "Sex": "male", "Age": 35.0, "SibSp": 0, "Parch": 0, "Fare": 8.05, "Embarked": "S", "Survived": 0},
            {"Pclass": 2, "Sex": "female", "Age": 28.0, "SibSp": 0, "Parch": 0, "Fare": 13.00, "Embarked": "Q", "Survived": 1},
        ]
    )


def test_train_model_creates_usable_artifact(tmp_path):
    csv_path = tmp_path / "titanic.csv"
    mini_titanic_df().to_csv(csv_path, index=False)

    model_path = tmp_path / "titanic_model.joblib"
    accuracy = train_model(str(csv_path), str(model_path), test_size=0.5, random_state=0)

    assert os.path.exists(model_path)
    assert 0.0 <= accuracy <= 1.0

    model = joblib.load(model_path)
    sample = preprocess(
        pd.DataFrame(
            [{"Pclass": 3, "Sex": "male", "Age": 22.0, "SibSp": 1, "Parch": 0, "Fare": 7.25, "Embarked": "S"}]
        )
    )
    assert model.predict(sample).shape == (1,)
