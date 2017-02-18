#!/usr/bin/env python
"""
This is an example of how to create an embedded IPython shell within a Python terminal application,
but to fall back to using an embedded vanilla Python shell if IPython isn't installed.
"""
use_ipython = True
try:
    from IPython import embed
except ModuleNotFoundError:
    use_ipython = False

def main():
    shell_name = 'Python'
    if use_ipython:
        shell_name = 'IPython'

    banner = 'Entering an embedded {} shell type quit() or <Ctrl>-d to exit ...'.format(shell_name)
    exit_msg = 'Leaving Interpreter, back to program.'

    # You will be able to see x and other local variables within the embedded shell, but any
    # modifications made in the embedded IPython shell won't propagate back to the main program.
    x = 5
    if use_ipython:
        embed(banner1=banner, exit_msg=exit_msg)
    else:
        raise NotImplemented("Basic embedded Python shell (non-IPython) not implemented yet.")

    print('x = {}.  Leaving main program.'.format(x))

if __name__ == '__main__':
    main()
