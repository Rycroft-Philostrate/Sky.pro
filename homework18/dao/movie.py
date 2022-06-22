# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например

# class BookDAO:
#     def get_all_books(self):
#         books = Book.query.all()
#         return

from dao.model.movie import Movie
from sqlalchemy.exc import SQLAlchemyError


class MovieDAO:
	def __init__(self, session):
		self.session = session

	def get_all(self):
		return self.session.query(Movie).all()

	def get_by_id(self, movie_id):
		return self.session.query(Movie).get(movie_id)

	def get_by_director_id(self, director_id):
		return self.session.query(Movie).filter(Movie.director_id == director_id).all()

	def get_by_genre_id(self, genre_id):
		return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

	def get_by_year(self, year):
		return self.session.query(Movie).filter(Movie.year == year).all()

	def create(self, data_movie):
		try:
			res = Movie(**data_movie)
			self.session.add(res)
			self.session.commit()
			return res
		except SQLAlchemyError:
			self.session.rollback()

	def update(self, movie):
		try:
			self.session.add(movie)
			self.session.commit()
		except SQLAlchemyError:
			self.session.rollback()

	def delete(self, movie):
		try:
			self.session.delete(movie)
			self.session.commit()
		except SQLAlchemyError:
			self.session.rollback()
