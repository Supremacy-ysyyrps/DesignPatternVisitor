from abc import ABC, abstractmethod
from JSONComponent import JSONComponent, JSONContainer, JSONLeaf


class JSONProduct:

    def __init__(self, root : JSONContainer, totLine : int):
        self.root = root        # 树的根节点
        self.totLine = totLine  # 渲染时输出的总行数


class Builder(ABC):

    @abstractmethod
    def buildPart(self, key : str, val) -> JSONComponent:
        pass

    @abstractmethod
    def build(self, data) -> JSONProduct:
        pass


class JSONBuilder(Builder):

    def __init__(self):
        self.num : int = -1    # 当前已经构建的节点数

    def buildPart(self, key : str, val) -> JSONComponent:
        self.num += 1
        composite = JSONContainer(key, self.num)
        if isinstance(val, dict):
            for k, v in val.items():
                composite.add(self.buildPart(k, v))
        elif isinstance(val, list):
            for i, v in enumerate(val):
                composite.add(self.buildPart(f'{i}', v))
        else:
            composite = JSONLeaf(key, self.num, val)
        return composite

    def build(self, data) -> JSONProduct:
        self.product = JSONProduct(self.buildPart("root", data), self.num)
        return self.product


class Director:

    def __init__(self, builder : Builder):
        self.builder = builder

    def construct(self, data) -> JSONProduct:
        return self.builder.build(data)
