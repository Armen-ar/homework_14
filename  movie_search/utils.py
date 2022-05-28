import json
import sqlite3


def search_by_title(title):
    with sqlite3.connect("../netflix.db") as connection:
        cursor = connection.cursor()
        query = (f"""SELECT title, country, release_year, listed_in, description
                FROM netflix 
                WHERE type = 'Movie' AND title LIKE '{title}%'
                ORDER BY release_year DESC LIMIT 1
                """
                 )
        cursor.execute(query)
        title_movie = cursor.fetchall()[0]

    movie_title = {
        "title": title_movie[0],
        "country": title_movie[1],
        "release_year": title_movie[2],
        "genre": title_movie[3],
        "description": title_movie[4]
    }

    json_movie_title = json.dumps(movie_title)

    return json_movie_title


def search_by_range_of_years(year_1, year_2):
    with sqlite3.connect("../netflix.db") as connection:
        cursor = connection.cursor()
        query = (f"""SELECT title, release_year
                FROM netflix
                WHERE release_year BETWEEN '{year_1}' AND '{year_2}'
                ORDER BY release_year
                LIMIT 100
                """
                 )
        cursor.execute(query)
        range_of_years = cursor.fetchall()

        movie_title_release_year = []
        for i in range_of_years:
            movie_title = {
                "title": i[0],
                "release_year": i[1],
            }
            movie_title_release_year.append(movie_title)

        json_movie_by_range_of_years = json.dumps(movie_title_release_year)

        return json_movie_by_range_of_years


def search_by_rating(rating):
    with sqlite3.connect("../netflix.db") as connection:
        cursor = connection.cursor()
        query = (f"""SELECT title, rating, description
                FROM netflix
                WHERE rating IN {rating}
                LIMIT 100
                """
                 )
        cursor.execute(query)
        by_rating = cursor.fetchall()

        movie_by_rating = []
        for i in by_rating:
            movie_one_by_rating = {
                "title": i[0],
                "rating": i[1],
                "description": i[2]
            }
            movie_by_rating.append(movie_one_by_rating)

        json_movie_by_rating = json.dumps(movie_by_rating)

        return json_movie_by_rating


def search_by_genre(genre):
    with sqlite3.connect("../netflix.db") as connection:
        cursor = connection.cursor()
        query = (f"""SELECT title, description
                FROM netflix
                WHERE listed_in = {genre}
                ORDER BY release_year DESC
                LIMIT 10
                """
                 )
        cursor.execute(query)
        by_genre = cursor.fetchall()

        movie_by_genre = []
        for i in by_genre:
            movie_one_by_genre = {
                "title": i[0],
                "description": i[1]
            }
            movie_by_genre.append(movie_one_by_genre)

        json_movie_by_genre = json.dumps(movie_by_genre)

        return json_movie_by_genre


def search_by_actors(actor_1, actor_2):
    with sqlite3.connect("../netflix.db") as connection:
        cursor = connection.cursor()
        query = (f"""SELECT netflix.cast
                FROM netflix
                WHERE netflix.cast LIKE '%{actor_1}%' AND netflix.cast LIKE '%{actor_2}%'
                """
                 )
        cursor.execute(query)
        movie_by_actors = cursor.fetchall()

        movie_by_actors_all = []
        for i in movie_by_actors:
            movie_by_actor = {
                "cast": i[0]
            }
            movie_by_actors_all.append(movie_by_actor)

        json_movie_by_actors_all = json.dumps(movie_by_actors_all)

    return json_movie_by_actors_all


# print(search_by_title('Am'))
# print(search_by_range_of_years(2019, 2020))
# print(search_by_genre('listed_in'))
# print(search_by_actors('Rose McIver', 'Ben Lamb'))
# print(search_by_actors('Jack Black', 'Dustin Hoffman'))
