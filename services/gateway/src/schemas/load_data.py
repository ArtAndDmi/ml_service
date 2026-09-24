from pydantic import BaseModel

class LoadDataResponse(BaseModel):
    filename: str
    rows_received: int
    status: str

