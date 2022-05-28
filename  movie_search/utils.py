import sqlite3
from collections import Counter

from flask import jsonify


def execute_query(query):
    with sqlite3.connect("../netflix.db") as connection:
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


def search_by_title(title):
    query = f"""SELECT title, country, release_year, listed_in, description
    FROM netflix 
    WHERE type = 'Movie' AND title LIKE '{title}%'
    ORDER BY release_year DESC LIMIT 1
    """

    title_movie = execute_query(query)

    movie_title = {
        "title": title_movie[0][0],
        "country": title_movie[0][1],
        "release_year": title_movie[0][2],
        "genre": title_movie[0][3],
        "description": title_movie[0][4]
    }

    json_movie_title = jsonify(movie_title)

    return json_movie_title


def search_by_range_of_years(year_1, year_2):
    query = f"""SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN '{year_1}' AND '{year_2}'
    ORDER BY release_year
    LIMIT 100
    """

    range_of_years = execute_query(query)

    movie_title_release_year = []
    for movie in range_of_years:
        movie_title = {
            "title": movie[0],
            "release_year": movie[1],
        }

        movie_title_release_year.append(movie_title)

    return movie_title_release_year


def search_by_rating(rating):
    parameters = {
        "children": "'G'",
        "family": "'G', 'PG', 'PG-13'",
        "adult": "'R', 'NC-17'"
    }
    if rating not in parameters:
        return "Введённой группы не существует"

    query = f"""SELECT title, rating, description
    FROM netflix
    WHERE rating IN ({parameters[rating]})
    """

    movie_by_rating_all = execute_query(query)

    movie_by_rating = []
    for movie in movie_by_rating_all:
        movie_one_by_rating = {
            "title": movie[0],
            "rating": movie[1],
            "description": movie[2]
        }
        movie_by_rating.append(movie_one_by_rating)

    return movie_by_rating


def search_by_genre(genre):
    query = f"""SELECT title, description
    FROM netflix
    WHERE listed_in LIKE '%{genre}%'
    ORDER BY release_year DESC
    LIMIT 10
    """

    by_genre = execute_query(query)

    movie_by_genre = []
    for movie in by_genre:
        movie_one_by_genre = {
            "title": movie[0],
            "description": movie[1]
        }
        movie_by_genre.append(movie_one_by_genre)

    return movie_by_genre


def search_by_actors(actor_1, actor_2):
    query = f"""SELECT `cast`
    FROM netflix
    WHERE `cast` LIKE '%{actor_1}%' AND `cast` LIKE '%{actor_2}%'
    """

    movie_by_actors_all = execute_query(query)

    movie_by_actors = []
    for cast in movie_by_actors_all:
        movie_by_actors.extend(cast[0].split(', '))
    counter = Counter(movie_by_actors)

    movie_by_actor = []
    for actor, count in counter.items():
        if actor not in [actor_1, actor_2] and count > 2:
            movie_by_actor.append(actor)

    return movie_by_actor


# print(search_by_actors('Rose McIver', 'Ben Lamb'))
# print(search_by_actors('Jack Black', 'Dustin Hoffman'))


def search_movie_by_param(type_movie, release_year, genre):
    query = f"""SELECT title, description
    FROM netflix
    WHERE type = '{type_movie}' AND release_year = {release_year} AND listed_in LIKE '%{genre}%'
    """

    by_param = execute_query(query)

    movie_by_param = []
    for movie in by_param:
        movie_one_by_param = {
            "title": movie[0],
            "description": movie[1]
        }

        movie_by_param.append(movie_one_by_param)

    return movie_by_param


# print(search_movie_by_param('Movie', 2017, 'Documentaries'))
