import logging
from fastapi import FastAPI

from src.api import (
    health_router,
    load_data_router,
    models_router,
    predict_router,
    train_router,
)

app = FastAPI(
    title='ML Service Gateway',
    version='0.1.0',
)

app.include_router(health_router)
app.include_router(load_data_router)
app.include_router(predict_router)
app.include_router(models_router)
app.include_router(train_router)
