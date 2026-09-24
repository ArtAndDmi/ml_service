from src.storage.filesystem import save_model, model_exists, get_models
from src.clients.inference import activate_model as activate_inference_model


def register_model(content: bytes) -> str:
    models = get_models()

    is_first_model = len(models) == 0

    model_id, _ = save_model(content=content)

    if is_first_model:
        activate_model(model_id=model_id)

    return model_id


def list_models() -> list[str]:
    return get_models()


def activate_model(model_id: str) -> None:
    if not model_exists(model_id):
        raise FileNotFoundError(
            f'Model {model_id} not found'
        )

    activate_inference_model(
        model_id=model_id
    )
