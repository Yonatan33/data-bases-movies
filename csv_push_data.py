import pandas as pd
import utils
csv_tables = ['movie_ratings',
              'series_ratings']
csv_columns = [['movie id', 'average vote', 'vote count'],
               ['series id', 'average vote', 'vote count']]


def insert_csv_to_db(data_frame:pd.DataFrame, index):
    data_array = data_frame.to_numpy()
    params = csv_columns[index]
    for row in data_array:
        query = utils.generate_insert_query(params, row, csv_tables[index])
        utils.insert(query)


