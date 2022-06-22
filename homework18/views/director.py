from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
	def get(self):
		"""Получение всех режиссеров"""
		res = director_service.get_all()
		return DirectorSchema(many=True).dump(res), 200

	def post(self):
		"""Добавление режиссера"""
		data = request.json
		director = director_service.create(data)
		return '', 201, {'location': f'/directors/{director.id}'}


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):
	def get(self, director_id):
		"""Получение режиссера"""
		res = director_service.get_by_id(director_id)
		return DirectorSchema().dump(res), 200

	def put(self, director_id):
		"""Обновление данных о режиссере"""
		data = request.json
		data['id'] = director_id
		director_service.update(data)
		return '', 204

	def delete(self, director_id):
		"""Удаление режиссера"""
		director_service.delete(director_id)
		return '', 204
