class SingleLinkList:
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

  def __init__(self):
    self.head = None
    self.tail = None

  def make_intersect(self, node1, node2):
    if node1 is None or node2 is None:
      return None
    node1.next = node2

  def append(self, node, data):
    if node is None and self.head:
      return node
    new_node = SingleLinkList.Node(data)
    if self.head is None:
      self.head = new_node
    else:
      node.next = new_node
    return new_node

  def appendLeft(self, n):
    node = SingleLinkList.Node(n)
    tmp = self.head
    self.head = node
    node.next = tmp
  
  def appendRight(self, n):
    node = SingleLinkList.Node(n)
    if self.tail is None:
      self.tail = node
      self.head = node
    else:
      self.tail.next = node
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
        else:
          self.head = tmp.next
        
        if tmp.next is None:
          self.tail = prev

      prev = tmp
      tmp = tmp.next
    return False

  def print_list(self):
    tmp = self.head
    while tmp is not None:
      print(tmp.data)
      tmp = tmp.next

if __name__ == '__main__':
  S = SingleLinkList()
  S.appendRight(1)
  S.appendRight(2)
  S.appendRight(3)
  S.appendRight(4)
  S.appendRight(5)
  S.appendRight(6)
  S.delete(6)
  S.print_list()
  print(S.tail.data)
