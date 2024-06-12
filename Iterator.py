from abc import ABC, abstractmethod


class Iterator(ABC):

    def __init__(self):
        self.curIdx : int = 0

    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass



class JSONIterator(Iterator):

    def __init__(self, components : list):
        super().__init__()
        self.components = components

    def hasNext(self) -> bool:
        return self.curIdx < len(self.components)

    def next(self):
        if self.hasNext():
            self.curIdx += 1
            return self.components[self.curIdx - 1]
        return None
