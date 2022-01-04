from sql_connector import SQLConnector

connector = SQLConnector()


def generate_insert_query_with_array(params: list, values: list, table_name):
    table_columns = ''
    for param in params:
        table_columns += (param + ', ')
    table_columns = table_columns[:-2]
    table_values = ''
    for value in values:
        table_values += (str(value) + ', ')
    table_values = table_values[:-2]
    query = f'INSERT INTO {table_name} ({table_columns}) VALUES ({table_values});'
    #query = f'INSERT INTO {table_name} VALUES ({table_values});'
    return query


def generate_insert_query_with_dict(details:dict, table_name):
    query_list = []
    for key in details.keys():
        query_list.append(f'INSERT INTO {table_name} ({key}) VALUES ({details[key]})')
    return query_list


def insert(query):
    try:
        connector.execute_query(query)
    except Exception as ex:
        print(f"{type(ex).__name__} at line {ex.__traceback__.tb_lineno} of {__file__}: {ex}")



