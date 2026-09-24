import httpx

from src.config import settings


async def activate_model(model_id: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{settings.model_registry_url}/models/{model_id}/activate',
        )

    if response.is_error:
        raise RuntimeError(f'Model Registry error: {response.status_code}')

    return response.json()


async def get_models() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'{settings.model_registry_url}/models',
        )

    if response.is_error:
        raise RuntimeError(f'Model Registry error: {response.status_code}')

    return response.json()
