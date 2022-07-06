from flask import request, abort
import jwt
from constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
	"""Проверка авторизации пользователя"""
	def wrapper(*args, **kwargs):
		if 'Authorization' not in request.headers:
			abort(401)
		token = request.headers.get('Authorization').split()[-1]
		try:
			jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
		except Exception as e:
			print(f'Token decode Exception {e}')
			abort(401)
		return func(*args, **kwargs)
	return wrapper


def admin_required(func):
	"""Проверка авторизации пользователя с правами админа"""
	def wrapper(*args, **kwargs):
		if 'Authorization' not in request.headers:
			abort(401)
		token = request.headers.get('Authorization').split()[1]
		try:
			user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
			if user.get('role') != 'admin':
				print('Не достаточно прав доступа')
				abort(401)
		except Exception as e:
			print(f'Token decode Exception {e}')
			abort(401)
		return func(*args, **kwargs)
	return wrapper
