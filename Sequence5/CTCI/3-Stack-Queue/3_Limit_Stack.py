from stack import Stack

class StackSet:
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []

  def get_last_stack(self):
    n = len(self.stacks)
    if n > 0:
      return self.stacks[n - 1]
    else:
      return None
  
  def push(self, data):
    last = self.get_last_stack()
    if last is None or not last.size == self.capacity:
      stack = Stack()
      stack.push(data)
      self.stacks.append(stack)
    else:
      last.push(data)

  def pop(self):
    last = self.get_last_stack()
    if last is None:
      raise Exception("Stack Is Empty")
    top = last.pop
    if last.size == 0:
      self.stacks.pop()
    return top


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