from crs.class_hh import HH
from data.functions import work_with_user
from crs.class_work_with_json import SaveJson

user_input = input('Укажите название вакансии: ')
hh = HH().get_information(user_input)
SaveJson().save_to_json(hh)
vac_list = SaveJson.get_vacancyes(SaveJson().load_from_json())

suit_values = []
user_request = work_with_user(vac_list, suit_values)

if len(suit_values) > 0:
    for option in user_request:
        print(option)
else:
    print(user_request)
