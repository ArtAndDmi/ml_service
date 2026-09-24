from pathlib import Path
from uuid import uuid4

from src.config import settings

MODEL_STORAGE_PATH = Path(settings.model_storage_path)
MODEL_FILENAME = 'model.joblib'


def save_model(content: bytes) -> tuple[str, Path]:
    model_id = str(uuid4())

    model_dir = MODEL_STORAGE_PATH / model_id
    model_dir.mkdir(
        parents=True,
        exist_ok=False
    )

    model_path = model_dir / MODEL_FILENAME
    model_path.write_bytes(content)

    return model_id, model_path


def get_models() -> list[str]:
    if not MODEL_STORAGE_PATH.exists():
        return []

    return [
        item.name
        for item in MODEL_STORAGE_PATH.iterdir()
        if item.is_dir()
    ]


def model_exists(model_id: str) -> bool:
    model_dir = MODEL_STORAGE_PATH / model_id
    return model_dir.is_dir()
