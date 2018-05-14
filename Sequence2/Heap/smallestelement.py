from heapclass import Heap

def getIndex(heap, data):
  for i in range(len(heap)):
    if heap[i] == data:
      return i
  return -1

# def smallest(heap, n):
#   min = heap.getMin()
#   if n < heap.getMin():
#     return
#   print(min)
#   index = getIndex(heap, min)
#   if index > -1:
#     smallest(heap.getLeft(min), n)

def smallest(heap, data):
  n = len(heap)
  _smallest(heap, 0, n, data)

def _smallest(heap, start, end, data):
  min = heap.getMin()
  

h = Heap()
h.insert(12)
h.insert(11)
h.insert(13)
h.insert(5)
h.insert(6)
h.insert(7)
smallest(h, 11)
h.printHeap()
