class Node:
  def __init__(self):
    self.data = data
    self.isEndOfString = False
    self.left = None
    self.equal = None
    self.right = None

class TernaryTree:
  def __init__(self):
    self.root = None

  def insert(self, word):
    if self.root is None:
      self.root = Node(word)

    if word 