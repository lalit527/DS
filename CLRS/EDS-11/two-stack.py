from ctypes import py_object

class Stack:
  def __init__(self, size=16):
    self.size = size
    self.left_top = -1
    self.right_top = size
    self.data = (size * py_object)()
  
  def push_stack1(self, n):
    if (self.left_top + 1) == self.right_top:
      raise Exception("Stack1 is Full")
    self.left_top += 1
    self.data[self.left_top] = n
  
  def push_stack2(self, n):
    if (self.right_top - 1) == self.left_top:
      raise Exception("Stack2 is Full")
    self.right_top -= 1
    self.data[self.right_top] = n

  def pop_stack1(self):
    if self.left_top == -1:
      return Exception("Stack1 is empty")
    tmp = self.data[self.left_top]
    self.left_top -= 1
    return tmp

  def pop_stack2(self):
    if self.right_top == self.size:
      return Exception("Stack2 is Empty")
    tmp = self.data[self.right_top]
    self.right_top += 1
    return tmp

s = Stack(2)
s.push_stack1(5)
s.push_stack2(2)
s.push_stack1(7)
s.push_stack2(4)
# print(s.pop_stack1())
# print(s.pop_stack2())
# print(s.pop_stack1())
# print(s.pop_stack2())
