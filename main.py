import requests
from crs.class_hh import HH
from crs.class_parser import All

params = {'query': 'Python'}
hh_url = 'https://api.hh.ru/vacancies'

response = requests.get(url='https://api.hh.ru/vacancies', params=params)
# print(response.json()['items'])

hh1 = HH(hh_url).fet_info('q')
print(hh1)
