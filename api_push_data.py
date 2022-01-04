import utils
import constants as const


def push_movie(details:dict):
    for i in range(len(const.api_movies_tables)):
        query_values = []
        for value in const.api_movie_columns[i]:
            if value == 'title':
                query_values.append(f'"{details[value]}"')
                continue
            if value == 'genres':
                lst = [str(i) for i in details[value]]
                genres_string = ', '.join(lst)
                genres_string = genres_string[:-2]
                query_values.append(f'({genres_string})')
                continue
            if value == "release_date":
                date = details[value]
                query_values.append(date[:4])
                continue
            query_values.append(details[value])
        query = utils.generate_insert_query_with_array(params=const.api_movie_columns[i],
                                                       values=query_values,
                                                       table_name=const.api_movies_tables[i])
        utils.insert(query)


def push_series(details:dict):
    for i in range(len(const.api_series_tables)):
        query_values = []
        for value in const.api_series_columns[i]:
            query_values.append(details[value])
        query = utils.generate_insert_query_with_array(params=const.api_series_columns[i],
                                                       values=query_values,
                                                       table_name=const.api_series_tables[i])
        utils.insert(query)


