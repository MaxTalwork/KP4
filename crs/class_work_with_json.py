import json
from crs.class_work_with_file import WorkWithFile


class SaveJson(WorkWithFile):
    """Класс для записи данных в файлы типа json"""
    def __init__(self, data_list):
        self.data_list = data_list

    def work_with_file(self):
        with open('vacancies.json', mode='w', encoding="utf-8") as f:
            items = []
            for vacancy in self.data_list:
                items.append({
                    'text': vacancy.text,
                    'url': vacancy.url,
                    'requirement': vacancy.requirement,
                    'responsibility': vacancy.responsibility,
                    'salary': vacancy.salary,
                    'currency': vacancy.salary_cor
                })
            json.dump(items, f, indent=4, ensure_ascii=False)

    def __repr__(self):
        return f"{self.data_list}, {self.save_to_json()}"
