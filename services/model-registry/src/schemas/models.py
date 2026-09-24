from pydantic import BaseModel


class ModelUploadResponse(BaseModel):
    model_id: str
    filename: str
    status: str


class ModelListResponse(BaseModel):
    models: list[str]


class ModelActivateResponse(BaseModel):
    model_id: str
    status: str
