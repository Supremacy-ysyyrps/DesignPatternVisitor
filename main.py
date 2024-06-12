from Builder import JSONBuilder, Director
from FJEVisitor import TreeVisitor, RectVisitor
from config import icons
import argparse
import json


class Demo:

    def __init__(self, args):
        self.args = args
        self.director = Director(JSONBuilder())

    def demo(self, data):
        components = self.director.construct(data)
        if args['style'] == 'tree':
            self.visitor = TreeVisitor(icons[args['icon_family']])
        elif args['style'] == 'rect':
            self.visitor = RectVisitor(icons[args['icon_family']], components.totLine)
        iterator = components.root.getIter()
        while iterator.hasNext():
            iterator.next().accept(self.visitor)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='命令行参数')

    parser.add_argument('-f',
                        '--file',
                        type = str,
                        default = 'test.json',
                        help = '选择 json 文件')

    parser.add_argument('-s',
                        '--style',
                        type = str,
                        choices = ['tree', 'rect'],
                        default = 'tree',
                        help = '选择风格')

    parser.add_argument('-i',
                        '--icon_family',
                        type = str,
                        choices = ['default', 'fruit', 'animal', 'sports'],
                        default = 'default',
                        help = '选择图标族')

    args = vars(parser.parse_args())

    with open(args['file'], 'r') as f:
        json_string = f.read()

    data = json.loads(json_string)

    demo = Demo(args)
    demo.demo(data)
