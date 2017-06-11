#!/usr/bin/env python
# coding=utf-8
"""
Simple example to demonstrate optional type hinting, MyPy, and PyCharm Introspection.
"""


def greeting(name: str) -> str:
    """Greet someone."""
    return 'Hello ' + name


if __name__ == '__main__':
    greeting('Todd')
    greeting(1)
