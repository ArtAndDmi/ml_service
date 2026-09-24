from pydantic import BaseModel


class TrainResponse(BaseModel):
    job_id: str
    status: str


class TrainStatusResponse(BaseModel):
    job_id: str
    status: str
    model_version: str | None = None
