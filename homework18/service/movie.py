# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример

# class BookService:
#
#     def __init__(self, book_dao: BookDAO):
#         self.book_dao = book_dao
#
#     def get_books(self) -> List["Book"]:
#         return self.book_dao.get_books()

from dao.movie import MovieDAO


class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def create(self, data_movie):
		return self.dao.create(data_movie)

	def get_by_id(self, movie_id):
		return self.dao.get_by_id(movie_id)

	def get_all(self, filters):
		if filters.get('director_id') is not None:
			return self.dao.get_by_director_id(filters.get('director_id'))
		elif filters.get('genre_id') is not None:
			return self.dao.get_by_genre_id(filters.get('genre_id'))
		elif filters.get('year') is not None:
			return self.dao.get_by_year(filters.get('year'))
		else:
			return self.dao.get_all()

	def update(self, data_movie):
		movie = self.get_by_id(data_movie.get('id'))
		movie.title = data_movie.get('title')
		movie.description = data_movie.get('description')
		movie.trailer = data_movie.get('trailer')
		movie.year = data_movie.get('year')
		movie.rating = data_movie.get('rating')
		movie.genre_id = data_movie.get('genre_id')
		movie.director_id = data_movie.get('director_id')
		self.dao.update(movie)

	def delete(self, movie_id):
		movie = self.get_by_id(movie_id)
		self.dao.delete(movie)
