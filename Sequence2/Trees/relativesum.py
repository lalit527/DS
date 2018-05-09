from binarytree import BinaryTree, Node

def rsum(root, node = None):
  if root is None:
    return root
  if node is None:
    node = Node(root.data)
  else:
    node.data += root.data
  
  node.left

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)