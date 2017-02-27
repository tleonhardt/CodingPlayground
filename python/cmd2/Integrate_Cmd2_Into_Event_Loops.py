#!/usr/bin/env python3
# coding=utf-8
""" Sometimes there is a desire to integrate cmd2 into an external event loop and not have cmd2
control the main loop itself.  This program is an extremely simple bare-bones example for how that
could be done.

It doesn't show how to integrate it with any specfic external event loop since there are a great
many competing options available.

What it does show you is how to get a cmd2 application properly setup to not occupy the main loop
and how to have this external event loop run a cmd2 command.
"""

from cmd2 import Cmd, make_option, options


class CmdLineApp(Cmd):
    """ Example cmd2 application. """

if __name__ == '__main__':
    app = CmdLineApp()

    # Run this before your event loop starts
    app.preloop()


    #----------- Your event loop code starts here ------------------------------------
    # Run whatever event loop code you want here
    # Use onecmd_plus_hooks() to run a single command
    a_command = 'help history'
    stop = app.onecmd_plus_hooks(a_command)

    # NOTE: By default the cmd2.Cmd app will print results to stdout and such.  If some other behavior
    # is desired, you may need to pass values in for either the stdin or stdout keyword args to the initializer.
    #----------- Your event loop code ends here ------------------------------------


    # Run this after your event loop exists
    app.postloop()
