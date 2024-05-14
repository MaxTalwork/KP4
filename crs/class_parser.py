from abc import ABC, abstractmethod


class All(ABC):
    """
    Абстрактный метод для подключения к API
    """

    @abstractmethod
    def get_information(self, text):
        pass
