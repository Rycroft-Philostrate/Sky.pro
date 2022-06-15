# app.py

from flask import Flask
from flask_restx import Api

from models import db
from config import Config
from movie import movie_ns
from director import directors_ns
from genre import genres_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run()
