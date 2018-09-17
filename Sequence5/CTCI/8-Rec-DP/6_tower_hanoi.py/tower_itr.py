class Stack:
  def __init__(self, capacity):
    self.capacity = capacity
    self.top = -1
    self.arr = []

  def is_empty(self):
    return self.top == -1
  
  def push(self, item):
    self.top += 1
    self.arr.append(item)

  def pop(self):
    if len(self.arr) > 0:
      self.top -= 1
      return self.arr.pop()
  
  def peep(self):
    if len(self.arr) > 0:
      return self.arr[-1]

class Tower:

