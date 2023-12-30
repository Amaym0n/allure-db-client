FROM python:3.11-slim

ENV PG_CONNECTION_STRING="postgresql://postgres:postgres@localhost:5432/test_db"
COPY . /project
WORKDIR /project
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

CMD ["poetry", "run", "pytest", "-s", "-vv"]