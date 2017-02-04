#!/usr/bin/env python3
# coding=utf-8
"""A sample application for cmd2 as it is completely out of the box.
"""

from cmd2 import Cmd, make_option, options


class CmdLineApp(Cmd):
    """ Example cmd2 application. """

if __name__ == '__main__':
    c = CmdLineApp()
    c.cmdloop()
