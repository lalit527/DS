from heapclass import Heap

def printMax(arr, k):
  h = Heap()
  frame = arr[:k]
  h.buildMinHeap(frame)
  n = len(arr)
  i = k
  while i < n:
    min = h.getMin()
    print(min)
    h.insert(arr[i])
    i += 1



arr = [4, 3, 2, 6, 7, 9 , 6, 5, 7]
printMax(arr, 2)