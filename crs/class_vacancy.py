class Vacancy:
    def __init__(self, text, url, requirement, responsibility, salary):
        self.text = text
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        if salary is None:
            self.salary, self.salary_cor = 'Не указано', ''
        else:
            try:
                if salary['from'] is None:
                    self.salary = 0
                else:
                    self.salary = salary['from']
            except TypeError:
                self.salary = 0
            try:
                self.salary_cor = salary['currency']
            except TypeError:
                self.salary_cor = ''

    def __str__(self):
        return (f'Название: {self.text}\nТребования: {self.requirement}\nОбязанности: {self.responsibility}\n'
                f'Ссылка на вакансию: {self.url}\nЗарплата от: {self.salary} {self.salary_cor}\n')
