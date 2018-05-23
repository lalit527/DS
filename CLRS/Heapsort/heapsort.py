from ctypes import py_object

class MaxHeap:
  def __init__(self, size = 16):
    self.size = size
    self.heap_size = 0
    self.heap = []

  def parent(self, index):
    return (index // 2) - 1
  
  def left(self, index):
    return (2 * index) + 1

  def right(self, index):
    return (2 * index) + 2

  def max_heapify(self, arr, i):
    l = self.left(i)
    r = self.right(i)
    if l <= self.heap_size and arr[l] >  arr[i]:
      largest = l
    else:
      largest = i
    if r <= self.heap_size and arr[r] > arr[largest]:
      largest = r
    
    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      self.max_heapify(arr, largest)

  def build_max_heap(self, arr):
    self.heap_size = len(arr) - 1
    for i in range(self.heap_size//2, -1, -1):
      self.max_heapify(arr, i)

  def heap_sort(self, arr):
    self.build_max_heap(arr)
    self.heap = arr
    for i in range(self.heap_size, 0, -1):
      self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
      self.heap_size -= 1
      self.max_heapify(arr, 0)

def main():
  heap = MaxHeap()
  arr = [ 12, 11, 13, 5, 6, 7]
  heap.heap_sort(arr)
  print(arr)

if __name__ == '__main__':
  main()