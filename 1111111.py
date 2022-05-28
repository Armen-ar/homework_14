# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# ____________________________________________________________
# rating — возрастной рейтинг

# ('TV-MA',)
# ('R',)
# ('PG-13',)
# ('TV-14',)
# ('TV-PG',)
# ('NR',)
# ('TV-G',)
# ('TV-Y',)
# ('',)
# ('TV-Y7',)
# ('PG',)
# ('G',)
# ('NC-17',)
# ('TV-Y7-FV',)
# ('UR',)
# ___________________________________________________________
"""
Агрегирующие функции

COUNT()
DISTINCT
SUM()
AVG()
MIN()
MAX()
"""

import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query_1 = """
        SELECT COUNT()
        FROM netflix
    """
    query_2 = """
        SELECT COUNT(*)  
        FROM netflix
        GROUP BY director
    """  # COUNT(*) количество строчек, только по столбцу director
    query_3 = """
        SELECT COUNT(DISTINCT director)  
        FROM netflix
    """  # COUNT(DISTINCT, director) количество строчек, только по столбцу director уникальные(без повторов)
    query_4 = """
        SELECT COUNT(*), country  
        FROM netflix
        WHERE country != ''
        GROUP BY country
    """  # COUNT(*) количество строчек, только по столбцу country
    query_5 = """
        SELECT MIN(release_year), MAX(release_year)
        FROM netflix
    """
    query_6 = """
        SELECT type, country, AVG(duration)  
        FROM netflix
        GROUP BY type, country
    """  # средняя продолжительность фильмов в минутах, сериалов в сезонах и сгруппированные по странам
    query_7 = """
        SELECT country, SUM(duration)
        FROM netflix
        WHERE type = 'TV Show'
        GROUP BY country
        ORDER BY SUM(duration)
        LIMIT 10
    """  # количество сезонов в сериалах по всем странам (вывод по 10 строк), сортированная от меньшего по умолчанию
    query_8 = """
        SELECT country, SUM(duration) AS total_duration
        FROM netflix
        WHERE type = 'TV Show'
        AND country != ''
        GROUP BY country
        ORDER BY total_duration DESC
        LIMIT 10
    """  # количество сезонов в сериалах по всем странам (вывод по 10 строк), сортированная от большего,
    # но с псевдонимом SUM(duration) перезаписывает в total_duration

    # cursor.execute(query_8)
    #
    # for row in cursor.fetchall():
    #     print(row)
# ___________________________________________________________
"""
Фильтрация данных
Условия - совпадение, диапазоны, вхождения, пустые значения
Комбинации - логические операторы
"""
import sqlite3

