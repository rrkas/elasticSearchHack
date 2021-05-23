import requests
from datetime import datetime


class APISetu:
    BASE_URL = 'https://cdn-api.co-vin.in/api'

    def __init__(self):
        self.txnId = None

    def generate_otp(self, number: str):
        url = f"{APISetu.BASE_URL}/v2/auth/public/generateOTP"
        data = {
            "mobile": number,
        }
        try:
            response = requests.post(url=url, data=data)
            print(response)
            print('--------------------------------------')
            print(response.url)
            print('--------------------------------------')
            print(response.text)
            print('--------------------------------------')
            print(response.content)
            print('--------------------------------------')
            print(response.request.headers)
            print('--------------------------------------')
            if response.status_code == 200:
                print(response.json())
            # if response.status_code == 200:
            #     self.txnId = response.json()['txnId']
        except Exception as e:
            print('GENERATE_OTP_ERROR', e.args)

    def confirm_otp(self, otp: str):
        url = f"{APISetu.BASE_URL}/v2/auth/public/confirmOTP"
        if not self.response:
            return
        json = self.response.json()
        data = {
            "otp": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
            "txnId": json['txnId'],
        }
        try:
            self.response = requests.post(url=url, data=data)
        except Exception as e:
            print('GENERATE_OTP_ERROR', e.args)

    def states(self):
        url = f"{APISetu.BASE_URL}/v2/admin/location/states"
        try:
            self.response = requests.get(url)
        except Exception as e:
            print('STATES_ERROR', e.args)


class APINews:
    API_KEY = '42a3934049bc45f0836ba9cf11e19870'

    def get_latest_news(self, date: datetime = datetime.now(), kwd='Covid', country='in'):
        url = (
            'https://newsapi.org/v2/top-headlines?'
            f'country={country}&'
            f'q={kwd}&'
            f'from={date.year}-{date.month}-{date.day}&'
            'sortBy=popularity&'
            f'apiKey={APINews.API_KEY}'
        )

        response = requests.get(url)
        return response.json()
