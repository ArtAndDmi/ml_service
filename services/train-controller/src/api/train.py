from fastapi import APIRouter, HTTPException, BackgroundTasks

from src.enums import JobStatus
from src.service.job_manager import job_manager
from src.service.docker_runner import run_train_container
from src.schemas import TrainResponse, TrainStatusResponse, TrainUpdateRequest

router = APIRouter(prefix='/train')


def start_training_job(job_id: str) -> None:
    try:
        run_train_container(job_id=job_id)

        job_manager.update_job(
            job_id=job_id,
            status=JobStatus.RUNNING
        )

    except Exception:
        job_manager.update_job(
            job_id=job_id,
            status=JobStatus.FAILED
        )


@router.post('', response_model=TrainResponse)
async def train(background_tasks: BackgroundTasks):
    job = job_manager.create_job()

    background_tasks.add_task(
        start_training_job,
        job.job_id
    )

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
