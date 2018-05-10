from binarytree import BinaryTree, Node

def exists(root, n):
  if root is None:
    return False
  if root.data == n:
    return True
  if exists(root.left, n) or exists(root.right, n):
    return True
  return False

def lca(root, p, q):
  if root is None:
    return None
  if root.data == p or root.data == q:
    return root
  l = lca(root.left, p, q)
  r = lca(root.right, p, q)

  if l and r:
    return root

  if l is None and r is not None:
    return r

  if l is not None and r is None:
    return l

  return None

# t = BinaryTree()
# t.insertLeft(5)
# t.insertLeft(4)
# t.insertLeft(3)
# t.insertRight(7)
# t.insertRight(9)
# t.insertLeftNode(7, 6)
# t.insertRightNode(9, 11)
# node = lca(t.root, 4, 7)
# print(node.data if node else None)