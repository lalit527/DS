# python3

import sys
from collections import deque

class Vertex:
  def __init__(self, key, size, left, right, parent):
    (self.key, self.size, self.left, self.right, self.parent) = (key, size, left, right, parent)

class SplayTree:
  def __init__(self, s):
    self.root = None
    self.s = s
    for i in range(len(s)):
      vertex = Vertex(s[i], 0, None, None, None)
      self.root = self.merge(self.root, vertex)

  def update(self, v):
    if v is None:
      right
    v.size = 1 + (v.left.size if v.left is not None else 0) + (v.right.size if v.right is not None else 0) 
    if v.left is not None:
      v.left.parent = v
    if v.right is not None:
      v.right.parent = v 

  def merge(self, left, right):
    if left is None:
      return right
    if right is None:
      return left
    min_right = right
    while min_right.left is not None:
      min_right = min_right.left
    
    self.splay(right, min_right)
    right.left = left
    self.update(right)
    return right

  def big_rotation(self, v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
      self.small_rotation(v.parent)
      self.small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
      self.small_rotation(v.parent)
      self.small_rotation(v)
    else:
      self.small_rotation(v)
      self.small_rotation(v)

  def small_rotation(self, v):
    parent = v.parent
    if parent is None:
      return
    grand_parent = v.parent.parent
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
    v.parent = grand_parent
    if grand_parent is not None:
      if grand_parent.left == parent:
        grand_parent.left = v
      else:
        grand_parent.right = v

  def splay(self, root, v):
    if v is None:
      return
    while v.parent is not None:
      if v.parent.parent is None:
        self.small_rotation(v)
        break
      self.big_rotation(v)
    return v

  def find(self, root, key):
    v = root
    # last = root
    # _next = None
    while v is not None:
      # if v.key >= key and 
      s = v.left.sum if v.left is not None else 0
      if key == (s + 1):
        break
      elif key < (s + 1):
        v = v.left
      else:
        v = v.right

    self.splay(root, v)
    return v

  def split(self, root, key, left, right):
    right = self.find(root, key)
    if right is None:
      left = root
      return 
    left = right.left
    right.left = None
    if left is None:
      left.parent = None
    self.update(left)
    self.update(right)

  def merge(self, left, right):
    if left is None:
      return right
    if right is None:
      return left
    min_right = right
    while min_right is not None:
      min_right = min_right.left
    self.splay(right, min_right)
    right.left = left
    self.update(left)
    return right

  def insert(self, root, k, s):
    left = None
    right = None
    self.split(root, k, left, right)
    root = self.merge(merge(left, s), right)
  
  def in_order(self):
    return self._in_order(self.root)

  def _in_order(self, root):
    result = ""
    if root is None:
      result += ""
    S = deque()
    p = root
    while p is not None:
      S.append(p)
      p = p.left
    
    while len(S) > 0:
      p = S.pop()
      result += p.key
      p = p.right
      while p is not None:
        S.append(p)
        p = p.left
    
    return result
    

class Rope:
  def process(self, i, j, k):
    print(self.S.in_order())
    print(i, j, k)

  def __init__(self, s):
	  self.S = SplayTree(s)

  def result(self):
    return self.S.in_order()
    # return self.s
  
  # def process(self, i, j, k):
  #   pass
                

if __name__ == "__main__":
  rope = Rope(sys.stdin.readline().strip())
  q = int(sys.stdin.readline())
  for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
  
  print(rope.result())