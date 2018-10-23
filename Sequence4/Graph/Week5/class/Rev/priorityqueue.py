class Node:
  def __init__(self, priority, data):
    self.priority = priority
    self.data = data

  def __str__(self):
    return str(str(self.priority) + " -- " + str(self.data))

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

  def add(self, p, e = None):
    if e is None:
      e = p 
    node = Node(p, e)
    self.Q.append(node)
    self.size += 1
    self.proc_up(self.size)
  
  def proc_up(self, index):
    if index > self.size:
      return
    
    p = self.parent(index)
    if p >= 0 and self.Q[p].priority > self.Q[index].priority:
      self.Q[p], self.Q[index] = self.Q[index], self.Q[p]
      self.proc_up(p)

  def get_min(self):
    ele = self.Q[0]
    self.Q[self.size], self.Q[0] = self.Q[0], self.Q[self.size]
    self.size -= 1
    self.proc_down(0)
    return ele

  def proc_down(self, index):
    l = self.left_child(index)
    r = self.right_child(index)
    _min = index
    if l <= self.size and self.Q[l].priority < self.Q[_min].priority:
      _min = l
    if r <= self.size and self.Q[r].priority < self.Q[_min].priority:
      _min = r
    if _min != index:
      self.Q[_min], self.Q[index] = self.Q[index], self.Q[_min]
      self.proc_down(_min)

  def find(self, e):
    index = -1
    for i in range(self.size+1):
      if self.Q[i].data == e:
        index = i
        break
    return index
  
  def check_ele(self, e):
    return self.find(e) > -1

  def change_priority(self, ele, p):
    index = self.find(ele) 
    if index > -1:
      o_p = self.Q[index].priority
      self.Q[index].priority = p
      if o_p > p:
        self.proc_up(index)
      elif o_p < p:
        self.proc_down(index)

  def isEmpty(self):
    return self.size < 0

  def __str__(self):
    result = [n for n in self.Q]
    return str(result)

def main():
  P = PriorityQueue()
  P.add(5)
  P.add(2)
  P.add(7)
  P.add(10)
  P.add(6)
  P.add(1)
  r = P.get_min()
  print('min', r.data)
  for i in P.Q:
    print(i)
  print("\nafter change")
  P.change_priority(10, 3)
  for i in P.Q:
    print(i)

if __name__ == '__main__':
  main()
  