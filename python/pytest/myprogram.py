#!/usr/bin/env python
# coding=utf-8
"""
Example Python code file for using pytest on.
"""

import sys


def doubleit(x):
    """ Double the value of the input number.

    :param x: int or float - a number
    :return: x * 2
    """
    if not isinstance(x, (int, float)):
        raise TypeError
    var = x * 2
    return var


def doublelines(filename):
    """ Opens a file which is expected to contain integers and calls doubleit() on
    every integer in that file.  Then it writes the double integers back out to
    the same file.

    :param filename: str - filename
    """
    with open(filename) as fh:
        newlist = [str(doubleit(int(val))) for val in fh]
    with open(filename, 'w') as fh:
        fh.write('\n'.join(newlist))

if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled_val = doubleit(input_val)

    print("the value of {0} is {1}".format(input_val, doubled_val))
