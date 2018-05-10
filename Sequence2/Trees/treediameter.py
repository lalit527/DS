from binarytree import BinaryTree, Node

def height(root):
  if root is None:
    return 0
  lh = height(root.left)
  rh = height(root.right)
  return 1 + max(lh, rh)

def diameter(root, level = 0):
  if root is None:
    return 0
  
  lh = diameter(root.left)
  rh = diameter(root.right)

  ld = diameter(root.left)
  rd = diameter(root.right)

  return max(lh + rh + 1, ld + rd)


t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
print(diameter(t.root))