#!/usr/bin/env python3
# coding=utf-8
"""A sample application for cmd2 that explores a GNU Readline bug related to ANSI color escape codes.
"""
import colorama
from colorama import Fore

from cmd2 import Cmd, make_option, options


class CmdLineApp(Cmd):
    """ Example cmd2 application. """
    def __init__(self):
        # Set use_ipython to True to enable the "ipy" command for entering an embedded IPython shell
        Cmd.__init__(self)
        self.prompt = '(cmd2) ' + Fore.CYAN + '1' + Fore.RESET + '> '

if __name__ == '__main__':
    colorama.init(autoreset=True)

    c = CmdLineApp()
    c.cmdloop()
