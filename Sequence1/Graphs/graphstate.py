from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2

class Node:
    def __init__(self, data):
        self.data = data
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()

class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, data):
        node = Node(data)
        self.nodes[data] = node
        return node

    def add_edge(self, source, dest, weight = 0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight

g = Graph()
g.add_edge(0, 1, 5)

print(g.nodes)
