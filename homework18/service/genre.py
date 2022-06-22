from dao.genre import GenreDAO


class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def create(self, data_genre):
		return self.dao.create(data_genre)

	def get_by_id(self, genre_id):
		return self.dao.get_by_id(genre_id)

	def get_all(self):
		return self.dao.get_all()

	def update(self, data_genre):
		genre = self.get_by_id(data_genre.get('id'))
		genre.name = data_genre.get('name')
		self.dao.update(genre)

	def delete(self, genre_id):
		genre = self.get_by_id(genre_id)
		self.dao.delete(genre)
