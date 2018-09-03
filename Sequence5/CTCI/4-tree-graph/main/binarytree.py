from collections import deque

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None
  
class BinaryTree:
  def __init__(self):
    self.root = None

  def insertLeft(self, data, parent=None):
    node = Node(data)
    if parent is not None:
      parent.left = node
      node.parent = parent
    elif parent is None and self.root is None:
      self.root = node
    return node

  def insertRight(self, data, parent=None):
    node = Node(data)
    if parent is not None:
      parent.right = node
      node.parent = parent
    elif parent is None and self.root is None:
      self.root = node
    return node
    
  def search(self, data):
    root = self.root
    return self._search(root, data)
  
  def _search(self, root, data):
    if root is None or root.data == data:
      return root
    self.search(root.left, data)
    self.search(root.right, data)

  def delete(self, data):
    node = self.search(data)
    if node.parent is None:
      self.root = None
    elif node.parent.left == node:
      tmp = node.parent
      while tmp.right is not None:
        tmp = tmp.right
      tmp.right = node.right
      node.parent.left = node.left
    elif node.parent.right == node:
      tmp = node.parent
      while tmp.left is not None:
        tmp = tmp.left
      tmp.left = node.left
      node.parent.right = node.right

  def print_level(self):
    root = self.root
    Q = deque()
    Q.append(root)
    while len(Q) > 0:
      node = Q.popleft()
      print(node.data)
      if node.left is not None:
        Q.append(node.left)
      if node.right is not None:
        Q.append(node.right)


BT = BinaryTree()
n1 = BT.insertLeft(1)
n2 = BT.insertLeft(2, n1)
n3 = BT.insertRight(3, n1)
BT.print_level()