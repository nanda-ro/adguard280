FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "adguard280.main:app", "--reload", "--host", "0.0.0.0" ]
