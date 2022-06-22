from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
	def get(self):
		"""Получение жанров"""
		res = genre_service.get_all()
		return GenreSchema(many=True).dump(res), 200

	def post(self):
		"""Добавление жанра"""
		data = request.json
		genre = genre_service.create(data)
		return '', 201, {'location': f'/genres/{genre.id}'}


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
	def get(self, genre_id):
		"""Получение жанра"""
		res = genre_service.get_by_id(genre_id)
		return GenreSchema().dump(res), 200

	def put(self, genre_id):
		"""Обновление данных о жанре"""
		data = request.json
		data['id'] = genre_id
		genre_service.update(data)
		return '', 204

	def delete(self, genre_id):
		"""Удаление жанра"""
		genre_service.delete(genre_id)
		return '', 204
