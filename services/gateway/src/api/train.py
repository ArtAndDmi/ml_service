from fastapi import APIRouter

from src.schemas import TrainResponse, TrainStatusResponse
from src.clients.train_controller import create_train, get_train_status

router = APIRouter(prefix='/train')


@router.post('', response_model=TrainResponse)
async def train():
    result = await create_train()
    return result


@router.get('/{job_id}', response_model=TrainStatusResponse)
async def train_status(job_id: str):
    result = await get_train_status(job_id)
    return result
