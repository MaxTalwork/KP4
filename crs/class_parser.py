from abc import ABC, abstractmethod


class All(ABC):
    @abstractmethod
    def __init__(self, url):
        self.url = url
