import httpx

from src.config import settings
from src.schemas import PredictRequest


async def predict(request: PredictRequest) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{settings.inference_url}/predict',
            json=request.model_dump()
        )

    if response.is_error:
        raise RuntimeError(f'Inference error: {response.status_code}')

    return response.json()
