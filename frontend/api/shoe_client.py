import requests

from . import SHOE_API_URL


class ShoeClient:
    @staticmethod
    def get_shoes():
        response = requests.get(SHOE_API_URL + '/api/shoe/all')
        return response.json()

    @staticmethod
    def get_shoe(slug):
        response = requests.get(SHOE_API_URL + '/api/shoe/' + slug)
        return response.json()
