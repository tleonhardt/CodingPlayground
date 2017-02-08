"""
Example module for importing into another module but allowing it's global variable to be set.
"""

A_GLOBAL = False

def print_global():
    """
    Prints state of the module-level global variable
    """
    print("A_GLOBAL = {}".format(A_GLOBAL))

def set_global(val: bool):
    global A_GLOBAL
    A_GLOBAL = val
