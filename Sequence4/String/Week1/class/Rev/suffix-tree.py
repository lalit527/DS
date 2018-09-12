from collections import OrderedDict

class Node:
  def __init__(self, n):
    self.node = n
    self.edge = {}

class Edge:
  def __init__(self, e):
    self.label = e
    self.start = None
    self.end = None

class SuffixTree:
  def __init__(self):
    self.root = Node(0)
    self.label = 0

  def insert(self, pattern):
    n = len(pattern)
    for i in range(n -1, -1, -1):
      current = self.root
      j = i
      while j < n:
        if pattern[j] in current.edge:
          _next = current.edge[text[j]]
          label = _next.label
          k = j + 1
