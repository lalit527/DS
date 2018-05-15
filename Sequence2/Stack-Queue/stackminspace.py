from stacklist import Stack

class StackWithMin:
  def __init__(self):
    self.stack = Stack()
    self.minStack = Stack()

  def push(self, n):  
    cur = self.minStack.peek()
    if cur is None or cur > n:
      self.stack.push(n)
      self.minStack.push(n)
    else:
      self.stack.push(n)
    
  def pop(self):
    tmp = self.stack.pop()
    min = self.minStack.peek()
    if tmp == min:
      min = self.minStack.pop()
    return tmp
  
  def getMin(self):
    return self.minStack.peek()
      
s = StackWithMin()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(1)
print(s.pop())
print(s.getMin())