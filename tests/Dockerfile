FROM python:3.11-slim

COPY . /tests
WORKDIR /tests
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

CMD ["poetry", "run", "pytest", "-s", "-vv", "--alluredir=allure_results"]