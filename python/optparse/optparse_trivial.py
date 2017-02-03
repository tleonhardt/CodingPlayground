#!/usr/bin/env python
from optparse import OptionParser

parser = OptionParser()

_, args = parser.parse_args()
print("type(args) = {},  args = {}".format(type(args), args))
