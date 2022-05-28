import logging

import logger as logger
from flask import Flask, jsonify
from utils import search_by_title, search_by_range_of_years, search_by_rating, search_by_genre

logger.create_logger()

logger = logging.getLogger("basic")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
def search_movie_by_title(title):
    logger.debug("Запрошен фильм по названию")
    try:
        movie_title = search_by_title(title)
        return movie_title
    except:
        return "Ошибка поиска фильма по названию"


@app.route('/movie/<int:year_1>/to/<int:year_2>')
def search_movie_by_range_of_years(year_1, year_2):
    logger.debug("Запрошен фильм по дате выпуска в прокат")
    try:
        movie_title_release_year = jsonify(search_by_range_of_years(year_1, year_2))
        return movie_title_release_year
    except:
        return "Ошибка поиска фильма по дате выпуска в прокат"


@app.route('/rating/<rating>')
def search_movie_by_rating(rating):
    logger.debug("Запрошен фильм по рейтингу")
    try:
        movie_by_rating = jsonify(search_by_rating(rating))
        return movie_by_rating
    except:
        return "Ошибка поиска фильма по рейтингу"


@app.route('/genre/<genre>')
def search_movie_by_genre(genre):
    logger.debug("Запрошен фильм по жанру")
    try:
        movie_by_genre = jsonify(search_by_genre(genre))
        return movie_by_genre
    except:
        return "Ошибка поиска фильма по жанру"


if __name__ == "__main__":
    app.run(debug=True, port=2910)
