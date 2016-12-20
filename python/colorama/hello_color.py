#!/usr/bin/env python
"""
Example of using the Colorama package for generating cross-platform colored output in Python.
"""
from colorama import init, Fore, Back, Style


# Applications should initialize Colorama using init().  autoreset makes it reset at end of print
init(autoreset=True)

# Generating colored output
print(Fore.RED + 'some red text')
print("automatically back to default color again")
print(Fore.GREEN + 'and with a green background')
print('back to normal now')
print(Fore.BLUE + 'blue')
print(Fore.CYAN + 'cyan')
print(Fore.MAGENTA + 'magenta')
print(Fore.YELLOW + 'yellow')
