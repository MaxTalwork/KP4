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
        self.salary = salary or 0
        self.salary_cor = currency

    def __lt__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return (f'\nНазвание: {self.text}\nТребования: {self.requirement}\nОбязанности: {self.responsibility}\n'
                f'Ссылка на вакансию: {self.url}\nЗарплата от: {self.salary} {self.salary_cor}')
