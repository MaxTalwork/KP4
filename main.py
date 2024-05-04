from crs.class_hh import HH
from data.functions import load_products, check_vacansy_name, check_vacansy_dis
from data.functions import is_digit
from crs.class_work_with_json import SaveJson


hh_url = 'https://api.hh.ru/vacancies'
hh1 = sorted(HH(hh_url).fet_info('text'), reverse=True)
save_json = SaveJson(hh1)
load_info = load_products()

user_req = input('Введите ключевые слова для поиска: ')
userrl = []

check_vacansy_name(load_info, user_req, userrl)
check_vacansy_dis(load_info, user_req, userrl)

req_quen = int(is_digit(input('Сколько результатов вывести? ')))
for p in userrl[:req_quen]:
    print(p)

