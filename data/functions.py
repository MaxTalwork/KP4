import json
from crs.class_work_with_json import SaveJson


def work_with_user(data_list, suit_values):
    answers = []
    user_request = input('Введите ключевые слова для поиска: ')
    check_vacansy_name(data_list, user_request, suit_values)
    check_vacansy_dis(data_list, user_request, suit_values)
    if len(suit_values) == 0:
        return f'По вашему запросу не найдено подходящих вариантов!'
    else:
        print(f'Найдено {len(suit_values)} подходящих результатов')
        req_quantity = int(is_digit(input('Сколько результатов вывести? ')))
        return sorted(suit_values[:req_quantity], reverse=True)


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
