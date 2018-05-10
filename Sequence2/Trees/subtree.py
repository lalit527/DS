from binarytree import BinaryTree, Node

def isIdentical(root1, root2):
  if root1 is None and root2 is None:
    return True
  if root1 is None or root2 is None:
    return False

  return (root1.data == root2.data and 
          isIdentical(root1.left, root2.left) and
          isIdentical(root1.right, root2.right)
          )

def isSubtree(t, s):
  if t is None:
    return True
  if s is None:
    return True
  if (isIdentical(t, s)):
    return True

  return isSubtree(t.left, s) or isSubtree(t.right, s)
  # l = isSubtree(t.left, s)
  # if l == True:
  #   return True
  
  # r = isSubtree(t.right, s)
  # if r == True:
  #   return True
  
  # return False



t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
s = BinaryTree()
s.insertLeft(5)
s.insertLeft(4)
s.insertRight(17)
t.inorder()
print(isSubtree(t.root, s.root))