import logging

import logger as logger
from flask import Flask
from utils import search_by_title, search_by_range_of_years, search_by_rating, search_by_genre

logger.create_logger()

logger = logging.getLogger("basic")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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
        movie_title_release_year = search_by_range_of_years(year_1, year_2)
        return movie_title_release_year
    except:
        return "Ошибка поиска фильма по дате выпуска в прокат"


@app.route('/rating/<rating>')
def search_movie_by_rating(rating):
    logger.debug("Запрошен фильм по рейтингу")
    try:
        if rating == 'children':
            movie_by_rating = search_by_rating('(\'G\')')
        elif rating == 'family':
            movie_by_rating = search_by_rating(('G', 'PG', 'PG-13'))
        elif rating == 'adult':
            movie_by_rating = search_by_rating(('R', 'NC-17'))

        return movie_by_rating
    except:
        return "Ошибка поиска фильма по рейтингу"


@app.route('/genre/<genre>')
def search_movie_by_genre(genre):
    logger.debug("Запрошен фильм по жанру")
    try:
        movie_by_genre = search_by_genre(genre)
        return movie_by_genre
    except:
        return "Ошибка поиска фильма по жанру"


if __name__ == "__main__":
    app.run(debug=True, port=2910)

# genre: Documentaries, Music & Musicals, International TV Shows, Reality TV,
# Documentaries, International Movies, Music & Musicals, Dramas, International Movies, Music & Musicals
# Children & Family Movies, Comedies, International TV Shows, Spanish-Language TV Shows, Stand-Up Comedy & Talk Shows
# Comedies, Horror Movies, Kids TV, Korean TV Shows, TV Comedies
