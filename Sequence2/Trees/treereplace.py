from binarytree import BinaryTree
from treetraversal import levelOrder

def replaceNode(root):
  if root is None:
    return 0

  l = replaceNode(root.left)
  r = replaceNode(root.right)
  sum = l + r + 1
  root.data += sum
  return root.data

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
levelOrder(t.root)
print(replaceNode(t.root))