from dao.director import DirectorDAO


class DirectorService:
	def __init__(self, dao: DirectorDAO):
		self.dao = dao

	def create(self, data_director):
		return self.dao.create(data_director)

	def get_by_id(self, director_id):
		return self.dao.get_by_id(director_id)

	def get_all(self):
		return self.dao.get_all()

	def update(self, data_director):
		director = self.get_by_id(data_director.get('id'))
		director.name = data_director.get('name')
		self.dao.update(director)

	def delete(self, director_id):
		director = self.get_by_id(director_id)
		self.dao.delete(director)
