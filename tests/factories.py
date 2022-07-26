import factory
from random import randint

from db import db

from models import ComplainerModel, UserRole


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class ComplainerFactory(BaseFactory):
    class Meta:
        model = ComplainerModel
    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    password = factory.Faker("password")
    iban = factory.Faker("iban")
    role = UserRole.complainer
