import json
from pathlib import Path

from src.config import settings


ACTIVE_MODEL_FILENAME = 'active_model.json'


def get_active_model_id() -> str | None:
    path = Path(settings.model_storage_path) / ACTIVE_MODEL_FILENAME

    if not path.exists():
        return None

    with path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    return data.get('active_model_id')


def save_active_model_id(model_id: str) -> None:
    path = Path(settings.model_storage_path) / ACTIVE_MODEL_FILENAME

    with path.open('w', encoding='utf-8') as file:
        json.dump(
            {
                'active_model_id': model_id
            },
            file
        )