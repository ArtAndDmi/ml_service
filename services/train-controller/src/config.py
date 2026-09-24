from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    train_url: str
    train_image: str = 'ml-service-train:latest'
    train_network: str = 'ml-network'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()