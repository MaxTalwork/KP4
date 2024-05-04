import requests
from crs.class_hh import HH
from data.functions import is_digit

hh_url = 'https://api.hh.ru/vacancies'

user_req = input('Введите запрос: ')
req_quen = int(is_digit(input('Сколько результатов вывести? ')))

hh1 = sorted(HH(hh_url).fet_info(user_req), reverse=True)[:req_quen]
for vac in hh1:
    print(vac)
