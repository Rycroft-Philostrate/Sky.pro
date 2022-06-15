from flask_restx import Resource, Namespace
from flask import request
from sqlalchemy.exc import SQLAlchemyError

from schemas import DirectorSchema
from utils import *

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Получение всех режиссеров"""
        res = get_director_all()
        return DirectorSchema(many=True).dump(res), 200

    def post(self):
        """Добавление режиссера"""
        try:
            data = request.json
            director = post_director(data)
            return '', 201, {"location": f"/directors/{director.id}"}
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка записи в БД!'


@directors_ns.route('/<int:director_id>')
class DirectorViewId(Resource):
    def get(self, director_id):
        """Получение режиссера"""
        res = get_director_id(director_id)
        return DirectorSchema().dump(res), 200

    def put(self, director_id):
        """Обновление данных о режиссере"""
        try:
            data = request.json
            put_director_id(data, director_id)
            return '', 204
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка обновления записи в БД!'

    def delete(self, director_id):
        """Удаление режиссера"""
        try:
            delete_director_id(director_id)
            return '', 204
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка удаления данных из БД!'
