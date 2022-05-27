import logging

from flask import app, Flask
from utils import movie_info

logger = logging.getLogger("../basic")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<_title>')
def search_title_movie(_title):
    logger.debug("Запрошен фильм")
    try:
        title_movie = movie_info(_title)
        return title_movie
    except:
        return "Ошибка поиска фильма по названию"


if __name__ == "__main__":
    app.run(debug=True, port=2910)
#
# @movie_blueprint.route('/movie/<title>')
# def post_one(post_pk):
#     logger.debug(f"Запрошен пост {post_pk}")
#     try:
#         post = posts_dao.get_by_pk(post_pk)
#         comments = comments_dao.get_by_post_pk(post_pk)
#         number_of_comments = len(comments)
#         return render_template('post.html', post=post, comments=comments,
#                                number_of_comments=number_of_comments)
#     except:
#         return "Ошибка открытия одного поста с комментами"
#
#
# @posts_blueprint.route('/search/')
# def post_search():
#     query = request.args.get("s", "")
#     logger.debug("Запрошены посты по вхождению")
#     try:
#         if query != "":
#             posts = posts_dao.search(query)
#             number_of_posts = len(posts)
#         else:
#             posts = []
#             number_of_posts = 0
#         return render_template('search.html', query=query, posts=posts, number_of_posts=number_of_posts)
#     except:
#         return "Ошибка при поиске по вхождению"
#
#
# @posts_blueprint.route('/users/<username>/')
# def post_by_user(username):
#     logger.debug("Запрошен пост по имени")
#     try:
#         posts_by_user = posts_dao.get_by_user(username)
#         number_of_posts = len(posts_by_user)
#         return render_template('user_feed.html', posts_by_user=posts_by_user, number_of_posts=number_of_posts)
#     except:
#         return "Ошибка открытия поста по имени"
