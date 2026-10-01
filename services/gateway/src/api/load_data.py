from typing import Annotated

from fastapi import APIRouter, File, UploadFile

from src.clients.data_controller import upload_data
from src.schemas import LoadDataResponse

router = APIRouter(prefix='/data')


@router.post('/replace', response_model=LoadDataResponse)
async def replace_data(
        file: Annotated[UploadFile, File()]
):
    content = await file.read()

    result = await upload_data(
        endpoint='/data/replace',
        filename=file.filename,
        content=content,
        content_type=file.content_type
    )

    return result


@router.post('/append', response_model=LoadDataResponse)
async def append_data(
        file: Annotated[UploadFile, File()]
):
    content = await file.read()

    result = await upload_data(
        endpoint='/data/append',
        filename=file.filename,
        content=content,
        content_type=file.content_type
    )

    return result
