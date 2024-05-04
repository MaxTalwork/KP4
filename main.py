from crs.class_hh import HH
from data.functions import load_products, check_vacansy_name, check_vacansy_dis
from data.functions import is_digit
from crs.class_work_with_json import SaveJson

suit_values = []
hh_url = 'https://api.hh.ru/vacancies'
hh1 = sorted(HH(hh_url).get_information('text'), reverse=True)
save_json = SaveJson(hh1)
load_info = load_products()

user_request = input('Введите ключевые слова для поиска: ')

check_vacansy_name(load_info, user_request, suit_values)
check_vacansy_dis(load_info, user_request, suit_values)


if len(suit_values) == 0:
    print('Нет подходящих вариантов!')
else:
    req_quantity = int(is_digit(input('Сколько результатов вывести? ')))
    for answer in suit_values[:req_quantity]:
        print(answer)
