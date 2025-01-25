import sys
import argparse

def add(x, y):
    return x + y


def sub(x, y):
    return x - y

parser = argparse.ArgumentParser('Simple math calculator')

parser.add_argument('--operation', choices=['add', 'sub'], required=True, help='Operation')
parser.add_argument('x', type=int, help='First number')
parser.add_argument('y', type=int, help='Second number')

args = parser.parse_args()
print(args)

commands = {"add": add, "sub": sub}

print(sys.argv)
print(commands[args.operation](args.x, args.y))
