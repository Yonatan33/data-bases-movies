import pandas as pd
from csv_push_data import insert_csv_to_db
import constants as const

paths = [const.movies_ratings_path,
         const.series_ratings_path]
columns_of_interest = [const.csv_movie_ratings_columns,
                       const.csv_series_rating_columns]


def pull_csv_data():
    for i, path in enumerate(paths):
        data_frame = pd.read_csv(path, names=columns_of_interest[i], keep_default_na=False)
        data_frame = data_frame[1:]
        insert_csv_to_db(data_frame, i)



