from fastapi import FastAPI

from src.api import health_router, data_router

app = FastAPI(
    title='ML Service Data-Controller',
    version='0.1.0',
)

app.include_router(health_router)
app.include_router(data_router)
