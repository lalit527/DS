#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def create(self, tree):
    self.tree = tree
    # print(self.tree)
    if len(self.tree) > 0:
      self.root = self._create(self.root, 0, 0)

  def _create(self, root, row, col):
    root = Node(self.tree[row][col])
    if self.tree[row][col + 1] > -1:
      root.left = self._create(root, self.tree[row][col + 1], 0)
    if self.tree[row][col + 2] > -1:
      root.right = self._create(root, self.tree[row][col + 2], 0)
    
    return root

  def check_bst(self):
    root = self.root
    _max = float('inf')
    _min = float('-inf')
    return self._check_bst(root, _min, _max)

  def _check_bst(self, root, _min, _max):
    if root is None:
      return True
    if root.key < _min or root.key > _max:
      return False

    if (self._check_bst(root.left, _min, root.key) == False or
       self._check_bst(root.right, root.key, _max) == False):
      return False
    
    return True


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  T = Tree()
  T.create(tree)
  # inorder(T.root)
  return T.check_bst()

def inorder(root):
  if root:
    inorder(root.left)
    inorder(root.right)


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
