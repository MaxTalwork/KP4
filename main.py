from crs.class_hh import HH
from data.functions import work_with_user
from crs.class_work_with_json import SaveJson

user_input = input('Укажите название вакансии: ')
hh = HH().get_information(user_input)

vac_list = SaveJson.get_vacancyes(hh)

suit_values = []
user_request = work_with_user(vac_list, suit_values)


if len(suit_values) > 0:
    for option in user_request:
        print(option)
    save_json = SaveJson().save_to_json(user_request)
else:
    print(user_request)
