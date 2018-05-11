from binarysearchtree import BinarySearchTree, Node, inorder
from dll import DoubleLinkList, Node as LinkNode

class Current:
  def __init__(self, head):
    self.value = head

def length(head):
  count = 0
  while head is not None:
    count += 1
    head = head.next
  return count

def convertToBST(head):
  l = length(head)
  r = Current(head)
  root = _convertToBST(r, l)
  return root

def _convertToBST(r, l):
  if l <= 0:
    return None
  
  left = _convertToBST(r, l // 2)
  root = r.value
  root.prev = left
  r.value = r.value.next
  right = _convertToBST(r, l - (l // 2) -1)
  root.next = right 

  return root

def printData(head):
  if head:
    printData(head.prev)
    print(head.key)
    printData(head.next)

l = DoubleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  l.insert(i)

r = convertToBST(l.head)
printData(r)

