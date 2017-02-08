#!/usr/bin/env python
"""
A module for tweaking another modules's global parameters via a function it provides.
"""
from A import print_global, set_global


def main():
    # Call a_function with default state
    print_global()

    # Tweak module A's global variable
    print("Module B is now setting A.A_GLOBAL = True")
    set_global(True)

    # Call a_function again
    print_global()


if __name__ == '__main__':
    main()
