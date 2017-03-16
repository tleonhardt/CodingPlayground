#!/usr/bin/env python
# coding=utf-8
"""
Intro to lxml based on The lxml.etree Tutorial at:
http://lxml.de/tutorial.html
"""
from lxml import etree

# ----- The Element class

# An Element is the main container object for the ElementTree API.  Most of the XML tree functionality is accessed
# through this class.  Elements are easily created through the Element factory:
root = etree.Element("root")

# The XML tag name of elements is accessed through the tag property:
print(root.tag)

# Elements are organised in an XML tree structure.  To create child elements and add them to a parent element, you can
# use the append() method:
root.append(etree.Element("child1"))

# However, this is so common that there is a shorter and much more efficient way to do this: the SubElement factory.
# It accepts the same arguments as the Element factory, but additionally requires the parent as first argument:
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

# To see that this is really XML, you can serialize the tree you have created:
print(etree.tostring(root, pretty_print=True))


# ----- Elements are lists
# To make the access to these subelments easy and straight forward, elements mimic the behavior of normal Python lists
# as closely as possible:
child = root[0]
print(child.tag)

print(len(root))

root.index(root[1]) # lxml.etree only!

children = list(root)

for child in root:
    print(child.tag)

root.insert(0, etree.Element("child0"))
start = root[:1]
end = root[-1:]

print(start[0].tag)
print(end[0].tag)

# Test if it's some kind of Element
print(etree.iselement(root))

# Test if it has children
if len(root):
    print("The root element has {} children".format(len(root)))

# There is an important case where the behavior of Elements in lxml deviates from that of lists and from that of the
# original ElementTree:
for child in root:
    print(child.tag)

# This moves the element in lxml.etree! (and overwrites the first element)
root[0] = root[-1]

for child in root:
    print(child.tag)

# In this example,, the last element is moved to a different position, instead of being copied, i.e. it is automatically
# removed from its previous position when it is put in a different place.  In lists, objects can appear in multiple
# positions at the same time, and the above assignment would just copy the item reference into the first position, so
# that both contain the exact same item.

# The upside of the difference is that an Element in lxml.etree always has exactly one parent, which can be queried
# through the getparent() method.  This is not supported in the original ElementTree.
assert root is root[0].getparent()  # lxml.etree only!
assert None is root.getparent()

# If you want to copy an element to a different position in lxml.etree, consider creating an independent deep copy using
# the copy module from Python's standard library.
from copy import deepcopy

element = etree.Element("neu")
element.append(deepcopy(root[1]))
print(element[0].tag)
print([c.tag for c in root])

# The siblings (or neighbours) of an element are accessed as next and previous elements:
assert root[0] is root[1].getprevious() # lxml.etree only!
assert root[1] is root[0].getnext()     # lxml.etree only!


# ----- Elements carray attributes as as dict
# XML elements support attributes.  You can create them directly in the Element factory:
root = etree.Element("root", interesting="totally")
print(etree.tostring(root))

# Attributes are just unordered name-value pairs, so a very convenient way of dealing with them is through the
# dictionary-like interface of Elements:
print(root.get("interesting"))

print(root.get("hello"))

root.set("hello", "Huhu")
print(root.get("hello"))

print(etree.tostring(root))

assert ['hello', 'interesting'] == sorted(root.keys())

for name, value in sorted(root.items()):
    print('{} = {!r}'.format(name, value))

# For the cases where you want to do item lookup or have other reasons for getting a 'real' dictionary-like object,
# e.g. for passing it around, you can use the attrib propery:
attributes = root.attrib
print(attributes["interesting"])
