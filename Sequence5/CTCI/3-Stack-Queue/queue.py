class Queue:
  class Node:
    def __init__(self, data):
      self.data = data
      self.prev = None
      self.next = None
  
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, data):
    node = Queue.Node(data)
    if self.front is None:
      self.front = node
      self.rear = node
    else:
      node.prev = self.rear
      self.rear.next = node
      self.rear = node

  def dequeue(self):
    front = self.front
    self.front = front.next
    front.next = None
    return front.data

  def peek(self):
    return self.front.data if self.top else None
  
  def print_queue(self):
    front = self.front
    while front:
      print(front.data)
      front = front.next

Q = Queue()
Q.enqueue(1)
Q.enqueue(2)
print('data',Q.dequeue())
Q.print_queue()