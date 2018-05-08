from binarytree import BinaryTree
from collections import deque

def inorder(root):
  if root:
    inorder(root.left)
    print(root.data)
    inorder(root.data)

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