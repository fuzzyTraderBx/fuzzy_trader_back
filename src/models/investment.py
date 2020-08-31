from sqlalchemy.orm import relationship

from sql_alchemy import database


class InvestmentModel(database.Model):
    """
    Class that represents a investment that can be: criptocurrency or stock
    """
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
        """
        Method that returns a investment on json format
        """
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'is_criptocurrency': self.is_criptocurrency,
        }

    @classmethod
    def find(cls, investment_key):
        """
        Method that find and get the investment at the database
        :param investment_key:
        :return: the investment or None if it doesn't exists
        """
        investment = cls.query.filter_by(name=investment_key).first()
        if investment:
            return investment
        return None

    @classmethod
    def find_by_id(cls, investment_id):
        """
        Method that find and get the investment on the database by id
        :param investment_key:
        :return: the investment or None if it doesn't exists
        """
        investment = cls.query.get(investment_id)
        if investment:
            return investment
        return None

    def save_investment(self):
        """
        Method that save the investment on the database
        """
        database.session.add(self)
        database.session.commit()