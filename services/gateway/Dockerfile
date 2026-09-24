FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY services/gateway/pyproject.toml ./pyproject.toml
COPY services/gateway/uv.lock ./uv.lock

RUN uv sync --frozen

COPY services/gateway/src ./src

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]