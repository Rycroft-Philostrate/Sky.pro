from flask_restx import Resource, Namespace
from flask import request
from sqlalchemy.exc import SQLAlchemyError

from schemas import GenreSchema
from utils import *

genres_ns = Namespace('genres')


@genres_ns.route('/genres/')
class GenreViewId(Resource):
    def get(self):
        """Получение всех жанров"""
        res = get_genre_all()
        return GenreSchema(many=True).dump(res), 200

    def post(self):
        """Добавление жанра"""
        try:
            data = request.json
            genre = post_genre(data)
            return '', 201, {"location": f"/genres/{genre.id}"}
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка записи в БД!'


@genres_ns.route('/genres/<int:genre_id>')
class GenreViewId(Resource):
    def get(self, genre_id):
        """Получение жанра"""
        res = get_genre_id(genre_id)
        return GenreSchema().dump(res), 200

    def put(self, genre_id):
        """Обновление данных о жанре"""
        try:
            data = request.json
            put_genre_id(data, genre_id)
            return '', 204
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка обновления записи в БД!'

    def delete(self, genre_id):
        """Удаление жанра"""
        try:
            delete_genre_id(genre_id)
            return '', 204
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка удаления данных из БД!'
