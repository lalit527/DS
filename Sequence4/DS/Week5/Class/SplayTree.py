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
    # print(self._splay(self.root, key).key)
    self.root = self._splay(self.root, key)
    if self.root.key == key:
      return self.root

    return None

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

  def left_rotate(self, node):
    if not node:
      return None

    child = node.right

    if not child:
      return node
    
    node.right = child.left
    child.left = node

    return child


  def right_rotate(self, node):
    if not node:
      return None

    child = node.left

    if not child:
      return node
    
    node.left = child.right
    child.right = node

    return child

  def _splay(self, node, key):
    if node is None or node.key == key:
      return node

    if key < node.key:
      if node.left is None:
        return node
      
      if key < node.left.key:
        node.left.left = self._splay(node.left.left, key)
        node = self.right_rotate(node)

      elif key > node.left.key:
        node.left.right = self._splay(node.left.right, key)
        if node.left.right:
          node.left = self.left_rotate(node.left)

      if node.left:
        return self.right_rotate(node)

      return node

    elif key > node.key:
      if node.right == None:
        return node

      if key < node.right.key:
        node.right.left = self._splay(node.right.left, key)
        if node.right.left:
          node.right = self.right_rotate(node.right)

      elif key > node.right.key:
        node.right.right = self._splay(node.right.right, key)
        node = self.left_rotate(node)
      
      if node.right:
        return self.left_rotate(node)

    return node
  
  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
      return
    
    self.root = self._splay(self.root, key)

    if key == self.root.key:
      return

    node = Node(key)
    if key < self.root.key:
      node.right = self.root
      node.left = self.root.left
      self.root.left = None

    else:
      node.left = self.root
      node.right = self.root.right
      self.root.right = None

    self.root = node

  def delete(self, key):
    if self.root is None:
      return

    self.root = self._splay(self.root, key)

    if self.root.key == key:
      if self.root.left is None:
        self.root = self.root.right

      else:
        x = self.root.right
        self.root = self._splay(self.root.left, key)
        self.root.right = x

  def inorder(self):
    root = self.root
    self._inorder(root)

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.key)
      self._inorder(root.right)

S=SplayTree()
S.insert(5)
S.insert(7)
S.insert(9)
S.insert(3)
S.insert(2)
print(S.find(9).key)
S.delete(9)
root = S.find(7)
print(root.key, root.left, root.right)
print(S.root.key)
S.inorder()