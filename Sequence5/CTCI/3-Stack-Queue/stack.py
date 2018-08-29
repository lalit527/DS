class Stack:
  class Node:
    def __init__(self, data):
      self.data = data
      self.prev = None
  
  def __init__(self):
    self.top = None

  def push(self, data):
    node = Stack.Node(data)
    node.prev = self.top
    self.top = node

  def pop(self):
    top = self.top
    self.top = top.prev
    top.prev = None
    return top.data

  def peek(self):
    return self.top.data if self.top else None

  def is_empty(self):
    return self.top is None
  
  def print_stack(self):
    top = self.top
    while top:
      print(top.data)
      top = top.prev

if __name__ == "__main__":
  S = Stack()
  S.push(1)
  S.push(2)
  print(S.pop())
  S.print_stack()