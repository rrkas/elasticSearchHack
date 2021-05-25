from flask import *
from website.api_calls import *
from website.util import *


news = Blueprint('news', __name__)


@news.route('/', methods=['POST', 'GET'])
def news_func():
    api = APINews()
    news = get_news_from_response(api.get_latest_news())
    news.sort(key=lambda x: x.publishedAt, reverse=True)
    data = request.form.get("data")
    payload = {}
    headers = {}
    url = "http://127.0.0.1:4000/autocomplete?query=" + str(data)
    response = requests.request("GET", url, headers=headers, data=payload)
    autocomplete = response.json()
    return render_template('home.html', news=news, autocomplete=autocomplete)
