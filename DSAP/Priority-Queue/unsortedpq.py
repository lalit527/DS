from priorityqueue import PriorityQueueBase
from collections import deque

class UnsortedPriorityQueue(PriorityQueueBase):

  def __init__(self):
    self._data = deque()

  def __len__(self):
    return len(self._data)

  def add(self, key, value):
    self._data.append(self._Item(key, value))


  def _find_min(self):
    if self.is_empty():
      raise Empty('Priority queue is Empty')
    small = self._data[0]
    walk = self._data[1]
    while walk is not None:
      

  def min(self):
    mi = self._find_min()