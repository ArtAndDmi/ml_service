import docker

from src.config import settings

docker_client = docker.from_env()


def run_train_container(job_id: str) -> None:
    docker_client.containers.run(
        image=settings.train_image,
        environment={
            'JOB_ID': job_id,
            'DB_HOST': 'postgres',
            'DB_PORT': '5432',
            'DB_NAME': 'ml_service',
            'DB_USER': 'train_user',
            'DB_PASSWORD': 'train',
            'MODEL_REGISTRY_URL': 'http://model-registry:8005',
            'TRAIN_CONTROLLER_URL': 'http://train-controller:8003',
        },
        network=settings.train_network,
        detach=True,
        remove=True
    )
