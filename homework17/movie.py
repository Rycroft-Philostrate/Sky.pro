from flask_restx import Resource, Namespace
from flask import request
from sqlalchemy.exc import SQLAlchemyError

from schemas import MoviesSchema
from utils import *

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Получение фильмов"""
        args = request.args
        query_director_id = args.get('director_id', type=int)
        query_genre_id = args.get('genre_id', type=int)
        if query_director_id is None and query_genre_id is None:
            res = get_movie_all()
            return MoviesSchema(many=True).dump(res), 200
        elif query_genre_id is None:
            res = get_movie_director_id(query_director_id)
            return MoviesSchema(many=True).dump(res), 200
        elif query_director_id is None:
            res = get_movie_genre_id(query_genre_id)
            return MoviesSchema(many=True).dump(res)
        else:
            res = get_movie_director_genre_id(query_director_id, query_genre_id)
            return MoviesSchema(many=True).dump(res), 200

    def post(self):
        """Добавление фильма"""
        try:
            data = request.json
            movie = post_movie(data)
            return '', 201, {"location": f"/movies/{movie.id}"}
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка записи в БД!'


@movie_ns.route('/<int:movie_id>', methods=['PUT', 'GET', 'DELETE'])
class MovieViewId(Resource):
    def get(self, movie_id):
        """Получение фильма"""
        res = get_movie_id(movie_id)
        return MoviesSchema().dump(res), 200

    def put(self, movie_id):
        """Обновление данных о фильме"""
        try:
            data = request.json
            put_movie_id(data, movie_id)
            return '', 204
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка обновления записи в БД!'

    def delete(self, movie_id):
        """Удаление фильма"""
        try:
            delete_movie_id(movie_id)
            return '', 204
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка удаления данных из БД!'
