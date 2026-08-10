"""Train and persist a Titanic survival model.

The module is runnable as a script::

    PYTHONPATH=projects/machine-learning/titanic python -m model.train

It can also be packaged as a Pants ``pex_binary`` (see ``model/BUILD``).
"""

import argparse
import os

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from model.features import preprocess
from model.paths import DEFAULT_DATA_PATH, DEFAULT_MODEL_PATH


def train_model(
    csv_path: str,
    model_path: str,
    test_size: float = 0.2,
    random_state: int = 42,
) -> float:
    """Load the Titanic CSV, train a classifier, and persist it with joblib.

    Returns the accuracy of the model on the held-out test split.
    """
    df = pd.read_csv(csv_path)
    X = preprocess(df)
    y = df["Survived"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))

    os.makedirs(os.path.dirname(model_path) or ".", exist_ok=True)
    joblib.dump(model, model_path)
    return accuracy


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a Titanic survival model.")
    parser.add_argument("--data", default=DEFAULT_DATA_PATH, help="Path to titanic.csv")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL_PATH,
        help="Where the trained model artifact should be saved",
    )
    args = parser.parse_args()

    accuracy = train_model(args.data, args.model)
    print(f"Saved model to {args.model} (test accuracy={accuracy:.3f})")


if __name__ == "__main__":
    main()
