from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
api = Api(app)
migrate = Migrate(app, db)

db.init_app(app)


@app.after_request
def return_response(resp):
    db.session.commit()
    return resp


[api.add_resource(*route_data) for route_data in routes]

if __name__ == "__main__":
    app.run()