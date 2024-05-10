import json
from crs.class_vacancy import Vacancy


def is_digit(string):
    """
    функция для проверки, является ли запрос целым числом
    :param string:
    :return: int
    """
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


def check_vacansy_name(dic_list, user_req, true_list):
    """
    проверяет, есть ли искомое значение в выбраном значении словаря
    При совпадении создаёт экземпляр Класса
    Добавляет все экземпляры в список
    :param dic_list:
    :param user_req:
    :param true_list:
    :return:
    """
    for info in dic_list:
        if user_req in info['text']:
            true_list.append(Vacancy(
                text=info['text'],
                url=info['url'],
                requirement=info['requirement'],
                responsibility=info['responsibility'],
                salary=info['salary'],
                currency=info['currency']
            ))


def check_vacansy_dis(dic_list, user_req, true_list):
    """
       проверяет, есть ли искомое значение в выбраном значении словаря
       При совпадении создаёт экземпляр Класса
       Добавляет все экземпляры в список
       Проверяет на существование описания.
       В случае отсутствия - пропускает словарь
       :param dic_list:
       :param user_req:
       :param true_list:
       :return:
       """
    for info in dic_list:
        try:
            if user_req in info['requirement']:
                true_list.append(Vacancy(
                    text=info['text'],
                    url=info['url'],
                    requirement=info['requirement'],
                    responsibility=info['responsibility'],
                    salary=info['salary'],
                    currency=info['currency']
                ))
        except TypeError:
            pass

