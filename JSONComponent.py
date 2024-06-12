from abc import ABC, abstractmethod
from Iterator import JSONIterator

class JSONComponent(ABC):

    def __init__(self, key : str, line : int):
        self.key = key
        self.line = line            # 节点应该显示在第几行
        self.isLast : bool = True   # 是否是父节点的最后一个子节点

    def getKey(self) -> str:
        return self.key

    def getLine(self) -> int:
        return self.line

    def getIsLast(self) -> bool:
        return self.isLast

    def setIsLast(self, isLast : bool):
        self.isLast = isLast

    @abstractmethod
    def getVal(self):
        pass

    @abstractmethod
    def accept(self, jsonVisitor):
        pass


class JSONContainer(JSONComponent):

    def __init__(self, key : str, line : int):
        super().__init__(key, line)
        self.val : list[JSONComponent] = []

    def getVal(self):
        return self.val

    def accept(self, jsonVisitor):
        jsonVisitor.visit(self)

    def add(self, component : JSONComponent):
        if len(self.val) > 0:
            self.val[-1].setIsLast(False)
        self.val.append(component)

    def getIter(self) -> JSONIterator:
        return JSONIterator(self.val)


class JSONLeaf(JSONComponent):

    def __init__(self, key : str, line : int, val):
        super().__init__(key, line)
        self.val = val

    def getVal(self):
        return self.val

    def accept(self, jsonVisitor):
        jsonVisitor.visit(self)
