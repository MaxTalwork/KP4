import requests
from crs.class_parser import All
from crs.class_vacancy import Vacancy


class HH(All):
    def __init__(self, url):
        self.url = url

    def fet_info(self, text) -> list[Vacancy]:
        params = {'query': text, 'area': 2, 'per_page': 100}

        response = requests.get(url=self.url, params=params)
        return self.__conv_vac(response.json()['items'])

    def __conv_vac(self, data) -> list[Vacancy]:
        return [
            Vacancy(
                text=items['name'],
                url=items['alternate_url'],
                requirement=items['snippet']['requirement'],
                responsibility=items['snippet']['responsibility'],
                salary=items['salary'])
            for items in data]


    # def __repr__(self):
    #     return f'{self.fet_info('java')}'