with sqlite3.connect(
        "netflix.db") as connection:  # переменная это объект соединения, который управляет подключение к файлу

    cursor = connection.cursor()  # переменная это объект соединения для передачи команд от приложения в БД и наоборот
    query_1 = """              
        SELECT director, duration
        FROM netflix
        WHERE director = 'Cristina Jacob'
        AND duration > 110
    """
    query_2 = """              
        SELECT title, country
        FROM netflix
        WHERE "cast" LIKE '%Maria%'
    """
    query_3 = """              
        SELECT title, country
        FROM netflix
        WHERE country = 'Argentina' OR country = 'Armenia'
    """
    query_4 = """              
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN 1945 AND 1950
        AND director != '' AND director IS NOT NULL
        ORDER BY release_year DESC
    """
    query_5 = """              
        SELECT *
        FROM netflix
    """
    query_6 = """              
        SELECT title, release_year
        FROM netflix
        WHERE release_year > 1945 AND release_year < 1950
        AND director != '' AND director IS NOT NULL
        ORDER BY release_year DESC
    """
    # * выводит все столбцы запрос:
    # SELECT DISTINCT получает значения без повторов уникальные
    # SELECT вместо * (всё) конкретно те столбцы, которые хотим видеть
    # director (режиссёр), duration (продолжительность), title (название), country (страны)
    # WHERE (где) значение число, то просто число
    # если строка в кавычках одинарных названия строки '',
    # а двойные кавычки "" названия столбцов
    # можно и писать director == 'Cristina Jacob'
    # отрицание director != 'Cristina Jacob'
    # может быть > < значение число
    # и дополнительное условие AND duration > 110 (продолжительность больше 110 мин.)
    # если условие вывода задаём WHERE country = 'Argentina' OR (или) country = 'Armenia'
    # или можно WHERE country IN (Argentina, Armenia, .....) если нужно перечислять много стран
    # WHERE country LIKE (похожая) 'A%' (% знак после буквы значит страны, которые начинаются с А)
    # '%A' в конце слова и '%A%' в середине слова
    # WHERE "cast" (играет) LIKE '%Maria%'
    # cast это зарезервированное слово, поэтому нужно писать в двойных кавычках или с название файла netflix.cast
    # release_year > 2000 все фильмы производство после 2000 года
    # можно писать интервал так: release_year < 1950(не включительно) AND release_year > 1945(не включительно)
    # но можно писать BETWEEN совпадение в числах между 1945 AND 1950 (включительно обе границы)
    # AND director IS NOT NULL означает эта строка не заполнена вообще
    # ORDER BY release_year DESC  сортировка от большего к меньшему
    # ГРУППИРОВКА ставится в конце, т.е. на полученном результате
    # ORDER BY release_year ASC  сортировка от меньшего к большему (применяется по умолчанию)
    # GROUP BY type, country группировка по типу
    # __________________________________________________________________________________________
    # GROUP BY - это ключевое слово для агрегирующих функций
    # COUNT - функция агрегации строк, которая считает и возвращает количество записей в группе
    # SUM - функция, которая считает сумму всех значений из столбца в группе
    # AVG - функция, которая считает среднее арифметическое значения столбца в группе
    # MIN - функция, которая определяет минимальное значение в столбце группы
    # MAX - функция, которая определяет максимальное значение в столбце группы
    # HAVING - это условие после группировки

    # cursor.execute(query_6)  # меняя номер переменной можно получить разные выводы
    #
    # for row in cursor.fetchall():  # вывести на каждую строчку
    #     print(row)

# ___________________________________________________________
# con = sqlite3.connect("../netflix.db")
# cur = con.cursor()
# sqlite_query = """
#         SELECT COUNT(*), type, country
#         FROM netflix
#         WHERE country LIKE '%India%'
#         GROUP BY type
#     """
# cur.execute(sqlite_query)
# executed_query = cur.fetchall()
#
# # для последующей выдачи в требуемом формате
#
# result = f"фильмы: {executed_query[0][0]} шт\сериалы: {executed_query[1][0]} шт"
#
# con.close()
#
# if __name__ == '__main__':
#     print(result)

# ___________________________________________________________
# with open("books.json", "r", encoding="utf-8") as file:
#     books = json.load(file)
# return books

# ___________________________________________________________
# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def get_json():
#     data = {"name": "Алиса"}
#     return jsonify(data)
#
#
# if __name__ == "__main__":
#     app.run()

# ___________________________________________________________
import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = """
        SELECT title, MAX(date_added)
        FROM netflix
    """
cur.execute(sqlite_query)
executed_query = cur.fetchall()[0][0]

# для последующей выдачи в требуемом формате

result = f"{executed_query}"

if __name__ == '__main__':
    print(result)

# _____________________________________________________
# @app.route('/rating/<rating>')
# def movie_rating_search(rating):
#     logger.debug("Запрошен фильм по рейтингу")
#     try:
#         if rating == 'children':
#             movie_by_rating = search_by_rating('(\'G\')')  # ('(\'G\')') для того, чтоб вывел ('G')
#         elif rating == 'family':
#             movie_by_rating = search_by_rating(('G', 'PG', 'PG-13'))
#         elif rating == 'adult':
#             movie_by_rating = search_by_rating(('R', 'NC-17'))
#
#         return movie_by_rating
#     except:
#         return "Ошибка поиска фильма по рейтингу"
