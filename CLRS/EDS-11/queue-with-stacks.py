from collections import deque

class Queue:
  def __init__(self):
    self.stack1 = deque()
    self.stack2 = deque()
  
  def enqueue(self, n):
    self.stack1.append(n)

  def dequeue(self):
    if len(self.stack2) == 0:
      n = len(self.stack1)
      while n > 0:
        self.stack2.append(self.stack1.pop())
        n -= 1
    return self.stack2.pop()

q = Queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(5)
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
    