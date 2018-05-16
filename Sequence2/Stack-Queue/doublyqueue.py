from ctypes import py_object

class DoubleQueue:
  def __init__(self, capacity=16):
    self.capacity = capacity
    self.data = (capacity * py_object)()
    self.front = -1
    self.rear = -1
    self.size = 0

  def enqueueFront(self, n):
    if self.front == -1:
      self.front = 0
    for i in range(self.rear - 1, self.front - 1, -1):
      self.data[i+1] = self.data[i]
    self.data[0] = n
    self.rear += 1
    self.size += 1
  
  def enqueueEnd(self, n):
    if self.front == -1:
      self.front = 0
    
    self.rear += 1
    self.data[self.rear] = n
    self.size += 1

  def dequeueFront(self):
    if self.front == -1:
      return Exception("Queue is Empty")
    
    tmp = self.data[self.front]
    self.front += 1
    return tmp


    def dequeueEnd(self):
      if self.front == -1:
        return Exception("Queue is Empty")
      tmp = self.data[self.rear]
      self.rear -= 1
      return tmp

  def peekFront(self):
    if self.front == -1:
      return Exception("Queue is Empty")
    return self.data[self.front]

  def peekEnd(self):
    if self.front == -1:
      return Exception("Queue is Empty")
    return self.data[self.rear]

q = DoubleQueue()
q.enqueueFront(1)
q.enqueueFront(2)
q.enqueueEnd(3)
q.enqueueEnd(4)
print(q.peekFront())
print(q.peekEnd())
    
    
    
