#!/usr/bin/env python
import cmd

class MyClass(cmd.Cmd):
    """Simple command processor example."""
    def __init__(self):
        # Call super class __init__
        cmd.Cmd.__init__(self)

        # Force cmd to use readline directly instead of input() (PY2) or raw_input() (PY3)
        self.use_rawinput = False

    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]

    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions

    def do_EOF(self, line):
        """ Called when <Ctrl>-d is pressed to exit """
        return True

    def postloop(self):
        """ Called at end just to ensure final newline when exiting """
        print()

if __name__ == '__main__':
    MyClass().cmdloop()
