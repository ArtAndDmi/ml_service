from fastapi import FastAPI

from src.api import health_router, train_router

app = FastAPI(
    title='ML Service Train Controller',
    version='0.1.0',
)

app.include_router(health_router)
app.include_router(train_router)
