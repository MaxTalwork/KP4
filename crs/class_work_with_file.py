from abc import ABC, abstractmethod


class SaveInFile(ABC):

    @abstractmethod
    def __init__(self, data_list):
        self.data_list = data_list
