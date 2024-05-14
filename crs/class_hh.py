import requests
from crs.class_parser import All


class HH(All):
    """
    класс для получения данных с HH
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'

    def get_information(self, text):
        """
        метод класса для подключения к API
        """
        params = {'text': text, 'area': 1, 'per_page': 100}
        response = requests.get(url=self.__url, params=params)
        return self.__conv_vac(response.json())

    @staticmethod
    def __conv_vac(data):
        """
        Метод для преобразования полученной информации в нужный формат
        """
        data_list = []
        for item in data['items']:
            items = {'text': (item['name']), 'url': (item['alternate_url']),
                     'requirement': (item['snippet']['requirement']),
                     'responsibility': (item['snippet']['responsibility']),
                     'salary': (item.get('salary', {}) or {}).get('from', 0),
                     'currency': (item.get('salary', {}) or {}).get('currency', 'RUR')}
            data_list.append(items)
        return data_list
