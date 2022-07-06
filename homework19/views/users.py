from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service
from decorators import auth_required, admin_required

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
	@auth_required
	def get(self):
		"""Получение все пользователей"""
		rs = user_service.get_all()
		res = UserSchema(many=True).dump(rs)
		return res, 200

	def post(self):
		"""Добавление пользователя"""
		req_json = request.json
		user = user_service.create(req_json)
		return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:bid>')
class UserView(Resource):
	@auth_required
	def get(self, bid):
		"""Получение пользователя"""
		print(request.authorization)
		r = user_service.get_one(bid)
		sm_d = UserSchema().dump(r)
		return sm_d, 200

	@admin_required
	def put(self, bid):
		"""Обновление данных о пользователе"""
		req_json = request.json
		if "id" not in req_json:
			req_json["id"] = bid
		user_service.update(req_json)
		return "", 204

	@admin_required
	def delete(self, bid):
		"""Удаление пользователя"""
		user_service.delete(bid)
		return "", 204
