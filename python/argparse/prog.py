#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print("type(args) = {},  args={}".format(type(args), args))
print("type(args.integers) = {},  args.integers={}".format(type(args.integers), args.integers))
print("sum = {}".format(args.accumulate(args.integers)))
