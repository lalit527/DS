from stack import Stack

class StackMin:
  def __init__(self):
    self.stack = Stack()
    self.stack_min = Stack()
  
  def push(self, data):
    self.stack.push(data)
    if self.stack_min.is_empty():
      self.stack_min.push(data)
    else:
      top = self.stack_min.peek()
      if top > data:
        self.stack_min.push(data)
  
  def pop(self):
    top = self.stack.pop()
    if top == self.stack_min.peek():
      top_min = self.stack_min.pop()
    return top

  def min_stack(self):
    return self.stack_min.peek()


S = StackMin()
S.push(6)
S.push(7)
S.push(2)
S.push(5)
S.push(1)

print(S.min_stack())
print(S.pop())
print(S.min_stack())
print(S.pop())
print(S.min_stack())