FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY services/train-controller/pyproject.toml ./pyproject.toml
COPY services/train-controller/uv.lock ./uv.lock

RUN uv sync --frozen

COPY services/train-controller/src ./src

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8003"]