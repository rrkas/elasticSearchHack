from typing import List

from website.models import *


def get_news_from_response(response: dict) -> List[NewsModel]:
    # print(response.keys())
    # print(response['totalResults'])
    # print(len(response['articles']))
    if response['status'] == 'ok':
        return [NewsModel(i) for i in response['articles']]


def news_post_es(data):
    for result in data['articles']:
        news_post_url = "http://localhost:9200/news/_doc"
        news_data = {
            "source": {
                "id": result['source']['id'],
                "name": result['source']['name']
            },
            "author": result['author'],
            "title": result['title'],
            "description": result['description'],
            "url": result['url'],
            "urlToImage": result['urlToImage'],
            "publishedAt": result['publishedAt'],
            "content": result['content']
        }

        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        }
        news_data = json.dumps(news_data)
        response = requests.request(
            "POST", news_post_url, data=news_data, headers=headers)

        if(response.status_code == 201):
            print("Values Posted in news index")
