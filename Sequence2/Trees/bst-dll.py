from binarysearchtree import BinarySearchTree, Node
from dll import DoubleLinkList, Node as LinkNode

class DLL:
  def __init__(self, data):
    self.data = data

class Previous:
  def __init__(self):
    self.value = None


def bst2dll(root):
  prev = Previous()
  h = Previous()
  _bst2dll(root, prev, h)
  return h.value

def _bst2dll(root, prev, h):
  if root is None:
    return root
  
  _bst2dll(root.left, prev, h)
  if prev.value is None:
    head = root
    h.value = root
  else:
    root.left = prev.value
    prev.value.right = root 
  prev.value = root
  _bst2dll(root.right, prev, h)

def printList(head):
  tmp = head
  while tmp.right is not None:
    print(tmp.right.data)
    tmp = tmp.right
s = BinarySearchTree(5)
s.insert(s.root, 3)
s.insert(s.root, 4)
s.insert(s.root, 2)
s.insert(s.root, 7)
s.insert(s.root, 6)
s.insert(s.root, 9)

h = bst2dll(s.root)
printList(h)

