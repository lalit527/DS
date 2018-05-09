from binarytree import BinaryTree, Node

def lca(root, p, q):
  if root is None:
    return None
  if root.data == p or root.data == q:
    return root
  l = lca(root.left, p, q)
  r = lca(root.right, p, q)
  if l is not None and r is not None:
    return root

  if l is not None and r is None:
    return l
  else:
    return r

def level(root, n, height = 0):
  if root is None:
    return 0
  if root.data == n:
    return height
  
  l = level(root.left, n, height + 1)
  r = level(root.right, n, height + 1)

  if l > 0:
    return l

  if r > 0:
    return r
  
  return -1

def distance(root, p, q):
  com = lca(root, p, q)
  l1 = level(com, p)
  l2 = level(com, q)
  return l1 + l2
  

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
print(distance(t.root, 4, 7))