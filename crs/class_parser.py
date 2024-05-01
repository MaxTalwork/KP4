import requests
from abc import ABC, abstractmethod


class All(ABC):
    @abstractmethod
    def __init__(self, url):
        self.url = url

    def fet_info(self, text):
        params = {}
        response = requests.get(url=self.url, params=params)
        return self.__conv_vac(response.json())

    def __conv_vac(self, data):
        pass
