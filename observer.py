
from abc import ABC, abstractmethod

class Observer():

    @abstractmethod
    def update(self):
        raise NotImplementedError


