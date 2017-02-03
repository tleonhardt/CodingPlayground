#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('bar', nargs='+', help='bar help')
args = parser.parse_args()

print("type(args) = {},  args={}".format(type(args), args))
