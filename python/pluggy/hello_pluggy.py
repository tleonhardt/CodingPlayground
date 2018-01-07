#!/usr/bin/env python
# coding=utf-8
"""Basic example of using the pluggy Python plugin framework."""

import pluggy

hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


class MySpec(object):
    """A hook specification namespace.
    """
    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize.
        """


class Plugin1(object):
    """A hook implementation namespace.
    """
    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2


class Plugin2(object):
    """A 2nd hook implementation namespace.
    """
    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2


# create a manager and add the spec
pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)

# register plugins
pm.register(Plugin1())
pm.register(Plugin2())

# call our `myhook` hook
results = pm.hook.myhook(arg1=1, arg2=2)
print(results)

"""
Results printed:
---------------
inside Plugin_2.myhook()
inside Plugin_1.myhook()
[-1, 3]
"""
