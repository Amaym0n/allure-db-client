from allure_db_client import DBClient


def test_check_hidden_execute_command(get_db_client: DBClient):
    table = 'pg_catalog.pg_tables'
    get_db_client.get_first_row(query=f'SELECT * FROM {table}')

