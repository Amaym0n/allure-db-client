import os

import pytest

from allure_pg_client import DBClient


@pytest.fixture(scope="session")
def get_db_client() -> DBClient:
    """ Get database client using environment variable PG_CONNECTION_STRING """
    connection_string = os.getenv('PG_CONNECTION_STRING')
    with DBClient(connection_string=connection_string) as db_client:
        print('DB connection successful opened')
        yield db_client
    print('DB connection was closed')
