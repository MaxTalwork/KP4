from abc import ABC, abstractmethod


class All(ABC):
    # ����������� ����� ��� ����������� � API
    @classmethod
    @abstractmethod
    def get_information(cls, *args, **kwargs):
        return args
