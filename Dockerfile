FROM python:3.14

WORKDIR /app

RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini ./

RUN chown -R appuser:appuser /app

USER appuser

CMD ["uv", "run", "fastapi", "run", "src/main.py"]
