# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
# from flask_restx import Resource, Namespace
#
# book_ns = Namespace('books')
#
#
# @book_ns.route('/')
# class BooksView(Resource):
#     def get(self):
#         return "", 200
#
#     def post(self):
#         return "", 201

from flask_restx import Resource, Namespace
from flask import request

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
	def get(self):
		"""Получение фильмов"""
		filters = {
			'director_id': request.args.get('director_id'),
			'genre_id': request.args.get('genre_id'),
			'year': request.args.get('year')
		}
		res = movie_service.get_all(filters)
		return MovieSchema(many=True).dump(res), 200

	def post(self):
		"""Добавление фильма"""
		data = request.json
		movie = movie_service.create(data)
		return '', 201, {'location': f'/movies/{movie.id}'}


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
	def get(self, movie_id):
		"""Получение фильма"""
		res = movie_service.get_by_id(movie_id)
		return MovieSchema().dump(res), 200

	def put(self, movie_id):
		"""Обновление данных о фильме"""
		data = request.json
		data['id'] = movie_id
		movie_service.update(data)
		return '', 204

	def delete(self, movie_id):
		"""Удаление фильма"""
		movie_service.delete(movie_id)
		return '', 204
