from abc import ABC, abstractmethod


class WorkWithFile(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def save_to_json(self, data_list):
        """
        Метод для записи в файл
        """
        pass

    def load_from_json(self):
        """
        Метод для загрузки из файла
        """
        pass

    def del_from_json(self):
        """
        Метод для удаления данных из файла
        """
        pass
