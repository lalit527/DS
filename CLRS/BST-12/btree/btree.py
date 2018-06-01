class BTreeNode:
  def __int__(self, t, leaf = False):
    self.t = t                        # Minimum degree
    self.keys = [None] * (2 * t - 1)  # An array of keys
    self.children = [None] * (2 * t)  # An array of children
    self.n = 0                        # current number of keys
    self.leaf = leaf                  # Is this a leaf node

  def isFull(self):
    pass

class BTree:
  def __init__(self, _t):
    self.t = _t
    self.root = BTreeNode(_t, True)
    

  def insert(self, k):
    r = self.root
    if self.root.n == 2 * t - 1:
      s = BTreeNode(t, False)
      self.root = s
      s.leaf = False
      s.n = 0
      s.children = r
      s.spiltChild(0)
    else:
      root.insertNonFull(k)
