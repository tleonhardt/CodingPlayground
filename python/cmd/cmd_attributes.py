#!/usr/bin/env python
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = 'prompt: '
    intro = "Simple command processor example."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

    ruler = '-'

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("type(arg) = {},  arg={}".format(type(person), person))
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
    HelloWorld().cmdloop()
