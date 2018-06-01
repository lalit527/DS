class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None

class Stack:
  def __init__(self):
    self.top = None

  def push(self, n):
    node = Node(n)
    node.prev = self.top
    self.top = node
  
  def pop(self):
    if self.top is None:
      return self.top
    tmp = self.top
    self.top = self.top.prev
    return tmp.data
  
  def peek(self):
    if self.top is None:
      return self.top
    return self.top.data
  
  def isEmpty(self):
    return self.top is None

# s = Stack()
# s.push(1)
# s.push(2)
# print(s.pop())
# print(s.pop())
# print(s.isEmpty())