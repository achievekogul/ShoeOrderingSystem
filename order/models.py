from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    is_open = db.Column(db.Boolean, default=False)
    order_items = db.relationship('OrderItem', backref="orderItem")

    def serialize(self):
        return {
            'user_id': self.user_id,
            'is_open': self.is_open,
            'order_items': [x.serialize() for x in self.order_items]
        }


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    shoe_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self, shoe_id, quantity):
        self.shoe_id = shoe_id
        self.quantity = quantity

    def serialize(self):
        return {
            'shoe': self.shoe_id,
            'quantity': self.quantity
        }
