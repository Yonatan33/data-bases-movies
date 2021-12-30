from sql_connector import SQLConnector

tables = ['movies',
          'movie_ratings',
          'movie_profits',
          'movie_cast']
column_types = [[('movie_id', 'INT'), ('title', 'varchar(500)'), ('release year', 'INT'), ('genres', 'varchar (500)')],
                [('movie_id', 'INT'), ('ratings', 'FLOAT'), ('vote count', 'INT')],
                [('movie_id', 'INT'), ('budget', 'INT'), ('revenue', 'INT')],
                [('movie_id', 'INT')]]


def create_query(table_name):
    query = 'CREATE TABLE '
    i = tables.index(table_name)
    query += table_name + ' ('
    for column in column_types[i]:
        query = f'{column[0]} {column[1]}, '
    query += f'PRIMARY KEY({column_types[i][0]}));'
    return query


def create_table():
    for table in tables:
        query = create_query(table)
        SQLConnector.execute_query(query)

# TODO - INDEX
