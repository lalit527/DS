from binarytree import BinaryTree, Node

def level(root, node):
  level = 0
  return _level(root, node, level)

def _level(root, node, level):
  if root is None:
    return 0
  if root.data == node:
    return level
  l = _level(root.left, node, level+1)
  r = _level(root.right, node, level+1)

  if l > 0:
    return l

  if r > 0:
    return r
  return -1
t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
print(level(t.root, 11))