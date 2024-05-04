import json
from crs.class_vacancy import Vacancy


def is_digit(string):
    while string.isdigit() is False:
        string = input(f'Запрос неверный. Введите целое число! ')
    else:
        return string


def load_products():  # pragma: no cover
    """
    Загружает данные из файла
    """
    with open('vacancies.json', mode='r', encoding='utf-8') as f:
        return json.load(f)

def check_vacansy_name(load_info, user_req, userrl):
    for info in load_info:
        if user_req in info['text']:
            userrl.append(Vacancy(
                text=info['text'],
                url=info['url'],
                requirement=info['requirement'],
                responsibility=info['responsibility'],
                salary=info['salary'],
                currency=info['currency']
            ))


def check_vacansy_dis(load_info, user_req, userrl):
    try:
        for info in load_info:
            if user_req in info['requirement']:
                userrl.append(Vacancy(
                    text=info['text'],
                    url=info['url'],
                    requirement=info['requirement'],
                    responsibility=info['responsibility'],
                    salary=info['salary'],
                    currency=info['currency']
                ))
    except TypeError:
        pass
