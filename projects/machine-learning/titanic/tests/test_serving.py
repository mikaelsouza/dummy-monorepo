import pandas as pd

from model.train import train_model
from serving import app as serving_app
from tests.test_train import mini_titanic_df


def test_health_endpoint():
    result = serving_app.health()
    assert result["status"] == "ok"
    assert result["checksum"] == 3


def test_predict_returns_expected_shape(tmp_path, monkeypatch):
    csv_path = tmp_path / "titanic.csv"
    mini_titanic_df().to_csv(csv_path, index=False)

    model_path = tmp_path / "titanic_model.joblib"
    accuracy = train_model(
        str(csv_path), str(model_path), test_size=0.5, random_state=0
    )
    assert 0.0 <= accuracy <= 1.0

    monkeypatch.setattr(serving_app, "MODEL_PATH", str(model_path))
    monkeypatch.setattr(serving_app, "_model", None)

    passenger = serving_app.Passenger(
        Pclass=3, Sex="male", Age=22.0, SibSp=1, Parch=0, Fare=7.25, Embarked="S"
    )
    result = serving_app.predict(passenger)

    assert set(result) == {"survived", "probability"}
    assert result["survived"] in (0, 1)
    assert 0.0 <= result["probability"] <= 1.0
