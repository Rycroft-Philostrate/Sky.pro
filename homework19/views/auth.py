from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """Авторизация пользователя, получение токена"""
        res = request.json
        if None in [res.get('username'), res.get('password')]:
            return 'Не переданы данные пользователя', 401
        return auth_service.create_token(res.get('username'), res.get('password'))

    def put(self):
        """Обновление токена"""
        res = request.json
        return auth_service.check_refresh_token(res.get('refresh_token'))
