from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from ml_common.model.factory import create_model
from sklearn.pipeline import Pipeline

TARGET_COLUMN = 'price'
TEST_SIZE = 0.2
RANDOM_STATE = 42


@dataclass
class TrainResult:
    model: Pipeline
    x_valid: pd.DataFrame
    y_valid: pd.Series


def train_model(
        data: pd.DataFrame,
) -> TrainResult:
    x = data.drop(
        columns=[TARGET_COLUMN],
    )

    y = data[TARGET_COLUMN]

    x_train, x_valid, y_train, y_valid = train_test_split(
        x,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    model = create_model()

    model.fit(
        x_train,
        y_train,
    )

    return TrainResult(
        model=model,
        x_valid=x_valid,
        y_valid=y_valid,
    )
