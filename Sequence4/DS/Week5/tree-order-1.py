# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

class TreeOrders:
  def __init__(self):
    self.root = None

  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    print(self.key)
    print(self.left)
    print(self.right)
    self.root = self.create(0)

  def parse_tree(self):
    i = 0
    for i in range(self.n):
      root = Node(self.key[i])
      if self.left[i] > -1:
        root.left = Node(self.left[i])
      if self.right[i] > -1:
        root.right = Node(self.right[i])


  def create(self, i):
    root = Node(self.key[i])
    if self.left[i] > -1:
      root.left = self.create(self.left[i])
    if self.right[i] > -1:
      root.right = self.create(self.right[i])
    return root


    
      

  def inOrder_(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._inorder_(0)
    return self.result

  def _inorder_(self, i):
    if i < self.n:
      self._inorder_(self.left[i])
      self.result.append(self.key[i])
      self._inorder_(self.right[i])
      


  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._inorder(self.root)
    return self.result

  def _inorder(self, root):
    if root:
      self._inorder(root.left)
      self.result.append(root.key)
      self._inorder(root.right)

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._preOrder(self.root)         
    return self.result

  def _preOrder(self, root):
    if root:
      self.result.append(root.key)
      self._preOrder(root.left)
      self._preOrder(root.right)


  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._postOrder(self.root)                  
    return self.result
  
  def _postOrder(self, root):
    if root:
      self._postOrder(root.left)
      self._postOrder(root.right)
      self.result.append(root.key)

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
