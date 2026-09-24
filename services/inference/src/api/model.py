from fastapi import APIRouter, HTTPException

from src.schemas import ModelReloadResponse
from src.service import load_model

router = APIRouter(prefix='/model')


@router.post('/{model_id}/reload', response_model=ModelReloadResponse)
async def reload_model(model_id: str):
    try:
        load_model(model_id=model_id)

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        ) from error

    except TypeError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error)
        ) from error

    return {
        'model_id': model_id,
        'status': 'activated'
    }
