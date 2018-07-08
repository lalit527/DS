# python3

from sys import stdin
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


class SplayTree:

  def update(self, v):
    if v == None:
      return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
      v.left.parent = v
    if v.right != None:
      v.right.parent = v

  def smallRotation(self, v):
    parent = v.parent
    if parent == None:
      return
    grandparent = v.parent.parent
    if parent.left == v:
      m = v.right
      v.right = parent
      parent.left = m
    else:
      m = v.left
      v.left = parent
      parent.right = m
    self.update(parent)
    self.update(v)
    v.parent = grandparent
    if grandparent != None:
      if grandparent.left == parent:
        grandparent.left = v
      else: 
        grandparent.right = v

  def bigRotation(self, v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
      # Zig-zig
      self.smallRotation(v.parent)
      self.smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
      # Zig-zig
      self.smallRotation(v.parent)
      self.smallRotation(v)    
    else: 
      # Zig-zag
      self.smallRotation(v)
      self.smallRotation(v)

  # Makes splay of the given vertex and makes
  # it the new root.
  def splay(self, v):
    if v == None:
      return None
    while v.parent != None:
      if v.parent.parent == None:
        self.smallRotation(v)
        break
      self.bigRotation(v)
    return v

  # Searches for the given key in the tree with the given root
  # and calls splay for the deepest visited node after that.
  # Returns pair of the result and the new root.
  # If found, result is a pointer to the node with the given key.
  # Otherwise, result is a pointer to the node with the smallest
  # bigger key (next value in the order).
  # If the key is bigger than all keys in the tree,
  # then result is None.
  def find(self, root, key): 
    v = root
    last = root
    next = None
    while v != None:
      if v.key >= key and (next == None or v.key < next.key):
        next = v    
      last = v
      if v.key == key:
        break    
      if v.key < key:
        v = v.right
      else: 
        v = v.left      
    root = self.splay(last)
    return (next, root)

  def split(self, root, key):  
    (result, root) = self.find(root, key)  
    if result == None:    
      return (root, None)  
    right = self.splay(result)
    left = right.left
    right.left = None
    if left != None:
      left.parent = None
    self.update(left)
    self.update(right)
    return (left, right)

    
  def merge(self, left, right):
    if left == None:
      return right
    if right == None:
      return left
    while right.left != None:
      right = right.left
    right = self.splay(right)
    right.left = left
    self.update(right)
    return right

class SetRange:
  # Code that uses splay tree to solve the problem
  root = None
  S = SplayTree()

  def insert(self, x):
    (left, right) = self.S.split(self.root, x)
    new_vertex = None
    if right == None or right.key != x:
      new_vertex = Vertex(x, x, None, None, None)  
    self.root = self.S.merge(self.S.merge(left, new_vertex), right)
    
  def erase(self, x): 
    if self.search(x) is None:
      return

    self.S.splay(self.root)
    self.root = self.S.merge(self.root.left, self.root.right)
    if self.root is not None:
      self.root.parent = None

  def search(self, x): 
    # Implement find yourself
    result, self.root = self.S.find(self.root, x)
    if result is None or self.root.key != x:
      return None
    return result.key
    
  def sum(self, fr, to): 
    (left, middle) = self.S.split(self.root, fr)
    (middle, right) = self.S.split(middle, to + 1)
    ans = 0
    # Complete the implementation of sum
    if middle is None:
      ans = 0
      self.root = self.S.merge(left, right)
    else:
      ans = middle.sum
      self.root = self.S.merge(self.S.merge(left, middle), right)

    return ans
  
  def get_tree(self):
    print(self.root.key)
    self._get_tree(self.root)
  
  def _get_tree(self, root):
    if root:
      self._get_tree(root.left)
      print(root.key)
      self._get_tree(root.right)



def main():
  MODULO = 1000000001
  n = int(stdin.readline())
  last_sum_result = 0

  s = SetRange()

  for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
      x = int(line[1])
      s.insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
      x = int(line[1])
      s.erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
      x = int(line[1])
      print('Found' if s.search((x + last_sum_result) % MODULO) is not None else 'Not found')
    elif line[0] == 's':
      l = int(line[1])
      r = int(line[2])
      res = s.sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
      print(res)
      last_sum_result = res % MODULO

    elif line[0] == 'c':
      s.get_tree()

if __name__ == "__main__":
  main()