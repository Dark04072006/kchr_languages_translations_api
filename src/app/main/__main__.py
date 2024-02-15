import gunicorn
from flask import Flask

from dishka.integrations.flask import setup_dishka

from app.web.routes import blueprint
from app.main.ioc import DbAdaptersProvider


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.register_blueprint(blueprint)

    setup_dishka(providers=[DbAdaptersProvider()], app=flask_app)

    return flask_app
