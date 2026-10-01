import httpx
from fastapi import HTTPException

from src.config import settings


timeout = httpx.Timeout(
    connect=5.0,
    read=60.0,
    write=60.0,
    pool=5.0,
)


async def upload_data(
        endpoint: str,
        filename: str,
        content: bytes,
        content_type: str | None
) -> dict:
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(
            f'{settings.data_controller_url}{endpoint}',
            files={
                'file': (
                    filename,
                    content,
                    content_type
                )
            }
        )

        if response.is_error:
            detail = response.json().get(
                'detail',
                'Data Controller request failed'
            )

            raise HTTPException(
                status_code=response.status_code,
                detail=detail
            )

        return response.json()