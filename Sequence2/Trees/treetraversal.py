from binarytree import BinaryTree
from collections import deque

def inorder(root):
  if root:
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def preorder(root):
  if root:
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
  if root:
    postorder(root.data)
    postorder(root.left)
    postorder(root.right)

def levelOrder(root):
  if root is None:
    return
  queue = deque()
  queue.append(root)
  while len(queue) > 0:
    node = queue.popleft()
    print(node.data)
    if node.left is not None:
      queue.append(node.left)
    if node.right is not None:
      queue.append(node.right)

t = BinaryTree()
t.insertLeft(5)
t.insertLeft(4)
t.insertLeft(3)
t.insertRight(7)
t.insertRight(9)
t.insertLeftNode(7, 6)
t.insertRightNode(9, 11)
# print(t.root)
levelOrder(t.root)