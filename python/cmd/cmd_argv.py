#!/usr/bin/env python
import cmd

class InteractiveOrCommandLine(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi, {}".format(person))
        else:
            print('hi')

    def do_EOF(self, line):
        """ Called when <Ctrl>-d is pressed to exit """
        return True

    def postloop(self):
        """ Called at end just to ensure final newline when exiting """
        print()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()
