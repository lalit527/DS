class Node:
  def __init__(self, next, start, end):
    self.next = next
    self.start = start
    self.end = end

class SuffixTree:
  def __init__(self):
    self.root = None
    self.edges = {}

  def build_tree(self, text):
    for j in range(len(text)):
      current = self.root

      k = j
      while True:
        symbol = text[k]
        