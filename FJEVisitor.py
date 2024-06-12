from abc import ABC, abstractmethod
from JSONComponent import JSONComponent, JSONContainer, JSONLeaf


class JSONVisitor(ABC):

    def __init__(self, icon : tuple):
        self.icon = icon

    @abstractmethod
    def visitContainer(self, container : JSONContainer, prefix : str = ''):
        pass

    @abstractmethod
    def visitLeaf(self, leaf : JSONLeaf, prefix : str = ''):
        pass

    @abstractmethod
    def visit(self, component : JSONComponent, prefix : str = ''):
        pass


class TreeVisitor(JSONVisitor):

    def __init__(self, icon : tuple):
        super().__init__(icon)

    def visitContainer(self, container: JSONContainer, prefix: str = ''):
        isLast = container.getIsLast()
        connector = '└─' if isLast else '├─'
        print(f'{prefix}{connector}{self.icon[0]}{container.getKey()}')
        prefix = f'{prefix}{'   ' if isLast else '│  '}'
        iterator = container.getIter()
        while iterator.hasNext():
            self.visit(iterator.next(), prefix)

    def visitLeaf(self, leaf: JSONLeaf, prefix: str = ''):
        isLast = leaf.getIsLast()
        connector = '└─' if isLast else '├─'
        toDisplay = f'{prefix}{connector}{self.icon[1]}{leaf.getKey()}'
        if leaf.getVal():
            toDisplay += f' : {leaf.getVal()}'
        print(toDisplay)

    def visit(self, component: JSONComponent, prefix = ''):
        if isinstance(component, JSONContainer):
            self.visitContainer(component, prefix)
        elif isinstance(component, JSONLeaf):
            self.visitLeaf(component, prefix)
        else:
            print('Unexpected node!')


class RectVisitor(JSONVisitor):

    def __init__(self, icon : tuple, totNum : int):
        super().__init__(icon)
        self.totNum = totNum

    def visitContainer(self, container: JSONContainer, prefix: str = ''):
        # 第一行和最后一行特殊处理
        connector = '├─'
        last = '│'
        if container.getLine() == 1:
            connector = '┌─'
            last = '┐'
        elif container.getLine() == self.totNum:
            connector = '┴─'
            last = '┘'
            prefix = '└' + '─' * len(prefix[1:])
        before = f'{prefix}{connector}{self.icon[0]}{container.getKey()} '
        after = '─' * (40 - len(before)) + last
        print(before + after)
        prefix = f'{prefix}│  '
        iterator = container.getIter()
        while iterator.hasNext():
            self.visit(iterator.next(), prefix)

    def visitLeaf(self, leaf: JSONLeaf, prefix: str = ''):
        # 第一行和最后一行特殊处理
        connector = '├─'
        last = '│'
        if leaf.getLine() == 1:
            connector = '┌─'
            last = '┐'
        elif leaf.getLine() == self.totNum:
            connector = '┴─'
            last = '┘'
            prefix = '└' + '─' * len(prefix[1:])
        before = f'{prefix}{connector}{self.icon[1]}{leaf.getKey()} '
        if leaf.getVal():
            before += f': {leaf.getVal()} '
        after = '─' * (40 - len(before)) + last
        print(before + after)

    def visit(self, component: JSONComponent, prefix: str = ''):
        if isinstance(component, JSONContainer):
            self.visitContainer(component, prefix)
        elif isinstance(component, JSONLeaf):
            self.visitLeaf(component, prefix)
        else:
            print('Unexpected node!')
