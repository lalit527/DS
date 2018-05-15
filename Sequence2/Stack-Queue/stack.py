from ctypes import py_object

class Stack:
  def __init__(self, capacity=16):
    self.capacity = capacity
    self.data = (capacity * py_object)()
    self.top = -1
  
  def push(self, n):
    if self.top == self.capacity:
      print("Stack is Full")
      return
    self.top += 1
    self.data[self.top] = n
  
  def pop(self):
    if self.top == -1:
      return None
    tmp = self.data[self.top]
    self.top -= 1
    return tmp

  def peek(self):
    if self.top == -1:
      return None
    return self.data[self.top]
  
  def isEmpty(self):
    return self.top == -1
    
s = Stack(8)
s.push(1)
s.push(2)
print(s.pop())
