# python3

import sys

class Vertex:
  def __init__(self, key, value, left, right, parent):
    (self.key, self.value, self.left, self.right, self.parent) = (key, value, left, right, parent)

class SplayTree:
  root = None

  def update(self, v , u):
    if v is None or u is None:
      return
    v.value, u.value = u.value, v.value    


  def find(self, root, key):
    v = root
    last = root
    _next = None
    while v is not None:
      if v.key >= key and (_next == None or v.key < _next.key):
        _next = v
      last = v

      if v.key == key:
        break
      if v.key < key:
        v = v.right
      else:
        v = v.left
    root = self.splay(last)
    return (_next, root)

  def splay(self, v):
    if v == None:
      return v
    while v.parent != None:
      if v.parent.parent == None:
        self.small_rotation(v)
        break
      self.big_rotation(v)
    return v
    
  def small_rotation(self, v):
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


  def split(self, root, key):
    (result, root) = self.find(root, key)
    if result == None:
      return(root, None)
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

  def insert(self, x):
    (left, right) = self.split(self.root, x)
    pass

class Rope:
  def process(self, i, j, k):
    print(i, j, k)

  def __init__(self, s):
	  self.s = s

  def result(self):
    return self.s
  
  # def process(self, i, j, k):
  #   pass
                

if __name__ == "__main__":
  rope = Rope(sys.stdin.readline().strip())
  q = int(sys.stdin.readline())
  for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
  print(rope.result())
