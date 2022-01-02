# *************** api constants ***************
api_key = '3200bf656c8e9d31856545ea40e02266'
api_movies_tables = ['movie_details',
                     'movie_budget']
api_movie_columns = [['id',
                      'title',
                      'release_date',
                      'genre',
                      'language'],
                     ['id',
                      'revenue',
                      'budget']]
api_series_tables = ['series_details']

api_series_columns = [['id',
                      'name',
                      'first_air_date',
                      'genre',
                      'language',
                      ]]

# *************** csv constants ***************
movies_ratings_path = 'C:\\Users\\USER\\OneDrive\\studies recovery\\Year 4\\סמסטר א\\מערכות בסיסי נתונים' \
                      '\\HW3\\IMDb ratings.csv'
series_ratings_path = "C:\\Users\\USER\\OneDrive\\Studies temp\\מערכות בסיסי נתונים\\HW3\\raw data" \
                      "\\imdb-tv-ratings-master\\all-series-ep-average.csv"
csv_movie_ratings_columns = ['imdb_title_id', 'weighted_average_vote', 'total_votes']
csv_series_rating_columns = ['Code', 'Rating', 'Rating Count']
csv_tables = ['movie_ratings',
              'series_ratings']
csv_columns = [['movie id', 'average vote', 'vote count'],
               ['series id', 'average vote', 'vote count']]

# *************** init constants ***************
init_tables = ['movies',
          'movie_ratings',
          'movie_profits',
          'movie_cast']
init_column_types = [[('movie_id', 'INT'), ('title', 'varchar(500)'), ('release year', 'INT'), ('genres', 'varchar (500)')],
                [('movie_id', 'INT'), ('ratings', 'FLOAT'), ('vote count', 'INT')],
                [('movie_id', 'INT'), ('budget', 'INT'), ('revenue', 'INT')],
                [('movie_id', 'INT')]]

