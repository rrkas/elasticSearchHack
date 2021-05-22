from flask import *



news = Blueprint('news', __name__)


@news.route('/')
def news_func():


    return render_template('home.html', news=None)
