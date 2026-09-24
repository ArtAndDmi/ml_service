import pandas as pd

from src.schemas import PredictRequest
from src.state.model_state import model_state


def predict(request: PredictRequest) -> tuple[float, str]:
    if model_state.model is None:
        raise RuntimeError('Active model is not loaded')

    if model_state.model_id is None:
        raise RuntimeError('Active model id is not set')

    data = pd.DataFrame([
        request.model_dump()
    ])

    prediction = model_state.model.predict(data)

    return (
        float(prediction[0]),
        model_state.model_id
    )
