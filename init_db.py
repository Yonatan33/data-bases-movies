from sql_connector import SQLConnector
import constants as const

connector = SQLConnector()


def check_if_table_exists(table):
    query = f"select table_name from INFORMATION_SCHEMA.TABLES as info where info.table_name = '{table}'"
    connector.execute_query(query)
    answer = connector.connector_current_rows()
    return answer


def create_query(table_name):
    query = 'CREATE TABLE '
    i = const.init_tables.index(table_name)
    query += table_name + ' ('
    for column in const.init_column_types[i]:
        query += f'{column[0]} {column[1]}, '
    if table_name == 'movie_genres' or \
            table_name == 'series_genres' or \
            table_name == 'movie_cast':
        query += f'PRIMARY KEY({const.init_column_types[i][0][0]}, {const.init_column_types[i][1][0]}));'
    else:
        query += f'PRIMARY KEY({const.init_column_types[i][0][0]}));'
    return query


def create_tables():
    for table in const.init_tables:
        if not check_if_table_exists(table):
            query = create_query(table)
            #query = 'drop table if exists ' + table
            connector.execute_query(query)
    # for table, column in const.init_indices:
    index_query = f'CREATE INDEX movie_id_index ON movie_details (movie_id);'
    connector.execute_query(index_query)


# TODO - INDEX

# create_tables()

