from abc import ABC, abstractmethod


class WorkWithFile(ABC):
    # Абстрактный класс для работы с файлами
    @classmethod
    @abstractmethod
    def save_to_json(cls, *args, **kwargs):
        # Метод для записи в файл
        return args, kwargs

    @classmethod
    def load_from_json(cls, *args, **kwargs):
        # Метод для загрузки из файла
        return args, kwargs

    @classmethod
    def del_from_json(cls, *args, **kwargs):
        # Метод для удаления данных из файла
        return args, kwargs
