from fastapi import APIRouter, HTTPException

from src.clients.inference import predict
from src.schemas import PredictRequest, PredictResponse

router = APIRouter(prefix='/predict')


@router.post('', response_model=PredictResponse)
async def make_prediction(request: PredictRequest):
    try:
        return await predict(request=request)

    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error)
        ) from error
