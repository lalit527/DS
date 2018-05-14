from heapclass import Heap

def smallest(heap, n, i =0):
  if i >= heap.getSize():
    return
  if heap.data[i] >= n:
    return
  else:
    print(heap.data[i])
    smallest(heap, n, heap.getLeft(i))
    smallest(heap, n, heap.getRight(i))

  

h = Heap()
h.insert(12)
h.insert(11)
h.insert(13)
h.insert(5)
h.insert(6)
h.insert(7)
smallest(h, 11)
