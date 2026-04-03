from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass
