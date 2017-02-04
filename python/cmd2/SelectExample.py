#!/usr/bin/env python3
# coding=utf-8
"""A sample application for cmd2 to test the select feature.
"""

from cmd2 import Cmd, make_option, options


class CmdLineApp(Cmd):
    """ Example cmd2 application. """

    def do_eat(self, arg):
        sauce = self.select('sweet salty', 'Sauce? ')
        result = '{food} with {sauce} sauce, yum!'
        result = result.format(food=arg, sauce=sauce)
        self.stdout.write(result + '\n')

if __name__ == '__main__':
    c = CmdLineApp()
    c.cmdloop()
