class Node:
  def __init__(self, n):
    self.node = n
    self.edge = [None] * 26

class Edge:
  def __init__(self, e):
    self.label = e
    self.start = None
    self.end = None

class Trie:
  def __init__(self):
    self.root = Node(0)
    self.label = 0

  def insert_patterns(self, patterns):
    for pattern in patterns:
      self.insert_pattern(pattern)
      

  def get_index(self, c):
    return ord(c) - ord('A')

  def insert_pattern(self, pattern):
    current = self.root
    for c in pattern:
      symbol = self.get_index(c)
      if current.edge and current.edge[symbol]:
        current = current.edge[symbol].end
      else:
        edge = Edge(c)
        current.edge[symbol] = edge
        edge.start = current
        n = self.label
        node = Node(n + 1)
        self.label += 1
        edge.end = node
        current = current.edge[symbol].end
  
  def show(self, current=None):
    if current is None:
      current = self.root
    print(current.node)
    for e in current.edge:
      if e is not None:
        print(e.label)
        self.show(e.end)


T = Trie()
patterns = ["ATAGA", "ATC", "GAT"]
T.insert_patterns(patterns)
T.show()