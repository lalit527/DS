from ctypes import py_object
class Queue:
  def __init__(self, capacity=16):
    self.capacity = capacity
    self.front = -1
    self.rear = -1
    self .data = (capacity * py_object)()

  def enqueue(self, n):
    if self.isFull():
      print('error')
      return Exception("Queue is Full")

    if self.front == -1:
      self.front = 0
    self.rear = (self.rear + 1) % self.capacity
    self.data[self.rear] = n
    print('error', self.rear, self.capacity)

  def dequeue(self):
    if self.front == -1 or self.front > self.rear:
      return Exception("Queue is Empty")

    else:
      tmp = self.data[self.front]
      self.front = (self.front + 1) % self.capacity
      return tmp
  
  def peek(self):
    if self.front == -1 or self.front > self.rear:
      return Exception("Queue is Empty")
    return self.data[self.front]

  def isFull(self):
        tmp = (self.rear+1) % self.capacity
        return tmp == self.front

  def isEmpty(self):
      return self.front == -1 or self.front > self.rear

q = Queue(2)
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())