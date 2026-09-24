FROM python:3.12-slim

RUN pip install uv

WORKDIR /app/services/train

COPY services/train/pyproject.toml ./pyproject.toml
COPY services/train/uv.lock ./uv.lock

COPY libs/ml_common /app/libs/ml_common

RUN uv sync --frozen

COPY services/train/src ./src

CMD ["uv", "run", "python", "-m", "src.main"]