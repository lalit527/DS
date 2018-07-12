class PriorityQueue:
  def __init__(self):
    self.Q = []
    self.size = -1
  
  def parent(self, i):
    return (i - 1) // 2

  def left_child(self, p):
    return 2 * p + 1

  def right_child(self, p):
    return 2 * p + 2

  def add(self, ele):
    self.Q.append(ele)
    self.size += 1
    self.proc_up(self.size)
  
  def proc_up(self, index):
    if index > self.size:
      return
    
    p = self.parent(index)
    if p >= 0 and self.Q[p] > self.Q[index]:
      self.Q[p], self.Q[index] = self.Q[index], self.Q[p]
      self.proc_up(p)

  def get_min(self):
    size = self.size
    self.Q[self.size], self.Q[0] = self.Q[0], self.Q[self.size]
    self.size -= 1
    self.proc_down(self, 0)

  def proc_down(self, index):
    l = self.left_child(index)
    r = self.right_child(index)
    _min = index
    if self.Q[l] < self.Q[_min]:
      _min = l
    if self.Q[r] < self.Q[_min]:
      _min = r
    
    if _min != index:
      self.Q[_min], self.Q[index] = self.Q[index], self.Q[_min]
      self.proc_down(_min)

  def __str__(self):
    return str(self.Q)

def main():
  P = PriorityQueue()
  P.add(5)
  P.add(2)
  P.add(7)
  P.add(10)
  P.add(6)
  P.add(1)
  print(P)

if __name__ == '__main__':
  main()
  