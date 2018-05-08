from binarytree import BinaryTree, Node

def identical(root):
  clone = BinaryTree()
  clone.root = _identical(root)
  return clone

def _identical(root):
  if root is None:
    return root
  tree = Node(root.data)
  tree.left = _identical(root.left)
  tree.right = _identical(root.right)
  return tree

def mirror(root):
  mirror = BinaryTree()
  mirror.root = _mirror(root)
  return mirror

def _mirror(root):
  if root is None:
    return root
  node = Node(root.data)
  node.left = _mirror(root.right)
  node.right = _mirror(root.left)
  return node

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertRight(7)
tree = identical(t.root)
print(tree.inorder() if tree else None)

mirrorTree = mirror(t.root)
print(mirrorTree.inorder() if tree else None)