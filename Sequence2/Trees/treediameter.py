from binarytree import BinaryTree, Node

def diameter(root, level = 0):
  if root is None:
    return level
  
  l = diameter(root.left, level + 1)
  r = diameter(root.right, level + 1)
  return level


t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
print(diameter(t.root))