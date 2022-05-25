from flask import Flask, jsonify
from utils import *

app = Flask(__name__)


@app.route('/movie/<title>')
def movie_title(title):
	"""Представление найденных фильмов по названию"""
	return jsonify(find_movie_name(title))


@app.route('/movie/<int:year_1>/to/<int:year_2>')
def movie_year(year_1, year_2):
	"""Представление найденных фильмов по диапазону годов релиза"""
	return jsonify(find_movie_year(year_1, year_2))


@app.route('/rating/<rating>')
def movie_rating(rating):
	"""Предстваление найденных фильмов по рейтингу"""
	return jsonify(find_rating(rating))


@app.route('/genre/<genre>')
def movie_genre(genre):
	"""Представление найденных фильмов по жанру"""
	return jsonify(find_genre(genre))


if __name__ == '__main__':
	app.run()
