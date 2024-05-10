from abc import ABC, abstractmethod


class WorkWithFile(ABC):

    @classmethod
    @abstractmethod
    def work_with_file(cls, *args, **kwargs):
        return args
