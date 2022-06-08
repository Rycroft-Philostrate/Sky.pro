from flask import Flask, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from utils import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/users', methods=['GET', 'POST'])
def users_all():
    """Представление всех пользователей в JSON формате и добавление нового пользователя"""
    if request.method == 'POST':
        if request.is_json:
            try:
                post_user(request.json)
                return 'Данные успешно записаны!'
            except SQLAlchemyError:
                db.session.rollback()
                return 'Ошибка записи в БД!'
        else:
            return 'Не JSON формат!'
    return jsonify(get_users_all())


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def users_id(user_id):
    """Представление пользователя в JSON формате, обновление
    данных пользователя и удаления пользователя с данным id"""
    if request.method == 'PUT':
        if request.is_json:
            try:
                put_user_id(user_id, request.json)
                return 'Данные успешно обновлены в БД'
            except SQLAlchemyError:
                db.session.rollback()
                return 'Ошибка обновления записи в БД!'
        else:
            return 'Не JSON формат!'
    elif request.method == 'DELETE':
        try:
            delete_user_id(user_id)
            return 'Данные успешно удалены из БД!'
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка удаления данных из БД!'
    return jsonify(get_user_id(user_id))


@app.route('/orders', methods=['GET', 'POST'])
def orders_all():
    """Представление всех заказов в JSON формате и добавление нового заказа"""
    if request.method == 'POST':
        if request.is_json:
            try:
                post_order(request.json)
                return 'Данные успешно записаны!'
            except SQLAlchemyError:
                db.session.rollback()
                return 'Ошибка записи в БД!'
        else:
            return 'Не JSON формат!'
    return jsonify(get_orders_all())


@app.route('/orders/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def orders_id(order_id):
    """Представление заказа в JSON формате, обновление
    данных заказа и удаления заказа с данным id"""
    if request.method == 'PUT':
        if request.is_json:
            try:
                put_order_id(order_id, request.json)
                return 'Данные успешно обновлены в БД'
            except SQLAlchemyError:
                db.session.rollback()
                return 'Ошибка обновления записи в БД!'
        else:
            return 'Не JSON формат!'
    elif request.method == 'DELETE':
        try:
            delete_order_id(order_id)
            return 'Данные успешно удалены из БД!'
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка удаления данных из БД!'
    return jsonify(get_order_id(order_id))


@app.route('/offers', methods=['GET', 'POST'])
def offers_all():
    """Представление всех предложений в JSON формате и добавление нового предложения"""
    if request.method == 'POST':
        if request.is_json:
            try:
                post_offer(request.json)
                return 'Данные успешно записаны!'
            except SQLAlchemyError:
                db.session.rollback()
                return 'Ошибка записи в БД!'
        else:
            return 'Не JSON формат!'
    return jsonify(get_offers_all())


@app.route('/offers/<int:offer_id>', methods=['GET', 'PUT', 'DELETE'])
def offers_id(offer_id):
    """Представление предложения в JSON формате, обновление
    данных предложения и удаления предложения с данным id"""
    if request.method == 'PUT':
        if request.is_json:
            try:
                put_offer_id(offer_id, request.json)
                return 'Данные успешно обновлены в БД'
            except SQLAlchemyError:
                db.session.rollback()
                return 'Ошибка обновления записи в БД!'
        else:
            return 'Не JSON формат!'
    elif request.method == 'DELETE':
        try:
            delete_offer_id(offer_id)
            return 'Данные успешно удалены из БД!'
        except SQLAlchemyError:
            db.session.rollback()
            return 'Ошибка удаления данных из БД!'
    return jsonify(get_offer_id(offer_id))


if __name__ == '__main__':
    app.run()
