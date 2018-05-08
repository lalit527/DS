from binarytree import BinaryTree, Node

def mirrorTree(root):
  if root is None:
    return root
  root.data = root.data
  root.left, root.right = root.right, root.left
  mirrorTree(root.left)
  mirrorTree(root.right)

def mirrorTreeBU(root):
  if root is None:
    return root
  root.data = root.data
  mirrorTree(root.left)
  mirrorTree(root.right)
  root.left, root.right = root.right, root.left

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertRight(7)
mirrorTreeBU(t.root)
t.inorder()