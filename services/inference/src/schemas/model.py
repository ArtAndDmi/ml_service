from pydantic import BaseModel


class ModelReloadResponse(BaseModel):
    model_id: str
    status: str
