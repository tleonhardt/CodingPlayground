#!/usr/bin/env python

import shlex
import sys
from cmd2 import Cmd, make_option, options

class DemoApp(Cmd):
    """Simple command processor example."""

    @options([make_option('-n', '--name', action="store", help="your name"),
         ])
    def do_hello(self, arg, opts):
        if opts.name:
            self.stdout.write('Hello {}\n'.format(opts.name))
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

    @options([make_option('-d', '--depth',  type="int", help="output [n] times")],
             arg_desc="[directory]")
    def do_dir(self, path, opts):
        """ Get a directory listing. """
        recursion_depth = 0
        if opts.depth:
            recursion_depth = opts.depth

        self.stdout.write('path = {}\n'.format(path))

if __name__ == '__main__':
    DemoApp().cmdloop()
