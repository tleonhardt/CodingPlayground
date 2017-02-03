#!/usr/bin/env python
"""
cmd2 example which illustrates some poor error logging when debug is set to False (the default)
"""
from cmd2 import Cmd

a_dict = {}
a_dict[1] = "blah"

class MyCmd(Cmd):
  def do_printdict(self, line):
    global a_dict
    print("a_dict is {}".format(a_dict))
    print("a_dict[1] = {}".format(a_dict[1]))
    print("a_dict[2] = {}".format(a_dict[2]))

my_cmd = MyCmd()
my_cmd.cmdloop()
