from datetime import datetime
import time


class NewsModel:
    def __init__(self, data: dict):
        self.data = data
        self.sourceId = data['source']['id']
        self.sourceName = data['source']['id']
        self.author = data['author']
        self.title = data['title']
        self.desc = data['description']
        self.url = data['url']
        self.urlToImage = data['urlToImage']
        self.publishedAt = datetime_from_utc_to_local(data['publishedAt'])
        self.content = str(data['content'])
        # print(self.content[-10:])

    def __repr__(self):
        return str(self.data)


def datetime_from_utc_to_local(utc_datetime):
    utc_datetime = datetime.strptime(utc_datetime, '%Y-%m-%dT%H:%M:%SZ')
    epoch = time.mktime(utc_datetime.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc_datetime + offset
