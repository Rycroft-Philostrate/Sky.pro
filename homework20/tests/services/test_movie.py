import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from dao.model.genre import Genre
from dao.model.director import Director
from setup_db import db


@pytest.fixture()
def movie_dao():
	movie_dao = MovieDAO(db.session)

	movie_1 = Movie(id=1, title='огонь', description='Info', trailer='Trailer', year=2021, rating=7.4, genre_id=1, director_id=1)
	movie_2 = Movie(id=2, title='лед', description='Info', trailer='Trailer', year=2022, rating=8.2, genre_id=1, director_id=1)

	movie_dao.get_one = MagicMock(return_value=movie_2)
	movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
	movie_dao.create = MagicMock(return_value=Movie(id=3))
	movie_dao.delete = MagicMock()
	movie_dao.update = MagicMock()
	return movie_dao


class TestMovieService:
	@pytest.fixture(autouse=True)
	def movie_service(self, movie_dao):
		self.movie_service = MovieService(dao=movie_dao)

	def test_get_one(self):
		movie = self.movie_service.get_one(2)
		assert movie.id is not None

	def test_get_all(self):
		movies = self.movie_service.get_all()
		assert len(movies) > 0

	def test_create(self):
		movie_d = {
			'title': 'земля',
			'description': 'Info',
			'trailer': 'Trailer',
			'year': 2020,
			'rating': 9.1,
			'genre_id': 2,
			'director_id': 2
		}
		movie = self.movie_service.create(movie_d)
		assert movie.id == 3

	def test_partially_update(self):
		movie_d = {
			'id': 1,
			'trailer': 'Trailer_34',
			'year': 2020,
		}
		self.movie_service.partially_update(movie_d)

	def test_update(self):
		movie_d = {
			'id': 2,
			'title': 'земля',
			'description': 'Info',
			'trailer': 'Trailer',
			'year': 2020,
			'rating': 9.1,
			'genre_id': 2,
			'director_id': 2
		}
		self.movie_service.update(movie_d)

	def test_delete(self):
		self.movie_service.delete(2)

