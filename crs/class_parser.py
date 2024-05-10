from abc import ABC, abstractmethod


class All(ABC):
    @classmethod
    @abstractmethod
    def get_information(cls, *args, **kwargs):
        return args
