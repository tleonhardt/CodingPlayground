#!/usr/bin/env python
"""
This is an example of how to start a full normal IPython shell (as opposed to an embedded IPython
shell) within a Python terminal application.
"""
from IPython import start_ipython

def main():
    x = 5
    print('Entering a full IPython shell ...')

    # Set argv to empty list to prevent parsing command-line args.
    start_ipython(argv=[], user_ns=locals())

    print('x = {}.  Leaving main program.'.format(x))

if __name__ == '__main__':
    main()
