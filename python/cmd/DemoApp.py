#!/usr/bin/env python

import shlex
from cmd import Cmd

class DemoApp(Cmd):
    """Simple command processor example."""

    def do_hello(self, arg):
        self.stdout.write('arg = {}\n'.format(arg))

    def do_say(self, arg):
        """ Say something ...

        Usage:  say [something]
        """
        if arg:
            print("type(arg)={},  arg={}, arg.split()={}".format(type(arg), arg, arg.split()))
            print("shlex.split(arg) = {}".format(shlex.split(arg)))
        else:
            print("No argument provided")

if __name__ == '__main__':
    DemoApp().cmdloop()
