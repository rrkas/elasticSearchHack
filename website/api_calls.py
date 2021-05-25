import requests
from datetime import datetime
import json
from fake_useragent import UserAgent

class APISetu:
    
    def check_availibility_pincode(self, pincode: str , date :str):
        User_agent = UserAgent()
        browser_header = {'User-Agent': User_agent.random}
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode,date)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            return response.json() 
        else:
            return response.status_code                       

    def check_availibility_district(self, district_id:str ,date : str):
        User_agent = UserAgent()
        browser_header = {'User-Agent': User_agent.random}
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id,date)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            return response.json() 
        else:
            return response.status_code  
         
'''
    def get_states(self):
        User_agent = UserAgent()
        browser_header = {'User-Agent': User_agent.random}
        URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            return response.json() 
        else:
            return response.status_code 
    def get_districts(self):
        User_agent = UserAgent()
        browser_header = {'User-Agent': User_agent.random}
        URL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_id,date)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            return response.json() 
        else:
            return response.status_code 
'''           



        


class APINews:
    DOCS = 'https://newsapi.org/docs/get-started#search'
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
