# *************** api constants ***************
api_key = '3200bf656c8e9d31856545ea40e02266'
api_movies_tables = ['movie_details',
                     'movie_profits']
api_movie_columns = [['movie_id',
                      'title',
                      'release_date',
                      'genres',
                      'language'],
                     ['movie_id',
                      'revenue',
                      'budget']]
api_series_tables = ['series_details']

api_series_columns = [['series_id',
                      'name',
                      'first_air_date',
                      'genres',
                      'language']]

# *************** csv constants ***************
movies_ratings_path = 'C:\\Users\\USER\\OneDrive\\studies recovery\\Year 4\\סמסטר א\\מערכות בסיסי נתונים' \
                      '\\HW3\\IMDb ratings.csv'
series_ratings_path = "C:\\Users\\USER\\OneDrive\\Studies temp\\מערכות בסיסי נתונים\\HW3\\raw data" \
                      "\\imdb-tv-ratings-master\\all-series-ep-average.csv"
csv_movie_ratings_columns = ['imdb_title_id', 'weighted_average_vote', 'total_votes']
csv_series_rating_columns = ['Code', 'Rating', 'Rating Count']
csv_tables = ['movie_ratings',
              'series_ratings']
csv_columns = [['movie id', 'average_vote', 'vote_count'],
               ['series id', 'average_vote', 'vote_count']]

# *************** init constants ***************
init_tables = ['movie_details',
               'movie_ratings',
               'series_details',
               'movie_profits',
               'series_ratings'
               ]
init_column_types = [[('movie_id', 'INT'), ('title', 'varchar(500)'), ('release_date', 'INT'), ('genres', 'varchar(500)'), ('language', 'varchar(500)')],
                     [('movie_id', 'INT'), ('average_vote', 'FLOAT'), ('vote_count', 'INT')],
                     [('series_id', 'INT'), ('name', 'varchar(500)'), ('first_air_date', 'INT'), ('genres', 'varchar(500)'), ('language', 'varchar(500)')],
                     [('movie_id', 'INT'), ('budget', 'INT'), ('revenue', 'INT')],
                     [('series_id', 'INT'), ('average_vote', 'FLOAT'), ('vote_count', 'INT')]]

