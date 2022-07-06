import calendar

import jwt
from datetime import datetime, timedelta

from flask_restx import abort

from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService:
	def __init__(self, user_service: UserService):
		self.user_service = user_service

	def create_token(self, username, password, check_refresh=False):
		user = self.user_service.get_by_username(username)
		if user is None:
			abort(404)
		if not check_refresh:
			if not self.user_service.compare_password(user.password, password):
				abort(400)
		min30 = datetime.utcnow() + timedelta(minutes=30)
		data = {'username': user.username, 'role': user.role, 'exp': calendar.timegm(min30.timetuple())}
		access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
		days30 = datetime.utcnow() + timedelta(days=30)
		data = {'username': user.username, 'role': user.role, 'exp': calendar.timegm(days30.timetuple())}
		refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)
		return {'access_token': access_token, 'refresh_token': refresh_token}

	def check_refresh_token(self, refresh_token):
		data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
		username = data.get('username')
		exp = data.get('exp')
		user = self.user_service.get_by_username(username)
		if user is None:
			abort(404)
		if not datetime.fromtimestamp(exp) >= datetime.utcnow():
			abort(401)
		return self.create_token(user.username, user.password, check_refresh=True)
