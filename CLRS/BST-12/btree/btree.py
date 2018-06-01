class BTreeNode:
  def __init__(self, t, leaf = False):
    self.t = t                        # Minimum degree
    self.keys = [None] * (2 * t - 1)  # An array of keys
    self.children = [None] * (2 * t)  # An array of children
    self.n = 0                        # current number of keys
    self.leaf = leaf                  # Is this a leaf node

  def isFull(self):
    pass

  def search(self, k):
    i = 0
    while i < self.n and k > self.keys[i]:
      i += 1

    if self.keys[i] == k:
      return self

    if self.leaf:
      return None

    return self.children[i].search(k)

  def spiltChild(self, x, i):
    z = BTreeNode(x.t, x.leaf)
    z.n = self.t - 1
    for j in range(self.t - 1):
      z.keys[j] = x.keys[j + self.t]
    if not x.leaf:
      for j in range(self.t):
        z.children[j] = x.children[j + self.t]
    x.n = self.t - 1

    for j in range(self.n, i + 2, -1):
      self.children[j + 1] = self.children[j]

    # self.children[i + 1] = z

    for j in range(self.n-1, i + 1, -1):
      self.keys[j+1] = self.keys[j]
    
    self.keys[i] = x.keys[self.t - 1]

    self.n += 1

  # def spiltChild(self, x, i):
  #   print(x.children[i])
  #   z = BTreeNode(x.t, x.leaf)
  #   y = x.children[i]
  #   z.leaf = y.leaf
  #   z.n = t - 1
  #   for j in range(t - 1):
  #     z.keys[j] = y.keys[j + t]
  #   if not y.leaf:
  #     for j in range(t):
  #       z.children[j] = z.children[j + t]
  #   y.n = t - 1
  #   for j in range(x.n + 1, i + 1, -1):
  #     x.children[j+1] = x.children[j]
  #   x.keys[i] = y.keys[i]
  #   x.n = x.n + 1

  def insertNonFull(self, k):
    i = self.n - 1
    if self.leaf:
      while i >= 0 and self.keys[i] > k:
        self.keys[i + 1] = self.keys[i]
        i -= 1

      self.keys[i+1] = k
      self.n += 1
    else:
      while i >= 0 and self.keys[i] > k:
        i -= 1

      if self.children[i+1].n == 2 * t - 1:
        self.spiltChild(i+1, self.children[i+1])

        if self.keys[i+1] < k:
          i += 1
      self.children[i+1] = self.insertNonFull(k)

class BTree:
  def __init__(self, _t):
    self.t = _t
    self.root = BTreeNode(_t, True)
    

  def insert(self, k):
    r = self.root
    if self.root.n == 2 * self.t - 1:
      s = BTreeNode(self.t, False)
      self.root = s
      s.leaf = False
      s.n = 0
      s.children = r
      s.spiltChild(r, 0)
      i = 0
      if s.keys[0] < k:
        i += 1
      s.children[i].insertNonFull(s, k)
      self.root = s
    else:
      self.root.insertNonFull(k)

  
B = BTree(3)
B.insert(10)
B.insert(20)
B.insert(30)
B.insert(40)
B.insert(50)
B.insert(60)
print(B.root.search(10).keys)