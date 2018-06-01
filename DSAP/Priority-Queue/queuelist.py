class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0
  
  def enqueue(self, n):
    node = Node(n)
    if self.front is None:
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = node
    self.size += 1

  def dequeue(self):
    if self.front is None:
      return None
    tmp = self.front
    self.front = self.front.next
    self.size -= 1
    return tmp.data
  
  def isEmpty(self):
    return self.front is None
  
  def peek(self):
    return self.front.data if self.front else None

  def length(self):
    return self.size

  def printQueue(self):
    tmp = self.front
    while tmp is not None:
      print(tmp.data)
      tmp = tmp.next