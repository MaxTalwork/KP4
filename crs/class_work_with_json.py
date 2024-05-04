import json
from crs.class_work_with_file import SaveInFile


class SaveJson(SaveInFile):
    def __init__(self, data_list):
        self.data_list = data_list

    def save_to_json(self):
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
