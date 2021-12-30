import locale
import pandas as pd
import requests
import json
api_key = '3200bf656c8e9d31856545ea40e02266'



def get_data(num_of_years):
    for i in num_of_years:
        response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key +
                                '&primary_release_year=' + str((2021 - i)) +'&sort_by=revenue.desc')
        highest_revenue = response.json()
    return True


response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key + '&sort_by=revenue.desc')
highest_revenue_ever = response.json()
highest_revenue_films_ever = highest_revenue_ever['results']

columns = ['film', 'revenue', 'budget', 'release_date', 'film_id','rating', 'Num of votes']
highest_revenue_ever_df = pd.DataFrame(columns=columns)
for film in highest_revenue_films_ever:
    # print(film['title'])

    film_revenue = requests.get('https://api.themoviedb.org/3/movie/'+ str(film['id']) +'?api_key='+ api_key+'&language=en-US')
    film_revenue = film_revenue.json()
    # print(film_revenue)

    # print(locale.currency(film_revenue['revenue'], grouping=True ))

    # Lord of the Rings duplicate w/ bad data was being returned  https://www.themoviedb.org/movie/454499-the-lord-of-the-rings
    # It's budget was $281 which is way too low for a top-earning film. Therefore in order to be added to dataframe the film
    # budget must be greater than $281.

    if film_revenue['budget'] > 281:
        # print(film_revenue['budget'])
        # add film title, revenue, budget and release date to the dataframe
        highest_revenue_ever_df.loc[len(highest_revenue_ever_df)]=[film['title'],film_revenue['revenue'],
                                                                   (film_revenue['budget'] * -1),
                                                                   film_revenue['release_date'],
                                                                   film_revenue['id'],
                                                                   film_revenue['vote_average'],
                                                                   film_revenue['vote_count']]

highest_revenue_ever_df.head()
print(highest_revenue_ever_df.head())
# response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key + '&primary_release_year=2020&')
'''
res_json = response.json()
with open('data.json', 'w') as f:
    json.dump(res_json, f)


# Pretty Printing JSON string back
print(json.dumps(res_json, indent=4, sort_keys=True))
'''
