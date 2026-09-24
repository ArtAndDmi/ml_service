from pathlib import Path

import httpx

from src.config import settings


def register_model(
    artifact_path: Path,
) -> str:
    with artifact_path.open('rb') as file:
        response = httpx.post(
            f'{settings.model_registry_url}/models',
            files={
                'file': (
                    artifact_path.name,
                    file,
                    'application/octet-stream',
                ),
            },
        )

    response.raise_for_status()

    result = response.json()

    return result['model_id']