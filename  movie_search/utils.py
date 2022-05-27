import json
import sqlite3


def movie_info(_title):
    with sqlite3.connect("../netflix.db") as connection:
        cursor = connection.cursor()
        # query = """
        #             SELECT COUNT(*), title, country, release_year, listed_in, description
        #             FROM netflix
        #             WHERE type = 'Movie'
        #             GROUP BY country
        #             ORDER BY COUNT(*) DESC
        #             LIMIT 2
        #           """
        query = """
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE type = 'Movie'
            AND title = '""" + _title + """'
            ORDER BY release_year DESC
            LIMIT 1
          """
        cursor.execute(query)
        title = cursor.fetchall()[0]

    title_movie = {
        "title": title[0],
        "country": title[1],
        "release_year": title[2],
        "genre": title[3],
        "description": title[4]
    }

    json_title_movie = json.dumps(title_movie)

    return json_title_movie


print(movie_info("Break"))
