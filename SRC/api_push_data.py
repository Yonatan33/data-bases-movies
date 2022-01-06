import utils
import constants as const


def push_movie_to_tables(details: dict):
    push_movie_details(details)
    push_movie_profits(details)
    push_movie_genres(details)


def push_movie_details(details: dict):
    query_values = []
    params = const.api_movie_columns[0]
    table_name = const.api_movies_tables[0]
    for value in params:
        if value == 'title':
            query_values.append(f'"{details[value]}"')
            continue
        if value == "release_date":
            date = details[value]
            query_values.append(date[:4])
            continue
        query_values.append(details[value])
    query = utils.generate_insert_query_with_array(params=params,
                                                   values=query_values,
                                                   table_name=table_name)
    utils.insert(query, query_values)
    utils.commit_query()


def push_movie_genres(details: dict):
    params = const.api_movie_columns[2]
    table_name = const.api_movies_tables[2]
    movie_id = details['movie_id']
    genre_list = details['genres']
    for genre in genre_list:
        query_values = [movie_id, genre]
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=query_values,
                                                       table_name=table_name)
        utils.insert(query, query_values)
        utils.commit_query()


def push_movie_profits(details: dict):
    query_values = []
    table_name = const.api_movies_tables[1]
    params = const.api_movie_columns[1]
    for param in params:
        query_values.append(details[param])
    query = utils.generate_insert_query_with_array(params=params,
                                                   values=query_values,
                                                   table_name=table_name)
    utils.insert(query, query_values)
    utils.commit_query()


def push_series_to_tables(details: dict):
    push_series_details(details)
    push_series_genres(details)


def push_series_details(details: dict):
    params = const.api_series_columns[0]
    table_name = const.api_series_tables[0]
    query_values = []
    for param in params:
        if param == 'name':
            query_values.append(f'"{details[param]}"')
            continue
        if param == 'first_air_date':
            year = str(details[param].split('-')[0])
            query_values.append(year)
            continue
        query_values.append(details[param])
    query = utils.generate_insert_query_with_array(params=params,
                                                   values=query_values,
                                                   table_name=table_name)
    utils.insert(query, query_values)
    utils.commit_query()


def push_series_genres(details: dict):
    params = const.api_series_columns[1]
    table_name = const.api_series_tables[1]
    series_id = details['series_id']
    genre_list = details['genres']
    for genre in genre_list:
        query_values = [series_id, genre]
        query = utils.generate_insert_query_with_array(params=params,
                                                       values=query_values,
                                                       table_name=table_name)
        utils.insert(query, query_values)
        utils.commit_query()


