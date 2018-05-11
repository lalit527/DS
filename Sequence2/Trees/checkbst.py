from binarysearchtree import BinarySearchTree, inorder

def isBST(root):
  return _isBST(root, None, None)

def _isBST(root, min, max):
  if root is None:
    return True
  
  if ((min is not None and root.data <= min) or
      (max is not None and root.data > max)):
    return False
  
  if (_isBST(root.left, min, root.data) == False or 
      _isBST(root.right, root.data, max) == False):
    return False

  return True

t = BinarySearchTree(5)
t.insert(t.root, 3)
t.insert(t.root, 4)
t.insert(t.root, 2)
t.insert(t.root, 7)
t.insert(t.root, 6)
t.insert(t.root, 9)
inorder(t.root)