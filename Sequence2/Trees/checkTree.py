from binarytree import BinaryTree

def isIdentical(t1, t2):
  if t1 is None and t2 is None:
    return True
  if t1 is None and t2 is not None:
    return False
  if t1 is not None and t2 is None:
    return False
  if (t1.data == t2.data and 
     isIdentical(t1.left, t2.left) and
     isIdentical(t1.right, t2.right)):
    return True
  return False

def isMirror(t1, t2):
  if t1 is None and t2 is None:
    return True
  if t1 is None and t2 is not None:
    return False
  if t1 is not None and t2 is None:
    return False
  if (t1.data == t2.data and
      isMirror(t1.left, t2.right) and
      isMirror(t1.right, t2.left)):
    return True
  return False

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertRight(7)

s = BinaryTree()
s.insertLeft(5)
s.insertLeft(4)
s.insertRight(7)

r = BinaryTree()
r.insertLeft(5)
r.insertLeft(7)
r.insertRight(4)

print(isMirror(t.root, r.root))