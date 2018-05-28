class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
  
  def enqueue(self, n):
    node = Node(n)
    if self.front is None:
      self.front = node
      self.rear = node
    else:
      self.rear.next = node
      self.rear = node

  def dequeue(self):
    if self.front is None:
      return None
    tmp = self.front
    self.front = self.front.next
    return tmp.data
  
  def isEmpty(self):
    return self.front is None
  
  def peek(self):
    return self.front.data if self.front else None

# q = Queue()
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.peek())