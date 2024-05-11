from abc import ABC, abstractmethod


class All(ABC):
    # Абстрактный метод для подключения к API
    @classmethod
    @abstractmethod
    def get_information(cls, *args, **kwargs):
        return args
