from fastapi import APIRouter, HTTPException

from src.schemas import PredictRequest, PredictResponse

from src.service.predictor import predict

router = APIRouter(prefix='/predict')


@router.post('', response_model=PredictResponse)
async def make_prediction(request: PredictRequest):
    try:
        prediction, model_version = predict(request=request)

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error)
        ) from error

    return {
        'prediction': prediction,
        'model_version': model_version
    }
