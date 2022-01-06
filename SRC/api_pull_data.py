from tmdbv3api import *
from api_push_data import *
import constants as const
tmdb = TMDb()
tmdb.api_key = const.api_key
tmdb.language = 'en'

discover = Discover()
movies_ids = discover.discover_movies({})
movies = Movie()
series = TV()
series_obj = discover.discover_tv_shows({})
genre = Genre()
genres_dict = genre.tv_list()


def import_api_movies_to_db(movie_id):
    movie = movies.details(movie_id)
    genre_list = []
    for genre in movie.genres:
        genre_list.append((genre["name"]))
    movie_details = {
        "movie_id": movie["imdb_id"],
        "title": movie["title"],
        "release_date":movie["release_date"],
        "revenue":movie["revenue"],
        "budget":movie["budget"],
        "genres":genre_list,
        "language": movie["original_language"]
    }
    return movie_details


def import_api_series_to_db(series_obj):
    genre_list = []
    for genre in series_obj['genre_ids']:
        for genre_element in genres_dict:
            if genre_element['id'] == genre:
                genre_list.append(genre_element["name"])
    series_details = {
        "series_id": series_obj["id"],
        "name": series_obj["name"],
        "first_air_date": series_obj["first_air_date"],
        "genres": genre_list,
        "language": series_obj["original_language"]
    }
    return series_details


# iterate over the dict and call the relevant push methods
def pull():
    for movie_id in movies_ids:
        movie_details = import_api_movies_to_db(movie_id.id)
        push_movie_to_tables(movie_details)
    for series_id in series_obj:
        series_details = import_api_series_to_db(series_id)
        push_series_to_tables(series_details)