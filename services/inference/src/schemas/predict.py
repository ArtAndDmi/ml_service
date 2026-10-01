from pydantic import BaseModel


class PredictRequest(BaseModel):
    carat: float
    depth: float | None = None
    table: float | None = None
    x: float | None = None
    y: float | None = None
    z: float | None = None
    cut: str
    color: str
    clarity: str


class PredictResponse(BaseModel):
    prediction: float
    model_version: str