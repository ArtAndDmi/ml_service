from src.api.health import router as health_router
from src.api.load_data import router as load_data_router
from src.api.models import router as models_router
from src.api.predict import router as predict_router
from src.api.train import router as train_router

__all__ = [
    'health_router',
    'load_data_router',
    'models_router',
    'predict_router',
    'train_router'
]
