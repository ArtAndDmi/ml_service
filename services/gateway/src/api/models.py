from fastapi import APIRouter, HTTPException

from src.clients.model_registry import activate_model, get_models

router = APIRouter(prefix='/models')


@router.get('')
async def list_models():
    try:
        return await get_models()

    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error)
        ) from error


@router.post('/{model_id}/activate')
async def activate(model_id: str):
    try:
        return await activate_model(model_id=model_id)

    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error)
        ) from error
