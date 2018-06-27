class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

class SplayTree:
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


  def splay(key):
    root = self.root
    node = self.find(key)
    return self._splay(node)

  def _splay(self, node):
    if node is None or node == self.root:
      return node
    elif node.parent == self.root:
      if node == node.parent.left:
        return self.right_rotate(node)
      elif node == node.parent.right:
        return self.left_rotate(node)
    elif node == node.parent.right and node.parent and node.parent.parent.left == node.parent:
      self.left_rotate(node)
      self.right_rotate(node)
    elif node == node.parent.left and node.parent.parent and node.parent.parent.right == node.parent:
      self.right_rotate(node)
      self.left_rotate(node)
    elif node == node.parent.left and node.parent.parent and node.parent.parent.left == node.parent:
      self.right_rotate(node.parent)
      self.right_rotate(node)
    elif node == node.parent.right and node.parent.parent and node.parent.parent.right == node.parent:
      self.left_rotate(node.parent)
      self.left_rotate(node)
    return self._splay(node)
  
  def __splay__(self, node):


  def __splay_chk__(self, root, key):
    if root is None or root.key == key:
      return root
    
    if root.key > key:
      if root.left is None:
        return root

      # Zig-zig (left-left)
      if root.left.key > key:
        root.left.left = self.__splay__(root.left.left, key)
        root = self.right_rotate(root)
      elif root.left.key < key:
        root.left.right = self.__splay__(root.left.right, key)

        if root.left.right:
          root.left = self.left_rotate(root.left)
    else:
      if root.right is None:
        return root

      if root.right.key > key:
        root.right.left = self.__splay__(root.right.left, key)

  def __splay_main__(self, node):
    while node.parent is not None:
      parent = node.parent
      grand_parent = node.parent.parent
      if grand_parent is None:
        if node == parent.left:
          self.right_rotate(node)
        elif node == parent.right:
          self.left_rotate(node)
      else:
        if node == parent.left and parent == grand_parent.left:
          

