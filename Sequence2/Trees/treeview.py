from binarytree import BinaryTree, Node
from collections import deque

def leftView(root):
  if root is None:
    return
  queue = deque()
  queue.append(None)
  queue.append(root)
  done = False
  while not done:
    node = queue.popleft()
    if node is None:
      if len(queue) > 0:
        node = queue.popleft()
        print(node.data)
        queue.append(None)
        if node.left is not None:
          queue.append(node.left)
        if node.right is not None:
          queue.append(node.right)
      else:
        done = True
    else:
      if node is not None and node.left is not None:
        queue.append(node.left)
      if node is not None and node.right is not None:
        queue.append(node.right)
      if len(queue) == 0:
        done = True

class MaxLevel:
  def __init__(self, value):
    self.value = value

def leftViewRec(root):
  m = MaxLevel(-1)
  _leftViewRec(root, 0, m)

def _leftViewRec(root, level, maxlevel):
  if root is None:
    return
  if maxlevel.value < level:
    print(root.data)
    maxlevel.value = level
  _leftViewRec(root.left, level + 1, maxlevel)
  _leftViewRec(root.right, level + 1, maxlevel)
  return
  

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
leftViewRec(t.root)