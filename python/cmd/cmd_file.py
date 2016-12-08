#!/usr/bin/env python
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    # Disable rawinput module use
    use_rawinput = False

    # Do not show a prompt after each command read
    prompt = ''

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
    input = open(sys.argv[1], 'rt')
    try:
        HelloWorld(stdin=input).cmdloop()
    finally:
        input.close()
