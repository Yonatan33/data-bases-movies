from sql_connector import SQLConnector

connector = SQLConnector()


def send_execute(query):
    try:
        connector.execute_query_no_params(query)
        answer = connector.fetch()
    except Exception as ex:
        print(f"{type(ex).__name__} at line {ex.__traceback__.tb_lineno} of {__file__}: {ex}")
        return None
    return answer


# *********** Query1 - top movies by rating ***********
def query_1(user_from, user_to):
    query = f'''select mr.movie_id, md.title, md.release_date
                from movie_details as md, movie_ratings as mr
                where md.movie_id = mr.movie_id and mr.vote_count>1000 and md.release_date >= {user_from} and md.release_date <= {user_to}
                order by mr.average_vote
                limit 100
                '''
    answer = send_execute(query)
    for movie_id, title, year in answer:
        print(f'movie_id: {movie_id} | title: {title} | release_date: {year}')


# *********** Query3 - top movie genre by rating ***********
def query_3():
    query = '''select distinct mg.genre_name, count(*)
                from movie_genres as mg, (select md.movie_id from movie_details as md, movie_ratings as mr
                                           where md.movie_id = mr.movie_id and mr.vote_count>1000
                                           order by mr.average_vote) as top_movie_ratings
                where mg.movie_id = top_movie_ratings.movie_id 
                group by mg.genre_name
                order by count(mg.genre_name) desc
                limit 10
                '''
    answer = send_execute(query)
    for genre_name, num_of_movies in answer:
        print(f'genre_name: {genre_name} | No. of top rated movies: {num_of_movies}')


# *********** Query4 - top movie genre by profits ***********
def query_4():
    query = '''select distinct mg.genre_name, count(*)
                from movie_genres as mg, (select md.movie_id from movie_details as md, movie_profits as mp
                                           where md.movie_id = mp.movie_id 
                                           order by (mp.revenue-mp.budget)) as top_movie_profit
                where mg.movie_id = top_movie_profit.movie_id 
                group by mg.genre_name
                order by count(mg.genre_name) desc
                limit 5
                '''
    answer = send_execute(query)
    for genre_name, num_of_movies in answer:
        print(f'genre_name: {genre_name} | No. of lucrative movies: {num_of_movies}')


# *********** Query5 - top series by ratings ***********
def query_5():
    query = '''select sd.name
                from series_details as sd, series_ratings as sr
                where sd.series_id = sr.series_id and sr.vote_count>100000
                order by sr.average_vote desc
                limit 50
                '''
    answer = send_execute(query)
    for series_name in answer:
        print(f'name: "{series_name[0]}"')


# *********** Query6 - top series in genre by ratings ***********
def query_6(genre_name):
    query = f'''select top_rating_series.series_name
                from series_genres as sg, (select sd.series_id as id, sd.name as series_name from series_details as sd, series_ratings as sr
                                            where sd.series_id = sr.series_id and sr.vote_count>200000
                                            order by sr.average_vote desc) as top_rating_series
                where sg.series_id = top_rating_series.id and sg.genre_name = "{genre_name}"
                limit 50
            '''
    answer = send_execute(query)
    for series_name in answer:
        print(f'name: "{series_name[0]}"')


# *********** Query7 - genres's actors of top movies by profits ***********
def query_7(user_genre_name):
    query = f'''select actor_name
                from actors as a, movie_cast as mc, movie_genres as mg, (select md.movie_id from movie_details as md, movie_profits as mp
                                           where md.movie_id = mp.movie_id 
                                           order by (mp.revenue-mp.budget)) as top_movie_profit
                where top_movie_profit.movie_id = mc.movie_id and mc.actor_id = a.actor_id 
                and top_movie_profit.movie_id = mg.movie_id and mg.genre_name = "{user_genre_name}"
                limit 50
                    '''
    answer = send_execute(query)
    for actor_name in answer:
        print(f'actor_name: "{actor_name[0]}"')


# *********** Query8 - movies of to selected actors ***********
def query_8(user_actor1_first, user_actor1_last, user_actor2_first, user_actor2_last):
    query = f'''select film_with_actor1.actor_name, film_with_actor1.title
                from
                    (select a.actor_name, md.title
                    from actors a, movie_details md, movie_cast as mc
                    where match(actor_name) against ("{user_actor1_first}") and  match(actor_name) against ("{user_actor1_last}")
                    and md.movie_id = mc.movie_id
                    and mc.actor_id = a.actor_id
                    ) as film_with_actor1
                union
                select film_with_actor2.actor_name, film_with_actor2.title
                from
                    (select a.actor_name, md.title
                    from actors a, movie_details as md, movie_cast as mc
                    where match(actor_name) against ("{user_actor2_first}") and  match(actor_name) against ("{user_actor2_last}")
                    and md.movie_id = mc.movie_id
                    and mc.actor_id = a.actor_id
                    ) as film_with_actor2
            '''
    answer = send_execute(query)
    for actor_name, title in answer:
        print(f'actor_name: {actor_name} | title: "{title}"')


# *********** Query9 - Average cost of making a movie in each genre ***********
def query_9():
    query = f'''select mg.genre_name, avg(mp.budget)
                from movie_details as md, movie_genres as mg, movie_profits as mp
                where md.movie_id = mg.movie_id and md.movie_id = mp.movie_id and mp.budget>0
                group by mg.genre_name 
                order by avg(mp.budget) asc
                '''
    answer = send_execute(query)
    for genre_name, avg_budget in answer:
        print(f'genre_name: {genre_name} | Average budget required: {avg_budget // 1000000}M$')


if __name__ == "__main__":
    print(f'**** Query 1 execution****')
    user_from, user_to = input("Enter year to start the search from"), input("Enter year to end the search at")
    query_1(user_from, user_to)
    print(f'**** Query 3 execution****')
    query_3()
    print(f'**** Query 4 execution****')
    query_4()
    print(f'**** Query 5 execution****')
    query_5()
    print(f'**** Query 6 execution****')
    genre_name = input("Enter genre name")
    query_6(genre_name)
    print(f'**** Query 7 execution****')
    genre_name = input("Enter genre name")
    query_7(genre_name)
    print(f'**** Query 8 execution****')
    actor1 = input("Enter first actor's name").split(" ")
    assert len(actor1) == 2, 'Name must be name and last name'
    actor2 = input("Enter second actor's name").split(" ")
    assert len(actor1) == 2, 'Name must be name and last name'
    query_8(actor1[0], actor1[1], actor2[0], actor2[1])
    print(f'**** Query 9 execution****')
    query_9()
