import mylib

i = mylib.Foo()
print("The first two addresses should be the same, but the third should be different:")
mylib.bar(i)
mylib.bar(i)
mylib.bar(mylib.Foo())
