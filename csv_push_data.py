import pandas as pd
import utils
import constants as const


def push_csv_movie_ratings(data_frame:pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[0]
    table_name = const.csv_tables[0]
    for row in data_array:
        row = row.tolist()
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=row,
                                                       table_name=table_name)
        utils.insert(query, row)
        utils.commit_query()


def push_csv_series_ratings(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[1]
    table_name = const.csv_tables[1]
    for row in data_array:
        row = row.tolist()
        row[1], row[2] = row[2], row[1]
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=row,
                                                       table_name=table_name)
        utils.insert(query, row)
        utils.commit_query()


def push_csv_actors(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[2]
    table_name = const.csv_tables[2]
    for row in data_array:
        row = row.tolist()
        if row[len(row)-1]:
            continue
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=row[:-1],
                                                       table_name=table_name)
        utils.insert(query, row[:-1])
        utils.commit_query()


def push_csv_movie_cast(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[3]
    table_name = const.csv_tables[3]
    for i, row in enumerate(data_array):
        row = row.tolist()
        if row[2] != 'actress' and row[2] != 'actor':
            continue
        if i % 5 == 0:
            row[3] = row[3][1:-1]
            row[3] = row[3].split(',')
            row[3] = str(len(row[3]))
            row.pop(2)
            query = utils.generate_insert_query_with_array(params=params,
                                                           values=row,
                                                           table_name=table_name)
            utils.insert(query, row)
            utils.commit_query()


def push_csv_movie_details(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[4]
    table_name = const.csv_tables[4]
    for row in data_array:
        row = row.tolist()
        year = str(row[2].split('-')[0])
        row[2] = year
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=row,
                                                       table_name=table_name)
        utils.insert(query, row)
        utils.commit_query()


def push_csv_movie_genres(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[5]
    table_name = const.csv_tables[5]
    for row in data_array:
        row = row.tolist()
        movie_id = row[0]
        genre_list = row[1].split(',')
        for genre in genre_list:
            query = utils.generate_insert_query_with_array(params=params,
                                                           values=[movie_id, genre],
                                                           table_name=table_name)
            utils.insert(query, [movie_id, genre])
            utils.commit_query()


def push_csv_series_details(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[6]
    table_name = const.csv_tables[6]
    for row in data_array:
        row = row.tolist()
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=row,
                                                       table_name=table_name)
        utils.insert(query, row)
        utils.commit_query()


def push_csv_series_genres(data_frame: pd.DataFrame):
    data_array = data_frame.to_numpy()
    params = const.csv_columns[7]
    table_name = const.csv_tables[7]
    for row in data_array:
        row = row.tolist()
        series_id = row[0]
        genre_list = row[1].split(',')
        for genre in genre_list:
            query = utils.generate_insert_query_with_array(params=params,
                                                           values=[series_id, genre],
                                                           table_name=table_name)
            utils.insert(query, [series_id, genre])
            utils.commit_query()

