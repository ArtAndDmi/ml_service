from pydantic import BaseModel


class PredictRequest(BaseModel):
    carat: float
    depth: float
    table: float
    x: float
    y: float
    z: float
    cut: str
    color: str
    clarity: str

class PredictResponse(BaseModel):
    prediction: float
    model_version: str
