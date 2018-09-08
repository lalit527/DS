class Heap:
  def __init__(self, heap):
    self.heap = heap
    self.size = len(heap)
  
  def parent(self, index):
    return (index - 1) // 2

  def leftChild(self, index):
    return (index * 2) + 1

  def rightChild(self, index):
    return (index * 2) + 2 

  def build_heap(self):
    n = self.size
    for i in range(n//2, -1, -1):
      self.min_heapify(n, i)

  def min_heapify(self, n, i):
    l = self.leftChild(i)
    r = self.rightChild(i)
    _min = i
    if l < n and self.heap[_min] > self.heap[l]:
      _min = l
    
    if r < n and self.heap[_min] > self.heap[r]:
        _min = r

    if _min != i:
      self.heap[i], self.heap[_min] = self.heap[_min], self.heap[i]
      self.min_heapify(n, _min)



arr = [ 12, 11, 13, 5, 6, 7]
heap = Heap(arr)
heap.build_heap()
print(arr)