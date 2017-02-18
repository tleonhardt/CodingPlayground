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
    print('Entering an embedded {} shell type quit() or <Ctrl>-d to exit ...'.format(shell_name))

    if use_ipython:
        embed(header='First time')
    else:
        raise NotImplemented("Basic embedded Python shell (non-IPython) not implemented yet.")

    print('Exited the embedded {} shell.  Goodbye.'.format(shell_name))

if __name__ == '__main__':
    main()
