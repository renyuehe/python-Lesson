import argparse

parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('param1', type=str,help='姓')
parser.add_argument('param2', type=str,help='名')
args = parser.parse_args()

#打印姓名
print(args.param1+args.param2)