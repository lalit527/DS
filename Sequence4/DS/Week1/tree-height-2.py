# python3

import sys, threading
from collections import deque
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None
  
  def add_child(self, child):
    self.children.append(child)

  def add_parent(self, parent):
    self.parent = parent
  
  def print_child(self):
    for i in self.children:
      print(i)

class Tree:
  def __init__(self):
    self.root = None
    self.nodes = []

  def allocate_node(self, arr, n):
    for i in range(n):
      node = Node(i)
      self.nodes.append(node)
    for child_index in range(n):
      parent_index = arr[child_index]
      if parent_index == -1:
        self.root = self.nodes[child_index]
      else:
        self.nodes[parent_index].add_child(self.nodes[child_index])
        self.nodes[child_index].add_parent(self.nodes[parent_index])
    
    if self.root is None:
      self.root = nodes[0]
    
    return self.root


  def insertLeft(self, root, data):
    node = Node(data)
    if root is None:
      self.root = node
    else:
      tmp = root.left
      root.left = node
      node.left = tmp
    return node

  def insertRight(self, data):
    node = Node(data)
    if root is None:
      self.root = node
    else:
      tmp = root.right
      root.right = node
      node.right = tmp
    return node

  def level_order(self):
    queue = deque()
    root = self.root
    count = 0
    queue.append((count,root))
    while len(queue) > 0:
      data = queue.popleft()
      count += 1
      if len(data[1].children) > 0:
        count += 1
        for i in data[1].children:
          print('i', i.data, 'parent', i.parent.data)
          queue.append((count, i))
    print('count', data[0])



class TreeHeight:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.parent = list(map(int, sys.stdin.readline().split()))
    self.tree = None

  def compute_height(self):
    # Replace this code with a faster implementation
    maxHeight = 0
    for vertex in range(self.n):
      height = 0
      i = vertex
      while i != -1:
        height += 1
        i = self.parent[i]
      maxHeight = max(maxHeight, height)
    return maxHeight
  
  def compute_height_better(self):
    root = self.tree
    return self._compute_height_better(root)

  def _compute_height_better(self, root):
    if root is None:
      return 0
    max_height = 0
    for i in root.children:
      child_height = self._compute_height_better(i)
      max_height = max(child_height, max_height)
    return max_height + 1

  def create(self):
    T = Tree()
    self.tree = T.allocate_node(self.parent, self.n)
    T.level_order()

  def print(self):
    print(self.n)
    print(self.parent)

    

def main():
  tree = TreeHeight()
  tree.read()
  tree.create()
  print(tree.compute_height_better())

threading.Thread(target=main).start()
