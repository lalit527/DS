from stacklist import Stack

class QueueTwoStack:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, n):
    self.stack1.push(n)

  def dequeue(self):
    if self.stack2.isEmpty():
      while not self.stack1.isEmpty():
        self.stack2.push(self.stack1.pop())

    return self.stack2.pop()

class QueueOneStack:
  def __init__(self):
    self.stack = Stack()
  
  def enqueue(self, n):
    self.stack.push(n)

  def dequeue(self):
    if self.stack.isEmpty():
      return None
    node = self.stack.pop()
    if self.stack.isEmpty():
      print(node)
    else:
      self.dequeue()
      self.stack.push(node)

q = QueueOneStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())