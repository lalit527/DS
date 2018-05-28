from ctypes import py_object

class Queue:
  def __init__(self, capacity=16):
    self.capacity = capacity
    self.front = -1
    self.rear = -1
    self.data = (capacity * py_object)()

  def enqueue(self, n):
    if self.front == -1:
      self.front = 0

    if self.rear == self.capacity:
      return ValueError("Array Index should be in range")

    self.rear += 1
    self.data[self.rear] = n

  def dequeue(self):
    if self.front == -1:
      return None
    tmp = self.data[self.front]
    self.front += 1
    return tmp
  
  def isEmpty(self):
    return self.front == -1 or self.front > self.rear

  def peek(self):
    if self.front == -1:
      return None
    return self.data[self.front]
  
q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.peek())
print(q.peek())
print(q.peek())