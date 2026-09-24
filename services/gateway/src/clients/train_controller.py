import httpx
from fastapi import HTTPException

from src.config import settings


async def create_train() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{settings.train_controller_url}/train',
        )

    if response.is_error:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json().get(
                'detail',
                'Train controller error'
            )
        )

    return response.json()


async def get_train_status(job_id: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'{settings.train_controller_url}/train/{job_id}',
        )

    if response.is_error:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json().get(
                'detail',
                'Train controller error'
            )
        )

    return response.json()
