from dao.model.director import Director
from sqlalchemy.exc import SQLAlchemyError


class DirectorDAO:
	def __init__(self, session):
		self.session = session

	def get_all(self):
		return self.session.query(Director).all()

	def get_by_id(self, director_id):
		return self.session.query(Director).get(director_id)

	def create(self, data_director):
		try:
			res = Director(**data_director)
			self.session.add(res)
			self.session.commit()
			return res
		except SQLAlchemyError:
			self.session.rollback()

	def update(self, director):
		try:
			self.session.add(director)
			self.session.commit()
		except SQLAlchemyError:
			self.session.rollback()

	def delete(self, director):
		try:
			self.session.delete(director)
			self.session.commit()
		except SQLAlchemyError:
			self.session.rollback()
