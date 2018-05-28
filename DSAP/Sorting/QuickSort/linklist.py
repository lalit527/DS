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
  
  def insertLeft(self, n):
    node = Node(n)
    if self.head is None:
      self.head = node
    else:
      tmp = self.head
      self.head = node
      node.next = tmp

  def delete(self, n):
    tmp = self.head
    prev = None
    while tmp is not None:
      if tmp.data == n:
        


  def printData(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.key)
      tmp = tmp.next


def main():
  print("here")
  s = SingleLinkList()
  arr = [1, 2, 3, 4, 5]
  for i in arr:
    s.insert(i)
  s.printData()

if __name__ == '__main__':
  main()