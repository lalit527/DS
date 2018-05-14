from heapclass import Heap

def minCost(arr):
  h = Heap()
  h.buildMinHeap(arr)
  cost = 0
  while (h.getSize() > 1):
    first = h.getMin()
    second = h.getMin()
    cost += first + second
    h.insert(first + second)
  return cost


arr = [4, 3, 2, 6]
print(minCost(arr))