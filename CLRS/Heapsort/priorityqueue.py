from heapsort import MaxHeap
from ctypes import py_object
import sys

class PriorityQueue(MaxHeap):
  def __init__(self, size = 16):
    self.size = size
    self.heap_size = -1
    self.heap = (size * py_object)()

  def heap_maximum(self):
    return self.heap[0]
  
  def extract_max(self):
    if self.heap_size < 0:
      return Exception("No Element")
    mx = self.heap[0]
    self.heap[0] = self.heap[self.heap_size]
    self.heap_size -= 1
    self.max_heapify(self.heap, 0)
    return mx

  def inrease_key(self, i, key):
    print(self.heap[i], key)
    if key < self.heap[i]:
      return Exception("Smaller Element")
    self.heap[i] = key
    while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
      self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
      i = self.parent(i)

  def insert(self, key):
    self.heap_size += 1
    self.heap[self.heap_size] = -99999
    self.inrease_key(self.heap_size, key)
    
q = PriorityQueue()
q.insert(1)
print(q.extract_max())