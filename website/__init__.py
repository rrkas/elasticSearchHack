from .config import Config
from flask import *


def create_app(config=Config):
    app = Flask(__name__)

    app.config.from_object(config)

    from website.news.routes import news
    from website.slots.routes import slots
    app.register_blueprint(news)
    app.register_blueprint(slots,url_prefix='/slots')

    return app