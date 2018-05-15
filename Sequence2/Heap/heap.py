class Heap:
  def __init__(self):
    self.size = 0
    self.data = []

  def buildMinHeap(self, arr):
    self.data = arr
    self.size = len(arr)
    n = self.size
    for i in range(n//2, -1, -1):
      self.minHeapify(arr, n, i)
    
  def minHeapify(self, arr, n, index):
    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index
    if left < n and arr[smallest] > arr[left]:
      smallest = left
    if right < n and arr[smallest] > arr[right]:
      smallest = right
    
    if smallest != index:
      arr[index], arr[smallest] = arr[smallest], arr[index]
      self.minHeapify(arr, n, smallest)

  def increaseCapacity(self):
    self.capacity *= 2
    tmp = [None] * self.capacity
    for i in range(self.size):
      tmp[i] = self.data[i]
    self.data = tmp

  def insert(self, n):
    self.data.append(n)
    self.size += 1
    self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
    self.minHeapify(self.data, self.size, 0)

  def deleteMin(self):
    self.data[0], self.data[self.size-1] = self.data[self.size-1], self.data[0]
    self.size -= 1
    n = self.data.pop()
    self.buildMinHeap(self.data)
    return n

  def print(self):
    for i in range(self.size):
      print(self.data[i])

heap = Heap()
arr = [ 12, 11, 13, 5, 6, 7]
heap.buildMinHeap(arr)
#heap.insert(17)
#heap.insert(21)
# print(heap.deleteMin())
heap.print()