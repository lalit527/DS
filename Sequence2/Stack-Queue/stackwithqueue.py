from queuelist import Queue
class Result:
  def __init__(self):
    self.data = None

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

  def _pop(self, r):
    if not self.queue.isEmpty():
      tmp = self.queue.dequeue()
      if self.queue.isEmpty():
        r.data = tmp
      else:
        self._pop(r)
        self.queue.enqueue(tmp)
        
    self.printData()
  
  def pop(self):
    r = Result()
    self._pop(r)
    return r.data
    
    
      

  def printData(self):
    tmp = self.queue.front
    while tmp is not None:
      print(tmp.data, end = " ")
      tmp = tmp.next

s = StackWithOneQueue2()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print('pop', s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
s.printData()