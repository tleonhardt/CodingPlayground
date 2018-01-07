from yapsy.IPlugin import IPlugin

class MyPlugin(IPlugin):
    def print_name(self):
        print("This is MyPlugin")
