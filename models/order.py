from flask import jsonify
from sqlalchemy.orm import relationship, backref

from models.investment import InvestmentModel
from models.user import UserModel
from sql_alchemy import database


class Order(database.Model):
    __tablename__ = 'orders'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    investment_id = database.Column(database.Integer, database.ForeignKey('investments.id'))

    user = relationship(UserModel, backref=backref("orders", cascade="all, delete-orphan"))
    product = relationship(InvestmentModel, backref=backref("orders", cascade="all, delete-orphan"))

    def __init__(self, user_id, investment_id):
        self.user_id = user_id
        self.investment_id = investment_id

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'investment_id': self.investment_id,
        }

    @classmethod
    def find(cls, user_id):
        orders = cls.query.filter_by(user_id=user_id)
        if orders:
            # json_list = [i.json for i in orders.all()]
            json_list = orders.all()
            return json_list
        return None

    def save_order(self):
        database.session.add(self)
        database.session.commit()


