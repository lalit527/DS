class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
  
class CircularLinkList:
  def __init__(self):
    self.head = None

  def insert(self, n):
    if self.head is None:
      node = Node(n)
      self.head = node
      node.next = self.head
    else:
      tmp = self.head
      while tmp.next != self.head:
        tmp = tmp.next
      node = Node(n)
      tmp.next = node
      node.next = self.head

  def printData(self):
    tmp = self.head
    while tmp.next != self.head:
      print(tmp.key)
      tmp = tmp.next
    print(tmp.key)

c = CircularLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  c.insert(i)
c.printData()
