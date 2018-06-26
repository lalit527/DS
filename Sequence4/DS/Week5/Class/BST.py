class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

class BST:
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

  def next(self, key):
    root = self.root
    node = self._find(root, key)
    return self._next(node) if node else None
    
  def _next(self, node):
    if node is None:
      return None
    elif node.right is not None:
      return self.left_descendent(node.right)
    else:
      return self.right_anchestor(node)

  def left_descendent(self, node):
    if node.left is None:
      return node
    else:
      return self.left_descendent(node.left)

  def right_anchestor(self, node):
    if node is None:
      return node
    if node.parent and node.key < node.parent.key:
      return node.parent
    else:
      return self.right_anchestor(node.parent)

  def range_search(self, x, y):
    root = self.root
    self._range_search(x, y, root)
  
  def _range_search(self, x, y, root):
    L = None
    N = self._find(root, x)
    while N.key <= y:
      if N.key >= x:
        L.append(N)
      N = self._next(N)

  def insert(self, key):
    node = Node(key)
    self._insert(node)
  
  def _insert(self, z):
    y = None
    x = self.root
    while x is not None:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    z.parent = y
    if y is None:
      self.root = z
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z
  
  def tree_minimum(self):
    root = self.root
    self.tree_minimum(root)

  def _tree_minimum(self, root):
    if root is None:
      return root
    while root.left is not None:
      root = root.left
    return root

  def tree_maximum(self):
    root = self.root
    self._tree_maximum(root)

  def _tree_maximum(self, root):
    if root is None:
      return root
    while root.right is not None:
      root = root.right
    return root

  def tree_successor(self, key):
    node = self.find(key)
    return self._tree_successor(node)

  def _tree_successor(self, node):
    if node:
      if node.right is not None:
        return self._tree_minimum(node.right)
      y = node.parent
      while y is not None and node == y.right:
        node = y
        y = y.parent
      return y

  def tree_predessor(self, key):
    node = self.find(key)
    return self._tree_predessor(node)

  def _tree_predessor(self, node):
    if node:
      if node.left is not None:
        return self._tree_maximum(node.left)
      y = node.parent
    
      while y is not None and node == y.left:
        node = y
        y = y.parent
      return y
    
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.key)
      self._inorder(root.right)

  def transplant(self, u, v):
    if u.parent is None:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
    if v is not None:
      v.parent = u.parent

  def delete(self, key):
    root = self.root
    node = self.find(key)
    self._delete(root, node)

  def _delete(self, root, node):
    if node.left is None:
      self.transplant(node, node.right)
    elif node.right is None:
      self.transplant(node, node.left)
    else:
      y = self._tree_minimum(node.right)
      if y.parent != node:
        self.transplant(node, node.right)
        y.right = node.right
        y.right.parent = y
      
      self.transplant(node, y)
      y.left = node.left
      y.left.parent = y


def main():
  B = BST()
  B.insert(5)
  B.insert(4)
  B.insert(7)
  B.insert(3)
  B.insert(8)
  B.insert(9)
  # print(B.tree_predessor(5).key)
  # print(B.tree_successor(5).key)
  B.delete(4)
  B.inorder()

if __name__ == "__main__":
  main()