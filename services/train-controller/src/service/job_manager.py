import uuid

from src.schemas import TrainResponse, TrainStatusResponse
from src.enums import JobStatus


class JobManager:
    def __init__(self):
        self.jobs: dict[str, TrainStatusResponse] = {}

    def create_job(self) -> TrainResponse:
        job_id = str(uuid.uuid4())

        job = TrainStatusResponse(
            job_id=job_id,
            status=JobStatus.CREATED,
            model_version=None
        )

        self.jobs[job_id] = job

        return TrainResponse(
            job_id=job_id,
            status=JobStatus.CREATED
        )

    def update_job(
            self,
            job_id: str,
            status: JobStatus,
            model_version: str | None = None,
            error: str | None = None
    ) -> TrainStatusResponse | None:
        job = self.jobs.get(job_id)

        if job is None:
            return None

        updated_job = TrainStatusResponse(
            job_id=job_id,
            status=status,
            model_version=(
                model_version
                if model_version is not None
                else job.model_version
            ),
            error=error
        )

        self.jobs[job_id] = updated_job

        return updated_job

    def get_job(self, job_id: str) -> TrainStatusResponse | None:
        return self.jobs.get(job_id)


job_manager = JobManager()
