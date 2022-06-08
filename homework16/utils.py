from models import *
from datetime import datetime


def get_users_all():
    """Получение всех пользователей"""
    return [user.serialize for user in User.query.all()]


def get_user_id(user_id):
    """Получение пользователя по id"""
    user = User.query.get(user_id)
    return user.serialize


def get_orders_all():
    """Получение всех заказов"""
    return [order.serialize for order in Order.query.all()]


def get_order_id(order_id):
    """Получение заказа по id"""
    order = Order.query.get(order_id)
    return order.serialize


def get_offers_all():
    """Получение всех предложений"""
    return [offer.serialize for offer in Offer.query.all()]


def get_offer_id(offer_id):
    """Получение предложения по id"""
    offer = Offer.query.get(offer_id)
    return offer.serialize


def post_user(data):
    """Добавление пользователя в БД"""
    user = User(**data)
    db.session.add(user)
    db.session.commit()


def put_user_id(user_id, data):
    """Изменение данных пользователя с данным id в БД"""
    user = User.query.get(user_id)
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.age = data.get('age')
    user.email = data.get('email')
    user.role = data.get('role')
    user.phone = data.get('phone')
    db.session.add(user)
    db.session.commit()


def delete_user_id(user_id):
    """Удаление пользователя с данным id из БД"""
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()


def post_order(data):
    """Добавление заказа в БД"""
    order = Order(**data)
    order.start_date = datetime.strptime(data.get('start_date'), "%m/%d/%Y")
    order.end_date = datetime.strptime(data.get('end_date'), "%m/%d/%Y")
    db.session.add(order)
    db.session.commit()


def put_order_id(order_id, data):
    """Изменение данных заказа с данным id в БД"""
    order = Order.query.get(order_id)
    order.name = data.get('name')
    order.description = data.get('description')
    order.start_date = datetime.strptime(data.get('start_date'), "%m/%d/%Y")
    order.end_date = datetime.strptime(data.get('end_date'), "%m/%d/%Y")
    order.address = data.get('address')
    order.price = data.get('price')
    order.customer_id = data.get('customer_id')
    order.executor_id = data.get('executor_id')
    db.session.add(order)
    db.session.commit()


def delete_order_id(order_id):
    """Удаление заказа с данным id из БД"""
    order = Order.query.get(order_id)
    db.session.delete(order)
    db.session.commit()


def post_offer(data):
    """Добавление предложения в БД"""
    offer = Offer(**data)
    db.session.add(offer)
    db.session.commit()


def put_offer_id(offer_id, data):
    """Изменение данных предложения с данным id в БД"""
    offer = Offer.query.get(offer_id)
    offer.order_id = data.get('order_id')
    offer.executor_id = data.get('executor_id')
    db.session.add(offer)
    db.session.commit()


def delete_offer_id(offer_id):
    """Удаление предложения с данным id из БД"""
    offer = Offer.query.get(offer_id)
    db.session.delete(offer)
    db.session.commit()
