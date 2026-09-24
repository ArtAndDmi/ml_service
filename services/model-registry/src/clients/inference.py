import httpx

from src.config import settings


def activate_model(model_id: str) -> None:
    response = httpx.post(
        f'{settings.inference_url}/model/{model_id}/reload',
    )

    response.raise_for_status()