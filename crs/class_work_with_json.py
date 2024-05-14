import json
from crs.class_work_with_file import WorkWithFile
from crs.class_vacancy import Vacancy


class SaveJson(WorkWithFile):
    """
    Класс для работы с файлом типа json
    """

    def __init__(self):
        self.json_file = 'vacancies.json'

    def save_to_json(self, data_list):
        """
        Метод для записи в файл типа json
        """
        items_list = []
        for data in data_list:
            item = {'text': data['text'],
                    'url': data['url'],
                    'requirement': data['requirement'],
                    'responsibility': data['responsibility'],
                    'salary': data['salary'],
                    'currency': data['currency']}
            items_list.append(item)
            with open(self.json_file, mode='w', encoding='utf-8') as f:
                json.dump(items_list, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        """
        Загружает данные из файла
        """
        with open(self.json_file, mode='r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def get_vacancyes(data):
        """
        Метод для получения списка вакансий из файла json
        """
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

    def del_from_json(self):
        """
        Метод для удаления данных из файла
        """
        open('vacancies.json', 'w').close()

    def __repr__(self):
        return f"{self.get_vacancyes}"
