class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None
    self.height = 1

class AVLTree:
  def __init__(self):
    self.root = None

  def find(self, key):
    root = self.root
    return self._find(root, key)

  def _find(self, root, key):
    if root is None:
      return root
    if root.key == key:
      return root
    elif root.key > key:
      return self._find(root.left, key)
    elif root.key < key:
      return self._find(root.right, key)

  def height(self):
    root = self.root
    return self._height(root)

  def _height(self, root):
    if root is None:
      return 0
    return root.height

  def adjust_height(self, node):
    node.height = 1 + max(node.left.height, node.right.height)

  def rebalance(self, node):
    p = node.parent
    if node.left.height > node.right.height + 1:
      self.rebalance_right(node)
    if node.right.height > node.left.height + 1:
      self.rebalance_left(node)
    
    self.adjust_height(node)
    if p is not None:
      self.adjust_height(p)

  def rebalance_right(self, node):
    m = node.left
    if m.right.height > m.left.height:
      self.left_rotate(m)
    self.right_rotate(node)

  def rebalance_left(self, node):
    n = node.right
    if n.left.height > n.right.height:
      self.right_rotate(n)
    self.left_rotate(node)


  def left_rotate(self, node):
    y = node.right
    node.right = y.left
    if y.left is not None:
      y.left.parent = node
    y.parent = node.parent
    if node.parent == None:
      self.root = y
    elif node == node.parent.left:
      node.parent.left = node
    elif node == node.parent.right:
      node.parent.right = node
    y.left = node
    node.parent = y

  def right_rotate(self, node):
    x = node.left
    node.left = x.right
    if node.right is not None:
      x.right.parent = node
    x.parent = node.parent
    if node.parent is None:
      self.root = x
    elif node == node.parent.left:
      node.parent.left = x
    elif node == node.parent.right:
      node.parent.right = x
    x.right = node
    node.parent = x

  def insert(self, key):
    node = Node(key)
    self._insert(root, node)

  def _insert(self, node):
    x = None
    y = self.root
    while y is not None:
      x = y
      if y.key > node.key:
        y = y.left
      else:
        x = x.right
    node.parent = x
    if x is None:
      self.root = node
    elif x.key > node.key:
      x.left = node
    else:
      x.right = node
    
    self.adjust_height(x)
      


def main():
  T = AVLTree()
  T.insert(2)

if __name__ == "__main__":
  main()