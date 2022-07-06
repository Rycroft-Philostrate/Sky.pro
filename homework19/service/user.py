import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_one(self, bid):
		return self.dao.get_one(bid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, user_d):
		user_d['password'] = self.get_hash(user_d.get('password'))
		return self.dao.create(user_d)

	def update(self, user_d):
		self.dao.update(user_d)
		return self.dao

	def delete(self, rid):
		self.dao.delete(rid)

	def get_hash(self, password):
		hash_digest = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
		)
		return base64.b64encode(hash_digest)

	def get_by_username(self, username):
		return self.dao.get_by_username(username)

	def compare_password(self, password_hash, password):
		decode_digest = base64.b64decode(password_hash)
		hash_digest = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
		)
		return hmac.compare_digest(decode_digest, hash_digest)
