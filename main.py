import requests
from crs.class_hh import HH


# params = {'name': 'Python'}
hh_url = 'https://api.hh.ru/vacancies'
#
# response = requests.get(url='https://api.hh.ru/vacancies', params=params)
# print(response.json()['items'])

hh1 = sorted(HH(hh_url).fet_info('Электрик'), reverse=True)
for vac in hh1:
    print(vac)
