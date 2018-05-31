from collections import deque

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self, n):
    node = Node(n)
    self._insert(node)

  def _insert(self, node):
    tmp = None
    root = self.root
    while root is not None:
      tmp = root
      if node.key < root.key:
        root = root.left
      else:
        root = root.right
    node.parent = tmp
    if tmp is None:
      self.root = node
    elif node.key < tmp.key:
      tmp.left = node
    else:
      tmp.right = node

  def inorder(self):
    self._inorder(self.root)
    print("")

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.key, end="-")
      self._inorder(root.right)

  def _inorder_st(self, root):
    current = root
    stack = deque()
    stack.append(root)
    while len(stack) > 0:
      if current.left is not None:
        current = current.left
        stack.append(current)
      else:
        node = stack.pop()
        print(node.key)
        if node.right:
          current = node.right
          stack.append(node.right)

  def search(self, key):
    # node = self._search(self.root, key)
    node = self._search_rec(self.root, key)
    if node:
      return True
    return False

  def _search(self, root, key):
    while root is not None:
      if root.key == key:
        return root
      elif root.key < key:
        root = root.right
      else:
        root = root.left
    return None

  def _search_rec(self, root, key):
    if root is None or root.key == key:
      return root
    
    if root.key < key:
      return self._search_rec(root.right, key)
    else:
      return self._search_rec(root.left, key)

  def _transplant(self, u, v):
    if u.parent is None:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v

  def _tree_min(self, x):
    while x.left is not None:
      x = x.left
    return x

  def _tree_delete(self, z):
    if z.left is None:
      self._transplant(z, z.right)
    elif z.right is None:
      self._transplant(z, z.left)
    else:
      y = self._tree_min(z.right)
      if y.parent != z:
        self._transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      self._transplant(z, y)
      y.left = z.left
      y.left.parent = y

def main():      
  B = BinarySearchTree()
  B.insert(5)
  B.insert(4)
  B.insert(2)
  B.insert(3)
  B.insert(9)
  B.insert(7)
  B.inorder()
  print(B.search(7))
  #B._inorder_st(B.root)

if __name__ == '__main__':
  main()