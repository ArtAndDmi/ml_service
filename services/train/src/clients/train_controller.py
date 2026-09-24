import httpx

from src.config import settings


def update_train_status(
        status: str,
        model_version: str | None = None,
) -> None:
    response = httpx.patch(
        f'{settings.train_controller_url}/train/{settings.job_id}',
        json={
            'status': status,
            'model_version': model_version,
        },
    )

    response.raise_for_status()


def notify_completed(
        model_version: str,
) -> None:
    update_train_status(
        status='completed',
        model_version=model_version,
    )


def notify_rejected() -> None:
    update_train_status(
        status='rejected',
    )


def notify_failed() -> None:
    update_train_status(
        status='failed',
    )
