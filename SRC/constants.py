# *************** api constants ***************
api_key = '3200bf656c8e9d31856545ea40e02266'
api_movies_tables = ['movie_details',
                     'movie_profits',
                     'movie_genres',
                     'movie_rating']
api_movie_columns = [['movie_id', 'title', 'release_date', 'language'],
                     ['movie_id', 'revenue', 'budget'],
                     ['movie_id', 'genre_name'],
                     ['movie_id', 'rating', 'vote_count']]
api_series_tables = ['series_details',
                     'series_genres',
                     'series_rating']

api_series_columns = [['series_id', 'name', 'first_air_date'],
                      ['series_id', 'genre_name'],
                      ['series_id', 'rating', 'vote_count']]

# *************** csv constants ***************
movies_ratings_path = 'IMDb ratings.csv'
series_ratings_path = 'IMDB TV Series.csv'
actors_path = 'IMDb names.csv'
movie_cast_path = 'IMDb title_principals.csv'
movies_path = 'IMDb movies.csv'
series_details_path = 'IMDB TV Series.csv'
series_genres_path = 'IMDB TV Series.csv'

csv_movie_ratings_columns = ['imdb_title_id', 'weighted_average_vote', 'total_votes']
csv_movie_genres_columns = ['imdb_title_id', 'genre']
csv_actors_columns = ['imdb_name_id', 'name']
csv_movie_cast_columns = ['imdb_title_id', 'imdb_name_id', 'characters']
csv_movie_details_columns = ['imdb_title_id', 'title', 'date_published', 'language']
csv_series_details_columns = ['tconst', 'primaryTitle', 'startYear']
csv_series_genres_columns = ['tconst', 'genres']
csv_series_rating_columns = ['tconst', 'numVotes', 'averageRating']

csv_tables = ['movie_ratings',
              'series_ratings',
              'actors',
              'movie_cast',
              'movie_details',
              'movie_genres',
              'series_details',
              'series_genres']
csv_columns = [['movie_id', 'average_vote', 'vote_count'],
               ['series_id', 'average_vote', 'vote_count'],
               ['actor_id', 'actor_name'],
               ['movie_id', 'actor_id', 'number_of_roles'],  # Primary key is (movie_id, actor_id)
               ['movie_id', 'title', 'release_date', 'language'],
               ['movie_id', 'genre_name'],
               ['series_id', 'name', 'first_air_date'],
               ['series_id', 'genre_name'],
               ]

# *************** init constants ***************
init_tables = ['movie_details',
               'movie_ratings',
               'movie_genres',
               'movie_profits',
               'movie_cast',
               'actors',
               'series_ratings',
               'series_details',
               'series_genres'
               ]
init_column_types = [[('movie_id', 'varchar(20)'), ('title', 'varchar(500) NOT NULL'), ('release_date', 'INT NOT NULL'), ('language', 'varchar(500)')],   # movie_details
                     [('movie_id', 'varchar(20)'), ('average_vote', 'FLOAT NOT NULL'), ('vote_count', 'INT')],   # movie_rating
                     [('movie_id', 'varchar(20)'), ('genre_name', 'varchar(500)')],     # movie_genres
                     [('movie_id', 'varchar(20)'), ('budget', 'INT NOT NULL'), ('revenue', 'INT NOT NULL')],  # movie_profits
                     [('movie_id', 'varchar(20)'), ('actor_id', 'varchar(20) NOT NULL'), ('number_of_roles', 'INT NOT NULL')],    # movie_cast
                     [('actor_id', 'varchar(20)'), ('actor_name', 'varchar(500)')],     # actors
                     [('series_id', 'varchar(20)'), ('average_vote', 'FLOAT'), ('vote_count', 'INT')],  # series_ratings
                     [('series_id', 'varchar(20)'), ('name', 'varchar(500)'), ('first_air_date', 'INT NOT NULL'), ('language', 'varchar(500)')],     # series_details
                     [('series_id', 'varchar(20)'), ('genre_name', 'varchar(500)')]]    # series_genres

init_indices = [('movie_details', 'movie_id'),
                ('movie_genres', 'genre_name'),
                ('actors', 'actor_name'),
                ('series_details', 'series_id'),
                ('series_genres', 'genre_name'),
                ]
