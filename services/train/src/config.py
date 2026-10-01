from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    model_registry_url: str
    train_controller_url: str

    job_id: str

    model_min_r2: float = 0.7

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    @property
    def database_url(self) -> str:
        return (
            f'postgresql+psycopg://'
            f'{self.db_user}:{self.db_password}'
            f'@{self.db_host}:{self.db_port}/{self.db_name}'
        )


settings = Settings()