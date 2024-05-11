import json
from crs.class_work_with_json import SaveJson


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


def check_vacansy_name(vac_list, user_req, true_list):
    """
    проверяет, есть ли искомое значение в выбраном значении словаря
    При совпадении создаёт экземпляр Класса
    Добавляет все экземпляры в список
    :param vac_list:
    :param user_req:
    :param true_list:
    :return:
    """
    for vacancy in vac_list:
        if user_req in vacancy.text:
            true_list.append(vacancy)
    return true_list


def check_vacansy_dis(vac_list, user_req, true_list):
    """
       проверяет, есть ли искомое значение в выбраном значении словаря
       При совпадении создаёт экземпляр Класса
       Добавляет все экземпляры в список
       Проверяет на существование описания.
       В случае отсутствия - пропускает словарь
       :param vac_list:
       :param user_req:
       :param true_list:
       :return:
       """
    for vacancy in vac_list:
        try:
            if user_req in vacancy.requirement:
                true_list.append(vacancy)
        except TypeError:
            pass
    return true_list
