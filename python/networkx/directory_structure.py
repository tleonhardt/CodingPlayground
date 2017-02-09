#!/usr/bin/env python
""" Experiment at using Networkx to store a directory structure and doing either a breath-first
or depth-first traversal.
"""
import os
import sys

import networkx as nx
import matplotlib
matplotlib.rcParams['backend'] = "Qt5Agg"
import matplotlib.pyplot as plt


# Create an empty directed graph
G = nx.DiGraph()

# Set the directory you want to start from
root_dir = '.'
if len(sys.argv) > 1:
    root_dir = sys.argv[1]

root_name = os.path.basename(os.path.realpath(root_dir))

print("Building a directory tree with root directory '{}'".format(root_dir))
print("Root node name is: {}".format(root_name))

# Traverse the directory structure breadth-first or depth-first?
BREADTH_FIRST = False

# Set topdown False to purpposely traverse in a depth-first fashion (not the default)
for root, dirs, files in os.walk(root_dir, topdown=BREADTH_FIRST):
    # print("root = {}".format(root))
    dir_name = os.path.basename(os.path.realpath(root))
    # print("dir_name = {}".format(dir_name))

    for subdir in dirs:
        # Note, adding edges automatically creates the associated nodes if they don't already exist
        G.add_edge(dir_name, subdir)
    for fname in files:
        G.add_edge(dir_name, fname)
        # Get info on file
        path = os.path.join(root, fname)
        file_stats = os.stat(path)
        size = file_stats.st_size # in bytes
        mode = file_stats.st_mode

        # Each node contains a dictionary of attributes where it can store arbitrary data
        G.node[fname]['size'] = size
        G.node[fname]['mode'] = mode

print("Nodes:")
# the data=True also returns the attribute dictionary
for node in G.nodes(data=True):
    print("\t{}".format(node))

print("\nEdges:")
for edge in G.edges():
    print("\t{}".format(edge))

# Breadth-first traversals
print("\nEdges, in a breadth-first fashion:")
bfs_edges = nx.bfs_edges(G, root_name)
for edge in bfs_edges:
    print("\t{}".format(edge))

# Other breadth-first options
# bfs_tree = nx.bfs_tree(G, root_name)
# bfs_successors = nx.bfs_successors(G, root_name)
