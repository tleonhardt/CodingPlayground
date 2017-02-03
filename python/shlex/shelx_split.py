#!/usr/bin/env python
"""
Example of using the shlex module to split a string by spaces, but preserver quoted substrings.
"""
import shlex

orig_string = 'this is "a test"'
shlex_split = shlex.split('this is "a test"')
print("original string = '{}'".format(orig_string))
print("shlex.split(original) = {}".format(shlex_split))
