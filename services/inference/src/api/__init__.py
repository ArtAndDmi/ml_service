from src.api.model import router as model_router
from src.api.predict import router as predict_router
from src.api.health import router as health_router

__all__ = [
    'model_router',
    'predict_router',
    'health_router'
]
