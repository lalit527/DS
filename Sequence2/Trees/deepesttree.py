from binarytree import BinaryTree

def height(root):
  if root is None:
    return 0

  lh = height(root.left)
  rh = height(root.right)

  return max(lh, rh) + 1

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
print(height(t.root))