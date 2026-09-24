from pydantic import BaseModel
from src.enums import JobStatus


class TrainResponse(BaseModel):
    job_id: str
    status: JobStatus


class TrainStatusResponse(BaseModel):
    job_id: str
    status: JobStatus
    model_version: str | None = None


from pydantic import BaseModel, model_validator

from src.enums.job_status import JobStatus


class TrainUpdateRequest(BaseModel):
    status: JobStatus
    model_version: str | None = None

    @model_validator(mode='after')
    def validate_model_version(self):
        if (
                self.status == JobStatus.COMPLETED
                and self.model_version is None
        ):
            raise ValueError(
                'model_version is required for completed status'
            )

        return self
