from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.config import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def check_connection() -> bool:
    with engine.connect() as connection:
        connection.execute(text('SELECT 1'))
    return True


def get_session():
    with SessionLocal() as session:
        yield session
