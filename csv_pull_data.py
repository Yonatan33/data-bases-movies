import pandas as pd
from csv_push_data import *
import constants as const


def pull():
    pull_csv_movie_ratings()
    pull_csv_series_ratings()
    pull_csv_actors()
    pull_csv_movie_cast()
    pull_csv_movie_details()
    pull_csv_movie_genres()
    pull_csv_series_details()
    pull_csv_series_genres()



def pull_csv_movie_ratings():
    path = const.movies_ratings_path
    columns = const.csv_movie_ratings_columns
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_movie_ratings(data_frame)


def pull_csv_series_ratings():
    path = const.series_ratings_path
    columns = const.csv_series_rating_columns
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_series_ratings(data_frame)


def pull_csv_actors():
    path = const.actors_path
    columns = const.csv_actors_columns
    columns.append('date_of_death')
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_actors(data_frame)


def pull_csv_movie_cast():
    path = const.movie_cast_path
    columns = const.csv_movie_cast_columns
    columns.append('category')
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_movie_cast(data_frame)


def pull_csv_movie_details():
    path = const.movies_path
    columns = const.csv_movie_details_columns
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_movie_details(data_frame)


def pull_csv_movie_genres():
    path = const.movies_path
    columns = const.csv_movie_genres_columns
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_movie_genres(data_frame)


def pull_csv_series_details():
    path = const.series_details_path
    columns = const.csv_series_details_columns
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_series_details(data_frame)


def pull_csv_series_genres():
    path = const.series_genres_path
    columns = const.csv_series_genres_columns
    data_frame = pd.read_csv(path, usecols=columns, dtype='str', keep_default_na=False)
    push_csv_series_genres(data_frame)



