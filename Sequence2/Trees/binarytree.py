from collections import deque
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insertLeft(self, n):
    node = Node(n)
    if self.root is None:
      self.root = node
    else:
      tmp = self.root
      while tmp.left is not None:
        tmp = tmp.left
      tmp.left = node

  def insertRight(self, n):
    node = Node(n)
    if self.root is None:
      self.root = node
    else:
      tmp = self.root
      while tmp.right is not None:
        tmp = tmp.right
      tmp.right = node

  def searchNode(self, root, r):
    queue = deque()
    if root is None:
      return False
    queue.append(root)
    while len(queue) > 0:
      node = queue.popleft()
      if node.data == r:
        return node
      if node.left is not None:
        queue.append(node.left)
      
      if node.right is not None:
        queue.append(node.right)
    return None


  def insertLeftNode(self, r, n):
    tmp = self.root
    result = self.searchNode(self.root, r)
    if result is not None:
      node = Node(n)
      result.left = node

  def insertRightNode(self, r, n):
    tmp = self.root
    result = self.searchNode(self.root, r)
    if result is not None:
      node = Node(n)
      result.right = node

  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      print(root.data)
      self._inorder(root.right)

