#!/usr/bin/env python
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print("type(options) = {},  options = {}".format(type(options), options))
print("type(args) = {},  args = {}".format(type(args), args))
