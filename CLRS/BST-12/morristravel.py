from bst import BinarySearchTree, Node
from collections import deque
from math import pow

def height(root):
  if root is None:
    return 0
  return 1 + max(height(root.left), height(root.right))

def pretty_print(root):
  if root is None:
    return
  Q = deque()
  Q.append(root)
  while len(Q) > 0:
    node = Q.popleft()
    print(node.key)
    if node.left:
      Q.append(node.left)
    if node.right:
      Q.append(node.right)

def morris_travel(root):
  current = root
  while current is not None:
    if current.left is None:
      print(current.key)
      current = current.right
    else:
      pre = current.left

      while pre.right is not None and pre.right != current:
        pre = pre.right
      
      if pre.right is None:
        pre.right = current
        current = current.left
      else:
        pre.right = None
        print(current.key)
        current = current.right



B = BinarySearchTree()
B.insert(5)
B.insert(4)
B.insert(2)
B.insert(3)
B.insert(9)
B.insert(7)
# print(height(B.root))
morris_travel(B.root)
