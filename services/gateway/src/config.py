from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    data_controller_url: str
    train_controller_url: str
    inference_url: str
    model_registry_url: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()