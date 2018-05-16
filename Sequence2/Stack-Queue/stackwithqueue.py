from queuelist import Queue

class StackWithOneQueue:
  def __init__(self):
    self.queue1 = Queue()
    self.queue2 = Queue()

  def push(self, n):
    self.queue1.enqueue(n)

  def pop(self):
    data = None
    while not self.queue1.isEmpty():
      n = self.queue1.dequeue()
      if self.queue1.isEmpty():
        data = n
      else:
        self.queue2.enqueue(n)
    tmp = self.queue2
    self.queue2 = self.queue1
    self.queue1 = tmp  
    return data

class StackWithOneQueue2:
  def __init__(self):
    self.queue = Queue()

  def push(self, n):
    self.queue.enqueue(n)

  def pop(self):
    if self.queue.isEmpty():
      return
    tmp = self.queue.dequeue()
    if not self.queue.isEmpty():
      self.pop()
      self.queue.enqueue(tmp)
    else:
      print('tmp', tmp)
      return tmp
    return tmp

  def print(self):
    tmp = self.queue.front
    while tmp is not None:
      print('data', tmp.data)
      tmp = tmp.next

s = StackWithOneQueue2()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
s.print()