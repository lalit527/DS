#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**10) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size
from collections import deque

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

class Tree:
  def __init__(self):
    self.root = None

  def create(self, tree):
    self.tree = tree
    if len(self.tree) > 0:
      self.root = self._create(self.root, 0, 0)

  def _create(self, root, row, col):
    root = Node(self.tree[row][col])
    if self.tree[row][col + 1] > -1:
      root.left = self._create(root, self.tree[row][col + 1], 0)
      root.left.parent = root
    if self.tree[row][col + 2] > -1:
      root.right = self._create(root, self.tree[row][col + 2], 0)
      root.right.parent = root
    
    return root


  def _check_bst_(self):
    return self._isBST(self.root, None, None)

  def _isBST(self, root, min, max):
    if root is None:
      return True
    
    if ((min is not None and root.key <= min) or
        (max is not None and root.key > max)):
      return False
    
    if (self._isBST(root.left, min, root.key) == False or 
        self._isBST(root.right, root.key, max) == False):
      return False
    return True

  def check_bst(self):
    root = self.root
    _max = float('inf')
    _min = float('-inf')
    return self._check_bst(root, _min, _max)

  def _check_bst(self, root, _min, _max, child = None):
    if root is None:
      return True
    print(root.key, _min, _max, child)
    if root.key <= _min or root.key > _max:
      return False

    if (self._check_bst(root.left, _min, root.key, 'left') == False or
       self._check_bst(root.right, root.key, _max, 'right') == False):
      return False
    
    return True

  def inorder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._inorder_(self.root)
    return self.result

  def _inorder_(self, root):
    if root:
      self._inorder_(root.left)
      self.result.append(root.key)
      self._inorder_(root.right)

  def preorder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._preorder(self.root)
    return self.result

  def _preorder(self, root):
    if root:
      self.result.append(root.key)
      self._preorder(root.left)
      self._preorder(root.right)


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  T = Tree()
  T.create(tree)
  result = T.inorder()
  print(result)
  result = T.preorder()
  print(result)
  return T.check_bst()


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
