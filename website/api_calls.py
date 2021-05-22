import requests


class APISetu:
    @staticmethod
    def generateOTP(number: str):
        url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
        response = requests.post(url)
        return response

    @staticmethod
    def states():
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        response = requests.get(url)
        return response
