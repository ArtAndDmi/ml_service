from typing import Annotated

from fastapi import APIRouter, UploadFile, File

from src.clients.data_controller import upload_data
from src.schemas import LoadDataResponse

router = APIRouter(prefix='/load-data')


@router.post('', response_model=LoadDataResponse)
async def load_data(file: Annotated[UploadFile, File()]):
    content = await file.read()

    result = await upload_data(
        filename=file.filename,
        content=content,
        content_type=file.content_type
    )

    return result
