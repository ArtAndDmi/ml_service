from fastapi import APIRouter, HTTPException

from src.service import job_manager, run_train_container
from src.schemas import TrainResponse, TrainStatusResponse, TrainUpdateRequest

router = APIRouter(prefix='/train')


@router.post('', response_model=TrainResponse)
async def train():
    job = job_manager.create_job()

    run_train_container(job_id=job.job_id)

    return job


@router.get('/{job_id}', response_model=TrainStatusResponse)
async def train_status(job_id: str):
    job = job_manager.get_job(job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail='Training job not found'
        )

    return job


@router.patch('/{job_id}', response_model=TrainStatusResponse)
async def update_train(job_id: str, request: TrainUpdateRequest):
    job = job_manager.update_job(
        job_id=job_id,
        status=request.status,
        model_version=request.model_version
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail='Train job not found'
        )

    return job
