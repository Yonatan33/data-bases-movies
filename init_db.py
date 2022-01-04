from sql_connector import SQLConnector
import constants as const

connector = SQLConnector()


def create_query(table_name):
    query = 'CREATE TABLE '
    i = const.init_tables.index(table_name)
    query += table_name + ' ('
    for column in const.init_column_types[i]:
        query += f'{column[0]} {column[1]}, '
    query += f'PRIMARY KEY({const.init_column_types[i][0][0]}));'
    return query


def create_tables():
    for table in const.init_tables:
        query = create_query(table)
        #query = 'drop table if exists ' + table
        connector.execute_query(query)

# TODO - INDEX

create_tables()