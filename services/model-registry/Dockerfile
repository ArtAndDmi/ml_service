FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY services/model-registry/pyproject.toml ./pyproject.toml
COPY services/model-registry/uv.lock ./uv.lock

RUN uv sync --frozen

COPY services/model-registry/src ./src

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8005"]