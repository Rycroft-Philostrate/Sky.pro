from dao.model.genre import Genre
from sqlalchemy.exc import SQLAlchemyError


class GenreDAO:
	def __init__(self, session):
		self.session = session

	def get_all(self):
		return self.session.query(Genre).all()

	def get_by_id(self, genre_id):
		return self.session.query(Genre).get(genre_id)

	def create(self, data_genre):
		try:
			res = Genre(**data_genre)
			self.session.add(res)
			self.session.commit()
			return res
		except SQLAlchemyError:
			self.session.rollback()

	def update(self, genre):
		try:
			self.session.add(genre)
			self.session.commit()
		except SQLAlchemyError:
			self.session.rollback()

	def delete(self, genre):
		try:
			self.session.delete(genre)
			self.session.commit()
		except SQLAlchemyError:
			self.session.rollback()
