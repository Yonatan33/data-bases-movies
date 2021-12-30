import pandas as pd
from csv_push_data import insert_csv_to_db

movies_ratings_path = 'C:\\Users\\USER\\OneDrive\\studies recovery\\Year 4\\סמסטר א\\מערכות בסיסי נתונים' \
                      '\\HW3\\IMDb ratings.csv'
series_ratings_path = "C:\\Users\\USER\\OneDrive\\Studies temp\\מערכות בסיסי נתונים\\HW3\\raw data" \
                      "\\imdb-tv-ratings-master\\all-series-ep-average.csv"

movie_ratings_columns = ['imdb_title_id', 'weighted_average_vote', 'total_votes']
series_rating_columns = ['Code', 'Rating', 'Rating Count']

paths = [movies_ratings_path,
         series_ratings_path]
columns_of_interest = [movie_ratings_columns,
                       series_rating_columns]


def pull_csv_data():
    for i, path in enumerate(paths):
        data_frame = pd.read_csv(path, names=columns_of_interest[i], keep_default_na=False)
        data_frame = data_frame[1:]
        insert_csv_to_db(data_frame, i)


pull_csv_data()

