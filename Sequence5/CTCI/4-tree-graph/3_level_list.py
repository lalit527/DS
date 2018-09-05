from main.binary_search_tree import Node, BinarySearchTree
from collections import deque
from form_bst_2 import make_tree

class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  # def add(self, node):
  #   if self.next is None:
  #     self.next = node
  #   root = self.next
  #   while root.next is not None:
  #     root = root.next

class LinkedList:
  def __init__(self):
    self.head = None
  
  def add(self, data):
    node = LinkedNode(data)
    if self.head is None:
      self.head = node
    else:
      root = self.head
      while root.next is not None:
        root = root.next
      root.next = node



def make_list_dfs(root):
  lists = deque()
  _make_list(root, lists, 0)
  return lists

def _make_list(root, lists, level):
  if root is None:
    return root
  
  if len(lists) == level:
    list = LinkedList()
    lists.append(list)
  else:
    list = lists[level]
  list.add(root)
  _make_list(root.left, lists, level + 1)
  _make_list(root.right, lists, level + 1)


def make_list_bfs(root):
  lists = deque()
  current = LinkedList()
  if root is not None:
    current.add(root)
  while current.head is not None:
    lists.append(current)
    parents = current
    current = LinkedList()
    parent = parents.head
    while parent is not None:
      if parent.data:
        if parent.data.left:
          current.add(parent.data.left)
        if parent.data.right:
          current.add(parent.data.right)
      parent = parent.next
  return lists


nodes_flattened = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = make_tree(nodes_flattened)
lists = make_list_dfs(B.root)
for index, list in enumerate(lists):
  head = list.head
  print(index, end = " ")
  while head is not None:
    print(head.data.data, end = " ")
    head = head.next
  print("")