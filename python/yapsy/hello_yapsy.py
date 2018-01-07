#!/usr/bin/env python
# coding=utf-8
"""
Simple example of using Yapsy to create a basic but fully working plugin management system.

Yapsy’s main purpose is to offer a way to easily design a plugin system in Python, and motivated by the fact that many
other Python plugin system are either too complicated for a basic use or depend on a lot of libraries. Yapsy only
depends on Python’s standard library.

Yapsy basically defines two core classes:
    - a fully functional though very simple PluginManager class
    - an interface IPlugin which defines the interface of plugin instances handled by the PluginManager

Note:
    The plugin_info object (typically an instance of IPlugin) plays as the entry point of each plugin. That’s also where
    Yapsy ceases to guide you: it’s up to you to define what your plugins can do and how you want to talk to them !
    Talking to your plugin will then look very much like the following:
        # Trigger 'some action' from the loaded plugins
        for pluginInfo in simplePluginManager.getAllPlugins():
           pluginInfo.plugin_object.doSomething(...)
"""
import logging

from yapsy.PluginManager import PluginManager

def main():
    # Yapsy uses Python’s standard logging module to record most important events and especially plugin loading failures.
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('yapsy').setLevel(logging.DEBUG)  # Enable DEBUG logging during development

    # Build the manager
    simplePluginManager = PluginManager()

    # Tell it the directories it should look in to find plugins
    simplePluginManager.setPluginPlaces(['plugins'])

    # Tell it the file extension to use for PluginInfo files (INI format)
    simplePluginManager.setPluginInfoExtension('plug')

    # Load all plugins
    simplePluginManager.collectPlugins()

    # Activate all loaded plugins (calls activate method)
    for pluginInfo in simplePluginManager.getAllPlugins():
        # pluginInfo is a plugin_info object, which is typically an instance of IPlugin
        simplePluginManager.activatePluginByName(pluginInfo.name)

    # Loop through the plugins and call a custom method to print their names
    for plugin in simplePluginManager.getAllPlugins():
        plugin.plugin_object.print_name()


if __name__ == '__main__':
    main()
