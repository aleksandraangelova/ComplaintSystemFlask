from flask import request
from flask_restful import Resource

from db import db
from models.user import ComplainerModel


class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        user = ComplainerModel(**data)
        db.session.add(user)
        db.session.commit()
        return 201
