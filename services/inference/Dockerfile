FROM python:3.12-slim

RUN pip install uv

WORKDIR /app/services/inference

COPY services/inference/pyproject.toml ./pyproject.toml
COPY services/inference/uv.lock ./uv.lock

COPY libs/ml_common /app/libs/ml_common

RUN uv sync --frozen

COPY services/inference/src ./src

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]