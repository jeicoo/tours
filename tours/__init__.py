from flask import Flask

from .extensions import db
from .views import ToursAPI


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    app.add_url_rule('/api/v1/tours', view_func=ToursAPI.as_view('tours'))

    return app
