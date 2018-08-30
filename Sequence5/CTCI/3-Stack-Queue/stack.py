class Stack:
  class Node:
    def __init__(self, data):
      self.data = data
      self.prev = None
  
  def __init__(self):
    self.top = None
    self.bottom = None
    self.size = 0

  def push(self, data):
    node = Stack.Node(data)
    node.prev = self.top
    self.top = node
    self.size += 1
    if self.bottom is None:
      self.bottom = node

  def pop(self):
    if self.top is None:
      return None
    top = self.top
    self.top = top.prev
    if top:
      top.prev = None
    self.size -= 1
    if top == self.bottom:
      self.bottom = None
    return top.data

  def peek(self):
    return self.top.data if self.top else None

  def is_empty(self):
    return self.top is None
  
  def pop_first(self):
    bottom = self.bottom


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