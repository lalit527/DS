class PriorityQueue:
  def __init__(self):
    self.heap = []
    self.size = 0

  def parent(self, index):
    return (index - 1) // 2

  def leftChild(self, index):
    return (index * 2) + 1

  def rightChild(self, index):
    return (index * 2) + 2 

  def insert(self, data):
    self.heap.append(data)
    self.size += 1
    n = len(self.heap)
    self.proculate_up(n, n - 1)

  def proculate_up(self, size, index):
    if index >= size:
      raise Exception("Invalid Index")
    parent = self.parent(index)
    if parent > -1 and self.heap[parent] > self.heap[index]:
      self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
      self.proculate_up(size, parent)

  def proculate_down(self, size, index):
    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index
    if left < size and arr[smallest] > arr[left]:
      smallest = left
    if right < size and arr[smallest] > arr[right]:
      smallest = right
    
    if smallest != index:
      arr[index], arr[smallest] = arr[smallest], arr[index]
      self.proculate_down(size, smallest)

  def getMin(self):
    l = len(self.heap)
    if l < 1:
      return None
    self.heap[0], self.heap[l-1] = self.heap[l-1], self.heap[0]
    min = self.heap.pop()
    self.procDown(l-1, 0)
    return min

