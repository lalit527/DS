class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
class BinarySearchTree:
  def __init__(self, n):
    self.root = Node(n)
  
  def insert(self, root, n):
    if root is None:
      return root
    if root.data > n:
      if root.left is None:
        root.left = Node(n)
      else:
        self.insert(root.left, n)
    elif root.data < n:
      if root.right is None:
        root.right = Node(n)
      else:
        self.insert(root.right, n)
  
  def search(self, root, n):
    if root is None:
      return False
    if root.data == n:
      return True
    elif root.data > n:
      return self.search(root.left, n)
    else:
      return self.search(root.right, n)

  def delete(self, root, n):
    if root is None:
      return root
    if root.data > n:
      root.left = self.delete(root.left, n)
    elif root.data < n:
      root.right = self.delete(root.right, n)
    else:
      if root.left is None:
        tmp = root.right
        root = None
        return tmp
      elif root.right is None:
        tmp = root.left
        root = None
        return tmp
      else:
        tmp = successor(root)
        root.data = tmp.data
        root.left = self.delete(root.left, tmp.data)
    
    return root

def successor(root):
  tmp = root.left
  while tmp.right is not None:
    tmp = tmp.right
  return tmp

def inorder(root):
  if root:
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# t = BinarySearchTree(5)
# t.insert(t.root, 3)
# t.insert(t.root, 4)
# t.insert(t.root, 2)
# t.insert(t.root, 7)
# t.insert(t.root, 6)
# t.insert(t.root, 9)
# print(t.search(t.root, 8))
# t.delete(t.root, 7)
# inorder(t.root)