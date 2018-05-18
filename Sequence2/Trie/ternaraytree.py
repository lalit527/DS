class Node:
  def __init__(self, data):
    self.data = data
    self.isEndOfString = False
    self.equal = self.left = self.right = None

class TernaryTree:
  def __init__(self):
    self.root = None

  def insert(self, word):
    return self._insert(self.root, word)

  def _insert(self, root, word):
    print(word)
    if self.root is None:
      self.root = Node(word[:1])

    if root is None:
      print("here", 1)
      root = Node(word[:1])
    
    if word[:1] < root.data:
      print("here", 2)
      self._insert(root.left, word)
    
    elif word[:1] > root.data:
      self._insert(root.right, word)
    
    else:
      if word[:1] > root.data:
        insert(root.equal, word[1:])
      else:
        root.isEndOfString = True

  def showTree(self):
    root = self.root
    print(self.root)
    if root is not None:
      print(root.data)
      root = root.right


t = TernaryTree()
t.insert("the")
t.insert("brown")
t.showTree()


