import joblib
from sklearn.pipeline import Pipeline

from src.config import settings
from src.state.model_state import model_state

MODEL_FILENAME = 'model.joblib'


def load_model(model_id: str) -> None:
    model_path = (settings.model_storage_path / model_id / MODEL_FILENAME)

    if not model_path.exists():
        raise FileNotFoundError(f'Model {model_id} not found')

    loaded_model = joblib.load(model_path)

    if not isinstance(loaded_model, Pipeline):
        raise TypeError('Loaded object is not sklearn Pipeline')

    model_state.model = loaded_model
    model_state.model_id = model_id
