from binarytree import BinaryTree

def size(root):
  if root is None:
    return 0

  l = size(root.left)
  r = size(root.right)

  return l + r + 1

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
print(size(t.root))