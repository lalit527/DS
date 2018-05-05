class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
    self.prev = None
  
class DoubleLinkList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, n):
    if self.head is None:
      node = Node(n)
      self.head = node
      self.tail = node
    else:
      tmp = self.head
      while tmp.next is not None:
        tmp = tmp.next
      node = Node(n)
      node.prev = tmp
      tmp.next = node
      self.tail = node
      
  def printData(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.key)
      tmp = tmp.next

  def printReverse(self):
    tmp = self.tail
    while tmp is not None:
      print(tmp.key)
      tmp = tmp.prev



l = DoubleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  l.insert(i)
l.printData()
l.printReverse()