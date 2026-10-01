from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.pipeline import Pipeline

from src.config import settings


@dataclass
class ValidationMetrics:
    rmse: float
    mae: float
    r2: float


@dataclass
class ValidationResult:
    metrics: ValidationMetrics
    is_valid: bool


def validate_model(
    model: Pipeline,
    x_valid: pd.DataFrame,
    y_valid: pd.Series,
) -> ValidationResult:
    y_pred = model.predict(x_valid)

    mse = mean_squared_error(
        y_valid,
        y_pred,
    )

    metrics = ValidationMetrics(
        rmse=float(np.sqrt(mse)),
        mae=float(
            mean_absolute_error(
                y_valid,
                y_pred,
            )
        ),
        r2=float(
            r2_score(
                y_valid,
                y_pred,
            )
        ),
    )

    is_valid = metrics.r2 >= settings.model_min_r2

    return ValidationResult(
        metrics=metrics,
        is_valid=is_valid,
    )