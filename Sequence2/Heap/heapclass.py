class Heap:
  def __init__(self):
    self.data = []

  def getParent(self, index):
    p = (index - 1) // 2
    return p

  def getLeft(self, index):
    l = (index * 2) + 1
    return l

  def getRight(self, index):
    r = (index * 2) + 2
    return r

  def procDown(self, arr, n, index):
    l = self.getLeft(index)
    r = self.getRight(index)
    smallest = index
    if l < n and arr[l] < arr[smallest]:
      smallest = l
    if r < n and arr[r] < arr[smallest]:
      smallest = r
    
    if smallest != r:
      arr[index], arr[smallest] = arr[smallest], arr[index]
      self.procDown(arr, n, smallest)

  def procUp(self, arr, n, index):
    p = self.getParent(index)
    if p < n and p > -1 and arr[p] > arr[index]:
      arr[index], arr[p] = arr[p], arr[index]
      self.procUp(arr, n, p)

  def insert(self, n):
    self.data.append(n)
    size = len(self.data)
    self.procUp(self.data, size, size - 1)

  def getMin(self):
    l = len(self.data)
    self.data[0], self.data[l-1] = self.data[l-1], self.data[0]
    min = self.data.pop()
    self.procDown(self.data, l-1, 0)
    return min
  
  def printHeap(self):
    for i in self.data:
      print(i)

h = Heap()
h.insert(12)
h.insert(11)
h.insert(13)
h.insert(5)
h.insert(6)
h.insert(7)
print(h.getMin())
h.printHeap()