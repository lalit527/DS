from collections import deque

class StackWithQueue:
  def __init__(self):
    self.qeue1 = deque()
    self.qeue2 = deque()

  def push(self, n):
    self.qeue1.append(n)

  # def pop(self):
  #   if (len(self.qeue2) == 0):
  #     n = len(self.qeue1)
  #     while n > 0:
  #       data = self.qeue1.popleft()
  #       print(data)
  #       self.qeue2.append(data)
  #       n -= 1
  #   n = len(self.qeue2)
  #   while n > 0:
  #     print(self.qeue2.popleft())
  #     if len(self.qeue2) == 0:

  #     n -= 1
  def pop(self):
    if (len(self.qeue1) > 0):
      n = len(self.qeue1)
      while n > 0:
        data = self.qeue1.popleft()
        if len(self.qeue1) == 0:
          break
        self.qeue2.append(data)
        n -= 1
      self.qeue2, self.qeue1 = self.qeue1, self.qeue2
      return data



s = StackWithQueue()
s.push(5)
s.push(7)
s.push(9)
s.push(10)
print(s.pop())
print(s.pop())