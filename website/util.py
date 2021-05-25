from typing import List

from website.models import *


def get_news_from_response(response: dict) -> List[NewsModel]:
    # print(response.keys())
    # print(response['totalResults'])
    # print(len(response['articles']))
    if response['status'] == 'ok':
        return [NewsModel(i) for i in response['articles']]
