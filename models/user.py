from sqlalchemy.orm import relationship

from sql_alchemy import database


class UserModel(database.Model):
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
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }

    @classmethod
    def find(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    def save_user(self):
        database.session.add(self)
        database.session.commit()


