from sqlalchemy.orm import relationship

from sql_alchemy import database


class InvestmentModel(database.Model):
    __tablename__ = 'investments'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    value = database.Column(database.Float(precision=7))
    is_criptocurrency = database.Column(database.Boolean())

    users = relationship("UserModel", secondary="orders")  # TODO: remove cause may not be used

    def __init__(self, name, value, is_criptocurrency):
        self.name = name
        self.value = value
        self.is_criptocurrency = is_criptocurrency

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'is_criptocurrency': self.is_criptocurrency,
        }

    @classmethod
    def find(cls, investment_key):
        investment = cls.query.filter_by(name=investment_key).first()
        if investment:
            return investment
        return None

    @classmethod
    def find_by_id(cls, investment_id):
        investment = cls.query.get(investment_id)
        if investment:
            return investment
        return None

    def save_investment(self):
        database.session.add(self)
        database.session.commit()