from ctypes import py_object

class DoubleQueue:
  def __init__(self, capacity=16):
    self.capacity = capacity
    self.data = (capacity * py_object)()
    self.front = -1
    self.rear = -1

  def enqueueFront(self, n):
    if self.front == -1:
      self.front = 0
    print(len(self.data))
    for i in range(len(self.data) - 2, -1, -1):
      self.data[i+1] = self.data[i]
    self.data[0] = n
    self.rear += 1
  
  def enqueEnd(self):
    if self.front == -1:
      self.front = 0
    
    self.rear += 1
    self.data[self.rear] = n

  def dequeFront(self):
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
q.enqueueBack(3)
q.enqueueBack(4)
print(q.peekFront())
print(q.peekEnd())
    
    
    
