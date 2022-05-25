import sqlite3 as sql

data = 'netflix.db'


def find_movie_name(title):
	"""Поиск фильмов по названию"""
	with sql.connect(data) as con:
		con.row_factory = sql.Row
		cursor = con.cursor()
		cursor.execute(f"""SELECT title, country, release_year, listed_in as genre, description
		FROM netflix
		WHERE LOWER(title) = '{title.lower()}'
		ORDER BY release_year DESC
		""")
		return dict(cursor.fetchone())


def find_movie_year(year_1, year_2):
	"""Поиск фильмов по диапазону годов релиза"""
	result = []  # список найденных фильмов
	with sql.connect(data) as con:
		con.row_factory = sql.Row
		cursor = con.cursor()
		cursor.execute(f"""SELECT title, release_year
		FROM netflix
		WHERE release_year BETWEEN {year_1} AND {year_2}
		LIMIT 100
		""")
		for el in cursor.fetchall():
			result.append(dict(el))
	return result


def find_rating(rating):
	"""Посик фильмов по рейтингу"""
	group_rating = {'children': ('G', 'G'), 'family': ('G', 'PG', 'PG-13'), 'adult': ('R', 'NC-17')}
	result = []  # список найденных фильмов
	with sql.connect(data) as con:
		con.row_factory = sql.Row
		cursor = con.cursor()
		cursor.execute(f"""SELECT title, rating, description
		FROM netflix
		WHERE rating IN {group_rating[rating]}
		""")
		for el in cursor.fetchall():
			result.append(dict(el))
	return result


def find_genre(genre):
	"""Поиск фильмов по жанру"""
	result = []  # список найденных фильмов
	with sql.connect(data) as con:
		con.row_factory = sql.Row
		cursor = con.cursor()
		cursor.execute(f"""SELECT title, description
		FROM netflix
		WHERE LOWER(listed_in) LIKE '%, {genre.lower()}, %' OR LOWER(listed_in) LIKE '{genre.lower()}, %'
		OR LOWER(listed_in) LIKE '%, {genre.lower()}' OR LOWER(listed_in) LIKE '{genre.lower()}'
		ORDER BY release_year DESC
		LIMIT 10
		""")
		for el in cursor.fetchall():
			result.append(dict(el))
	return result


def find_cast(actor_1, actor_2):
	"""Ищем актеров играющих с двумя данными в паре больше двух раз"""
	result = []  # список актеров
	with sql.connect(data) as con:
		cursor = con.cursor()
		cursor.execute(f"""SELECT "cast"
		FROM netflix
		WHERE (LOWER("cast") LIKE '%, {actor_1.lower()}, %' OR LOWER("cast") LIKE '{actor_1.lower()}, %'
		OR LOWER("cast") LIKE '%, {actor_1.lower()}') AND (LOWER("cast") LIKE '%, {actor_2.lower()}, %'
		OR LOWER("cast") LIKE '{actor_2.lower()}, %' OR LOWER("cast") LIKE '%, {actor_2.lower()}')
		""")
		list_actor = []  # список всех актеров фильмов где встречаются два данных актера
		for el in cursor.fetchall():
			list_actor.extend(el[0].split(', '))
	for el in list_actor:  # ищем актеров встречающихся больше двух раз с данными актерами
		if el.lower() not in (actor_1.lower(), actor_2.lower()) and list_actor.count(el) > 2 and el not in result:
			result.append(el)
	return result


def find_movies(type_movie, year, genre):
	"""Поиск фильмов по трем критериям (тип, год, жанр)"""
	result = []  # список фильмов
	with sql.connect(data) as con:
		con.row_factory = sql.Row
		cursor = con.cursor()
		cursor.execute(f"""SELECT title, description
		FROM netflix
		WHERE LOWER("type") = '{type_movie.lower()}' AND release_year = {year} AND
		(LOWER(listed_in) LIKE '%, {genre.lower()}, %' OR LOWER(listed_in) LIKE '{genre.lower()}, %'
		OR LOWER(listed_in) LIKE '%, {genre.lower()}' OR LOWER(listed_in) LIKE '{genre.lower()}')
		""")
		for el in cursor.fetchall():
			result.append(dict(el))
	return result
