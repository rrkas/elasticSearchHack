from .config import Config
from flask import *


def create_app(config=Config):
    app = Flask(__name__)

    app.config.from_object(config)

    from website.news.routes import news
    app.register_blueprint(news)

    return app