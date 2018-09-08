from stack import Stack

class MyQueue:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, data):
    self.stack1.push(data)

  def dequeue(self):
    if self.stack2.size == 0:
      while  self.stack1.size != 0:
        top = self.stack1.pop()
        self.stack2.push(top)
    return self.stack2.pop()

Q = MyQueue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())