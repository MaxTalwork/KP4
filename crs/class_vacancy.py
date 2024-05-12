class Vacancy:
    """
    Класс Вакансий.
    Создаёт экземпляры.
    Сортирует
    Выводит в нужном формате
    """

    def __init__(self, text, url, requirement, responsibility, salary, currency):
        self.text = text
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary = salary
        self.salary_cor = currency

    @property
    def salary(self):
        """
        Проверка корректности введёной зарплаты
        """
        return self._salary

    @salary.setter
    def salary(self, value):
        if value is None:
            value = 0
        self._salary = value

    def __lt__(self, other):
        return self._salary < other._salary
    """
    Функция сортировки для Класса Вакансий.
    """

    def __str__(self):
        if self._salary != 0:
            return (f'\nНазвание: {self.text}\nТребования: {self.requirement}\nОбязанности: {self.responsibility}\n'
                    f'Ссылка на вакансию: {self.url}\nЗарплата от: {self._salary} {self.salary_cor}')
        else:
            return (f'\nНазвание: {self.text}\nТребования: {self.requirement}\nОбязанности: {self.responsibility}\n'
                    f'Ссылка на вакансию: {self.url}\nМинимальная зарплата не указана!')
