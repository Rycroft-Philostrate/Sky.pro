from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Модель пользователь"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String(10))
    phone = db.Column(db.String(20))

    @property
    def serialize(self):
        """Метод преобразования данных в словарь"""
        return {
            'user_id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role,
            'phone': self.phone
        }


class Order(db.Model):
    """Модель заказа"""
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    customer = db.relationship(User, foreign_keys=[customer_id])
    executor = db.relationship(User, foreign_keys=[executor_id])

    @property
    def serialize(self):
        """Метод преобразования данных в словарь"""
        return {
            'order_id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'address': self.address,
            'price': self.price,
            'customer_id': self.customer_id,
            'executor_id': self.executor_id
        }


class Offer(db.Model):
    """Модель предложения"""
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    executor = db.relationship(User, foreign_keys=[executor_id])
    order = db.relationship(Order, foreign_keys=[order_id])

    @property
    def serialize(self):
        """Метод преобразования данных в словарь"""
        return {
            'offer_id': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id
        }
