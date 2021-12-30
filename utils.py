from sql_connector import SQLConnector


def generate_insert_query(params: list, values: list, table_name):
    table_columns = ''
    for param in params:
        table_columns += (param + ', ')
    table_columns = table_columns[:-2]
    table_values = ''
    for value in values:
        table_values += (value + ', ')
    table_values = table_values[:-2]
    query = f'INSERT INTO {table_name} ({table_columns}) VALUES ({table_values})'
    return query


def insert(query):
    try:
        SQLConnector.execute_query(query)
    except Exception as ex:
        print(f"{type(ex).__name__} at line {ex.__traceback__.tb_lineno} of {__file__}: {ex}")