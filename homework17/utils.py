from models import *


def get_movie_all():
	"""Получение всех фильмов"""
	return Movie.query.all()


def get_movie_director_id(director_id):
	"""Получение всех фильмов по id режисера"""
	return Movie.query.join(Director, Movie.director_id == Director.id).filter(Director.id == director_id).all()


def get_movie_genre_id(genre_id):
	"""Получение всех фильмов и по id жанра"""
	return Movie.query.join(Genre, Movie.genre_id == Genre.id).filter(Genre.id == genre_id).all()


def get_movie_director_genre_id(director_id, genre_id):
	"""Получение всех фильмов по id режисера и по id жанра"""
	return Movie.query.join(Director, Movie.director_id == Director.id).join(Genre, Movie.genre_id == Genre.id).filter(
		Genre.id == genre_id).filter(Director.id == director_id).all()


def post_movie(data):
	"""Дабвление фильма в БД"""
	res = Movie(**data)
	db.session.add(res)
	db.session.commit()
	return res


def get_movie_id(movie_id):
	"""Получение фильма по id"""
	return Movie.query.get(movie_id)


def put_movie_id(data, movie_id):
	"""Обновление данных о фильме по id"""
	movie = get_movie_id(movie_id)
	movie.title = data.get('title')
	movie.description = data.get('description')
	movie.trailer = data.get('trailer')
	movie.year = data.get('year')
	movie.rating = data.get('rating')
	movie.genre_id = data.get('genre_id')
	movie.director_id = data.get('director_id')
	db.session.add(movie)
	db.session.commit()


def delete_movie_id(movie_id):
	"""Удаление фильма по id из БД"""
	movie = get_movie_id(movie_id)
	db.session.delete(movie)
	db.session.commit()


def get_director_all():
	"""Получение всех режисеров"""
	return Director.query.all()


def post_director(data):
	"""Добавление режисера в БД"""
	res = Director(**data)
	db.session.add(res)
	db.session.commit()
	return res


def get_director_id(director_id):
	"""Получение режисера по id"""
	return Director.query.get(director_id)


def put_director_id(data, director_id):
	"""Обноление данных режисера по id"""
	director = get_director_id(director_id)
	director.name = data.get('name')
	db.session.add(director)
	db.session.commit()


def delete_director_id(director_id):
	"""Удаление режисера по id из БД"""
	director = get_director_id(director_id)
	db.session.delete(director)
	db.session.commit()


def get_genre_all():
	"""Получение всех жанров"""
	return Genre.query.all()


def post_genre(data):
	"""Добавление жанра в БД"""
	res = Director(**data)
	db.session.add(res)
	db.session.commit()
	return res


def get_genre_id(genre_id):
	"""Получение жанра по id"""
	return Genre.query.get(genre_id)


def put_genre_id(data, genre_id):
	"""Обновление ланных о жанре по id"""
	genre = get_genre_id(genre_id)
	genre.name = data.get('name')
	db.session.add(genre)
	db.session.commit()


def delete_genre_id(genre_id):
	"""Удаление жанра по id из БД"""
	genre = get_genre_id(genre_id)
	db.session.delete(genre)
	db.session.commit()
