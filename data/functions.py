def is_digit(string):
    while string.isdigit() is False:
        string = input(f'Запрос неверный. Введите целое число! ')
    else:
        return string
