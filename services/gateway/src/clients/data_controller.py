import httpx

from src.config import settings


timeout = httpx.Timeout(
    connect=5.0,
    read=60.0,
    write=60.0,
    pool=5.0,
)

async def upload_data(
        filename: str,
        content: bytes,
        content_type: str | None
) -> dict:
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(
            f'{settings.data_controller_url}/data/upload',
            files={
                'file': (
                    filename,
                    content,
                    content_type
                )
            }
        )

        response.raise_for_status()

        return response.json()
