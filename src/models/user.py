from sqlalchemy.orm import relationship

from sql_alchemy import database


class UserModel(database.Model):
    """
    Class that define a user
    """
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    email = database.Column(database.String(80))
    password = database.Column(database.String(30))

    investments = relationship("InvestmentModel", secondary="orders")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        """
        Method that returns a user on json format
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }

    @classmethod
    def find(cls, email):
        """
        Method that find and get the user
        :param email:
        :return: the user or None if it doesn't exists
        """
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    def save_user(self):
        """
        Method that save the user on the database
        """
        database.session.add(self)
        database.session.commit()


