from src.clients.model_registry import register_model
from src.clients.train_controller import (
    notify_completed,
    notify_failed,
    notify_rejected,
)
from src.service.artifact import save_model
from src.service.data_loader import load_training_data
from src.service.train import train_model
from src.service.validator import validate_model


def main() -> None:
    artifact_path = None

    try:
        data = load_training_data()

        train_result = train_model(data)

        validation_result = validate_model(
            model=train_result.model,
            x_valid=train_result.x_valid,
            y_valid=train_result.y_valid,
        )
        print(validation_result.metrics)

        if not validation_result.is_valid:
            notify_rejected()
            return

        artifact_path = save_model(
            model=train_result.model,
        )

        model_id = register_model(
            artifact_path=artifact_path,
        )

        notify_completed(
            model_version=model_id,
        )


    except Exception:
        notify_failed()
        raise

    finally:
        if artifact_path is not None:
            artifact_path.unlink(
                missing_ok=True,
            )


if __name__ == '__main__':
    main()