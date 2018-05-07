class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
  
class SingleLinkList:
  def __init__(self):
    self.head = None
  
  def insert(self, n):
    if self.head is None:
      self.head = Node(n)
    else:
      tmp = self.head
      while tmp.next != None:
        tmp = tmp.next
      tmp.next = Node(n)

  def printData(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.key)
      tmp = tmp.next

  
s = SingleLinkList()
arr = [1, 2, 3, 4, 5]
for i in arr:
  s.insert(i)
# s.printData()