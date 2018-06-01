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

  def delete(self, n):
    if self.head is None:
      return Exception("No Node to Delete")
    if self.head.key == n:
      self.head = self.head.next
    else:
      tmp = self.head
      while tmp.next is not None:
        if tmp.next.key == n:
          tmp.next = tmp.next.next
          break
        tmp = tmp.next


  def printData(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.key)
      tmp = tmp.next

def main():
  s = SingleLinkList()
  arr = [1, 2, 3, 4, 5]
  for i in arr:
    s.insert(i)
  s.delete(2)
  s.printData()

if __name__ == '__main__':
  main()