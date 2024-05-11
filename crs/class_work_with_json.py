import json
from crs.class_work_with_file import WorkWithFile
from crs.class_vacancy import Vacancy


class SaveJson(WorkWithFile):
    """Класс для записи данных в файлы типа json"""

    def __init__(self):
        pass

    def save_to_json(self, data_list):
        with open('vacancies.json', mode='w', encoding='utf-8') as f:
            json.dump(data_list, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        """
        Загружает данные из файла
        """
        with open('vacancies.json', mode='r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def get_vacancyes(data):
        vac_list = []
        for info in data:
            vac_list.append(Vacancy(
                text=info.get('text'),
                url=info.get('url'),
                requirement=info.get('requirement'),
                responsibility=info.get('responsibility'),
                salary=info.get('salary'),
                currency=info.get('currency')
            ))
        return vac_list

    def __repr__(self):
        return f"{self.get_vacancyes}"
