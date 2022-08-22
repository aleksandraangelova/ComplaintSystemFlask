from flask_testing import TestCase

from config import create_app
from db import db


class TestApp(TestCase):

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_required(self):
        url = "/complaint/"
        resp = self.client.get(url)
        self.assert_401(resp)
