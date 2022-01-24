from abc import ABC


class Writer(ABC):
    def write(self, filename, data):
        raise NotImplementedError
