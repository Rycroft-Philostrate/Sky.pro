import pytest
from unittest.mock import MagicMock

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService
from setup_db import db


@pytest.fixture()
def director_dao():
	director_dao = DirectorDAO(db.session)

	director_1 = Director(id=1, name='Вася')
	director_2 = Director(id=2, name='Петя')

	director_dao.get_one = MagicMock(return_value=director_2)
	director_dao.get_all = MagicMock(return_value=[director_1, director_2])
	director_dao.create = MagicMock(return_value=Director(id=3))
	director_dao.delete = MagicMock()
	director_dao.update = MagicMock()
	return director_dao


class TestDirectorService:
	@pytest.fixture(autouse=True)
	def director_service(self, director_dao):
		self.director_service = DirectorService(dao=director_dao)

	def test_get_one(self):
		director = self.director_service.get_one(2)
		assert director.id is not None

	def test_get_all(self):
		directors = self.director_service.get_all()
		assert len(directors) > 0

	def test_create(self):
		director_d = {
			'name': 'Вова'
		}
		director = self.director_service.create(director_d)
		assert director.id == 3

	def test_update(self):
		director_d = {
			'id': 2,
			'name': 'Вова'
		}
		self.director_service.update(director_d)

	def test_delete(self):
		self.director_service.delete(2)

