import pytest

from src.enums import JobStatus
from src.service.job_manager import job_manager


@pytest.fixture(autouse=True)
def clear_jobs():
    job_manager.jobs.clear()

    yield

    job_manager.jobs.clear()


def test_create_job():
    job = job_manager.create_job()

    assert job.job_id
    assert job.status == JobStatus.CREATED


def test_get_existing_job():
    created_job = job_manager.create_job()

    job = job_manager.get_job(
        created_job.job_id
    )

    assert job is not None
    assert job.job_id == created_job.job_id
    assert job.status == JobStatus.CREATED


def test_get_unknown_job():
    job = job_manager.get_job(
        'unknown-job-id'
    )

    assert job is None


def test_update_job_status():
    job = job_manager.create_job()

    updated_job = job_manager.update_job(
        job_id=job.job_id,
        status=JobStatus.RUNNING,
    )

    assert updated_job is not None
    assert updated_job.job_id == job.job_id
    assert updated_job.status == JobStatus.RUNNING
    assert updated_job.model_version is None


def test_update_job_with_model_version():
    job = job_manager.create_job()

    updated_job = job_manager.update_job(
        job_id=job.job_id,
        status=JobStatus.COMPLETED,
        model_version='model-123',
    )

    assert updated_job is not None
    assert updated_job.status == JobStatus.COMPLETED
    assert updated_job.model_version == 'model-123'


def test_update_unknown_job():
    updated_job = job_manager.update_job(
        job_id='unknown-job-id',
        status=JobStatus.FAILED,
    )

    assert updated_job is None