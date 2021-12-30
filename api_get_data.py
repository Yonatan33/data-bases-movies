from tmdbv3api import *
import sql_connector

tmdb = TMDb()
tmdb.api_key = '3200bf656c8e9d31856545ea40e02266'
tmdb.language = 'en'

discover = Discover()
movies_ids = discover.discover_movies({})
movies = Movie()
genre = Genre()
genres_dict = genre.movie_list()




def import_api_to_db(movie_id):
    movie = movies.details(movie_id)
    genre_list = ''
    for genre in movie.genres:
        genre_list += f'{str(genre[id])} '
    genre_list = genre_list[:-1]
    movie_details = {
        "id": movie["id"],
        "title": movie["title"],
        "year":movie["year"],
        "popularity":movie["popularity"],
        "revenue":movie["revenue"],
        "genre":movie["genre_ids"],
        "language": movie["original_language"],
        "vote_avg": movie["vote_average"],
        "votes": movie["vote_count"]
    }

i=0
for movie_id in movies_ids:
    if i==5:
        break
    i += 1
    import_api_to_db(movie_id.id)


# for p in trend:
#     print(p.known_for_department)
# print(m_details.genres)
# for i in trend:
#     print(f'{i.keys()}')


