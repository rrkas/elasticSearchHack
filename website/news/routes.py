from flask import *
from website.api_calls import *
from website.util import *


news = Blueprint('news', __name__)


@news.route('/')
def news_func():
    api = APINews()
    news = get_news_from_response(api.get_latest_news(
    )) + get_news_from_response(api.get_latest_news(kwd='Corona'))
    news.sort(key=lambda x: x.publishedAt, reverse=True)
    return render_template('home.html', news=news)
