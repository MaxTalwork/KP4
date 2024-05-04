import requests
from crs.class_parser import All
from crs.class_vacancy import Vacancy


class HH(All):

    def __init__(self, url):
        self.url = url

    def get_information(self, text):
        params = {'query': text, 'area': 2, 'per_page': 100}
        response = requests.get(url=self.url, params=params)
        return self.__conv_vac(response.json())

    def __conv_vac(self, data) -> list[Vacancy]:
        return [
            Vacancy(
                text=item['name'],
                url=item['alternate_url'],
                requirement=item['snippet']['requirement'],
                responsibility=item['snippet']['responsibility'],
                salary=(item.get('salary', {}) or {}).get('from', 0),
                currency=(item.get('salary', {}) or {}).get('currency', 'RUB'))
            for item in data['items']]

    # def __repr__(self):
    #     return f'{self.fet_info('java')}'
