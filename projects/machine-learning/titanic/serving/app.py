"""FastAPI application exposing a Titanic survival prediction endpoint.

Run it locally from the repo root with::

    PYTHONPATH=projects/machine-learning/titanic uvicorn serving.app:app

The trained model artifact is expected at ``TITANIC_MODEL_PATH`` (defaults to
``projects/machine-learning/titanic/data/titanic_model.joblib``).
"""

import os

import joblib
import pandas as pd
from calculator import add
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from model.features import preprocess
from model.paths import DEFAULT_MODEL_PATH

app = FastAPI(title="Titanic Survival Prediction")

MODEL_PATH = os.environ.get("TITANIC_MODEL_PATH", DEFAULT_MODEL_PATH)
_model = None


class Passenger(BaseModel):
    Pclass: int = Field(..., ge=1, le=3)
    Sex: str = Field(..., pattern="^(male|female)$")
    Age: float = Field(..., ge=0)
    SibSp: int = Field(0, ge=0)
    Parch: int = Field(0, ge=0)
    Fare: float = Field(..., ge=0)
    Embarked: str = Field("S", pattern="^(S|C|Q)$")


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(
            status_code=503,
            detail=(
                f"No model found at {MODEL_PATH}. Run the training script first "
                "(e.g. PYTHONPATH=projects/machine-learning/titanic "
                "python -m model.train)."
            ),
        )
    return joblib.load(MODEL_PATH)


def get_model():
    global _model
    if _model is None:
        _model = load_model()
    return _model


@app.get("/health")
def health() -> dict:
    # The `calculator` shared-lib is exercised here to show cross-package imports.
    return {"status": "ok", "checksum": add.add(1, 2)}


@app.post("/predict")
def predict(passenger: Passenger) -> dict:
    model = get_model()
    row = {
        "Pclass": passenger.Pclass,
        "Sex": passenger.Sex,
        "Age": passenger.Age,
        "SibSp": passenger.SibSp,
        "Parch": passenger.Parch,
        "Fare": passenger.Fare,
        "Embarked": passenger.Embarked,
    }
    features = preprocess(pd.DataFrame([row]))
    survived = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])
    return {"survived": survived, "probability": probability}
