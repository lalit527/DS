class DoubleLinkList:
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

  def __init__(self):
    self.head = None
    self.tail = None

  def appendLeft(self, n):
    node = DoubleLinkList.Node(n)
    tmp = self.head
    self.head = node
    node.next = tmp
    tmp.prev = node
  
  def appendRight(self, n):
    node = DoubleLinkList.Node(n)
    if self.tail is None:
      self.tail = node
      self.head = node
    else:
      self.tail.next = node
      node.prev = self.tail
      self.tail = node

  def search(self, n):
    tmp = self.head
    while tmp is not None:
      if tmp.data == n:
        return True
      tmp = tmp.next
    return False

  def delete(self, n):
    tmp = self.head
    prev = None
    while tmp is not None:
      if tmp.data == n:
        if prev is not None:
          prev.next = tmp.next
          tmp.prev = prev
        else:
          self.head = tmp.next
        
        if tmp.next is None:
          self.tail = prev

      prev = tmp
      tmp = tmp.next
    return False

  def traverse(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.data)
      tmp = tmp.next

  def traverse_rev(self):
    tmp = self.tail
    while tmp is not None:
      print(tmp.data)
      tmp = tmp.prev

if __name__ == '__main__':
  S = DoubleLinkList()
  S.appendRight(1)
  S.appendRight(2)
  S.appendRight(3)
  S.appendRight(4)
  S.appendRight(5)
  S.appendRight(6)
  S.delete(3)
  S.traverse_rev()
  # print(S.tail.data)
