from heapclass import Heap
class Node:
  def __init__(self, data, index, identity):
    self.data = data
    self.index = index
    self.identity = identity

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

  def procUp(self, arr, n, index):
    p = self.getParent(index)
    if p < n and p > -1 and arr[p].data > arr[index].data:
      arr[index], arr[p] = arr[p], arr[index]
      self.procUp(arr, n, p)
  
  def procDown(self, arr, n, index):
    l = self.getLeft(index)
    r = self.getRight(index)
    smallest = index
    if l < n and arr[l].data < arr[smallest].data:
      smallest = l
    if r < n and arr[r].data < arr[smallest].data:
      smallest = r
    
    if smallest != index:
      arr[index], arr[smallest] = arr[smallest], arr[index]
      self.procDown(arr, n, smallest)

  def insert(self, n):
    self.printHeap()
    self.data.append(n)
    size = len(self.data)
    self.procUp(self.data, size, size - 1)

  def getMin(self):
    l = len(self.data)
    if l < 1:
      return None
    self.data[0], self.data[l-1] = self.data[l-1], self.data[0]
    min = self.data.pop()
    self.procDown(self.data, l-1, 0)
    return min
  
  def printHeap(self):
    for i in self.data:
      print(i.data, end='')

  def getSize(self):
    return len(self.data)

def merge(mat):
  heap = Heap()
  r = len(mat)
  c = len(mat[0])
  result = []
  for i in range(len(mat)):
    print(mat[i][0])
    data = mat[i][0]
    index = 0
    n = Node(data, index, i)
    heap.insert(n)
  while(1):
    min = heap.getMin()
    if min is None:
      break
    else:
      l = len(mat[min.identity])
      if min.index < l - 1:
        result.append(min.data)
        n = Node(mat[min.identity][min.index+1], min.index + 1, min.identity)
        heap.insert(n)
      else:
        result.append(min.data)
        continue
  print(result)
  

arr = [
        [2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]
      ]

merge(arr)