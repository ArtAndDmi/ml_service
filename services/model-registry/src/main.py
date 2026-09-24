from fastapi import FastAPI

from src.api import health_router, models_router

app = FastAPI(
    title='ML Service Model-Registry',
    version='0.1.0'
)

app.include_router(health_router)
app.include_router(models_router)
