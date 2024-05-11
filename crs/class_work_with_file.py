from abc import ABC, abstractmethod


class WorkWithFile(ABC):

    @classmethod
    @abstractmethod
    def save_to_json(cls, *args, **kwargs):
        return args, kwargs

    @classmethod
    def load_from_json(cls, *args, **kwargs):
        return args, kwargs

    @classmethod
    def del_from_json(cls, *args, **kwargs):
        return args, kwargs
