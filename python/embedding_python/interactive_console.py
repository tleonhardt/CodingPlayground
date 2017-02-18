#!/usr/bin/env python
"""
This is an example of how to start an interactive Python console within a Python terminal application.
"""
from code import InteractiveConsole
import sys

def main():
    x = 5
    print('Entering an interactive Python shell ...')

    interp = InteractiveConsole(locals=locals())
    interp.runcode('import sys, os;sys.path.insert(0, os.getcwd())')

    interp.runcode('x = 7')
    print('x = {}'.format(x))

    cprt = 'Type "help", "copyright", "credits" or "license" for more information.'

    try:
        interp.interact(banner="Python %s on %s\n%s\n" % (sys.version, sys.platform, cprt))
    except SystemExit:
        print("Exited InteractiveConsole")

    print('x = {}.  Leaving main program.'.format(x))

if __name__ == '__main__':
    main()
