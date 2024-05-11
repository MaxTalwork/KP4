from crs.class_hh import HH
from data.functions import check_vacansy_name, check_vacansy_dis
from data.functions import is_digit
from crs.class_work_with_json import SaveJson

user_request = input('Введите ключевые слова для поиска: ')
suit_values = []
hh = HH().get_information(user_request)

save_json = SaveJson().save_to_json(hh)
load_info = SaveJson().load_from_json()
vac_list = SaveJson.get_vacancyes(load_info)
check_vacansy_name(vac_list, user_request, suit_values)
check_vacansy_dis(vac_list, user_request, suit_values)

if len(suit_values) == 0:
    print('По вашему запросу не найдено подходящих вариантов!')
else:
    print(f'Найдено {len(suit_values)} подходящих результатов')
    req_quantity = int(is_digit(input('Сколько результатов вывести? ')))
    for answer in sorted(suit_values[:req_quantity], reverse=True):
        print(answer)
