import sys
import argparse

def add(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)

parser = argparse.ArgumentParser('Simple math calculator')

subparsers = parser.add_subparsers(dest='command', required=True)

parser_add = subparsers.add_parser(name='add', help='sum two numbers')
parser_add.add_argument('x', type=int, help='First number')
parser_add.add_argument('y', type=int, help='Second number')
parser_add.set_defaults(func=add)

parser_sub = subparsers.add_parser(name='sub', help='Substruct two numbers')
parser_sub.add_argument('x', type=int, help='First number')
parser_sub.add_argument('y', type=int, help='Second number')
parser_sub.set_defaults(func=sub)

argv = parser.parse_args()
print(argv)

argv.func(argv.x, argv.y)