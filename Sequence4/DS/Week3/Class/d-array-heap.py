class DHeap:
  def __init__(self, k, capacity = 16):
    self.capacity = capacity
    self.heap = [None] * capacity
    self.size = -1
    self.k = k
  
  def parent(self, i):
    return (i - 1) // self.k

  def child(self, i, pos):
    return self.k * i + (pos + 1)

  def shift_down(self, index):
    children = [None] * (self.k + 1)
    max_index = index
    for i in range(self.k):
      child_index = child(index, i) 
      if self.heap[child_index] > self.heap[max_index]:
        max_index = child_index
    
    if max_index != index:
      self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
      self.shift_down(max_index)

  def shift_up(self, index):
    parent = self.parent(index)
    if parent >= 0 and self.heap[parent] < self.heap[index]:
      self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
      self.shift_up(parent)
  
  def insert(self, p):
    if self.size + 1 == self.capacity:
      return Exception('Heap is Full')
    self.size += 1
    self.heap[self.size] = p
    self.shift_up(self.size)

  def extract_max(self):
    result = self.heap[0]
    self.heap[0], self.heap[self.size] = self.heap[self.size], self.heap[0]
    self.size -= 1
    self.shift_down(0)
    return result
  
  def view_heap(self):
    print([i for i in self.heap if i is not None])



def build_heap(A, n, k):
  h = DHeap(k)
  for i in range(n-1, -1, -1):
    h.insert(A[i])
  h.view_heap()

def main():
  arr = [4, 5, 6, 7, 8, 9, 10]
  k = 3
  n = len(arr)

  build_heap(arr, n, k)

if __name__ == "__main__":
  main()