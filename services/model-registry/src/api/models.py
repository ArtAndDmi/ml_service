from fastapi import APIRouter, File, UploadFile, HTTPException
import httpx

from src.enums import ModelStatus
from src.schemas import ModelUploadResponse, ModelActivateResponse, ModelListResponse
from src.service import register_model, activate_model, list_models

router = APIRouter(prefix='/models')


@router.post('', response_model=ModelUploadResponse)
async def upload_model(file: UploadFile = File(...),):
    content = await file.read()

    model_id = register_model(
        content=content
    )

    return {
        'model_id': model_id,
        'filename': file.filename,
        'status': ModelStatus.REGISTERED
    }


@router.get('', response_model=ModelListResponse)
async def get_models():
    return {
        'models': list_models()
    }


@router.post('/{model_id}/activate', response_model=ModelActivateResponse)
async def activate(model_id: str):
    try:
        activate_model(model_id=model_id)

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        ) from error

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail='Inference failed to load model'
        ) from error

    return {
        'model_id': model_id,
        'status': 'activated'
    }
