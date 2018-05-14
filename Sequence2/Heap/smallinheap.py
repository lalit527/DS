from heapclass import Heap

def getNSmallest(heap, n, i = 0):
  Haux = Heap()
  count = -1
  data = None
  min = heap.getMin()
  Haux.insert(min)
  while(1):
    data = Haux.getMin()
    count += 1
    if count == n:
      return data
    Haux.insert(min, getLeft())


h = Heap()
h.insert(12)
h.insert(11)
h.insert(13)
h.insert(5)
h.insert(6)
h.insert(7)
getNSmallest(h, 3)