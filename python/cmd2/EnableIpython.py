#!/usr/bin/env python3
# coding=utf-8
"""A sample application for cmd2 as it is completely out of the box.
"""

from cmd2 import Cmd, make_option, options


class CmdLineApp(Cmd):
    """ Example cmd2 application. """

    def __init__(self):
        # Set use_ipython to True to enable the "ipy" command for entering an embedded IPython shell
        Cmd.__init__(self, use_ipython=True)

if __name__ == '__main__':
    c = CmdLineApp()
    c.cmdloop()
