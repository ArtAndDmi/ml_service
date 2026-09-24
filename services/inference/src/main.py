from fastapi import FastAPI

from src.api import predict_router, model_router, health_router

app = FastAPI(
    title='ML Service Inference',
    version='0.1.0'
)

app.include_router(predict_router)
app.include_router(model_router)
app.include_router(health_router)
