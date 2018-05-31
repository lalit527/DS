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

def print_leaves(indent, level, node_in_this_level, Q, print):
  for i in range(node_in_this_level):
    w = (i == 0) ? indent + 2 : 2 * level + 2
    print()

def print_pretty(root, level, indent, print):
  h = height(root)
  node_in_this_level = 1

  branch_len = 2 * (pow(2.0, h) - 1) - (3 - level) * (pow(2.0, h - 1))
  node_space = 2 + (level + 1) * pow(2.0, h)
  start_len = branch_len + (3 - level) + indent

  Q = deque()
  Q.append(root)
  for i in range(1, h):
    print_branches(branch_len, node_space, start_len, node_in_this_level, Q, print)
    branch_len = branch_len // 2 - 1
    node_space = node_space // 2 + 1
    start_len = branch_len + (3 - leve) + indent
    print_nodes(branch_len, node_space, start_len, node_in_this_level, Q, print)

    for i in range(node_in_this_level):
      curr_node = Q.popleft()
      if curr_node is not None:
        Q.append(curr_node.left)
        Q.append(curr_node.right)
      else:
        Q.append(None)
        Q.append(None)
    node_in_this_level *= 2
  print_branches(branch_len, node_space, start_len, node_in_this_level, Q, print)
  print_leaves(indent, level, node_in_this_level, Q, print)

B = BinarySearchTree()
B.insert(5)
B.insert(4)
B.insert(2)
B.insert(3)
B.insert(9)
B.insert(7)
print(height(B.root))
#pretty_print(B.root)
