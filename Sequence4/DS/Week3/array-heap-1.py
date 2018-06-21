# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self._size = 0

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    self._size = n
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def build_heap(self, i):
    l = 2 * i + 1
    r = 2 * i + 2
    _mi = i
    if l < self._size and self._data[l] < self._data[_mi]:
      _mi = l
    if r < self._size and self._data[r] < self._data[_mi]:
      _mi = r
    
    if _mi != i:
      self._data[_mi], self._data[i] = self._data[i], self._data[_mi]
      self._swaps.append((i, _mi))
      self.build_heap(_mi)

  def GenerateSwaps(self):
    print(self._data)
    print(self._swaps)
    for i in range(self._size//2, -1, -1):
      self.build_heap(i)

  def GenerateSwaps_naive(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
