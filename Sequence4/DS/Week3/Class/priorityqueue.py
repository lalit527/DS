class PriorityQueue:
  def __init__(self, capacity=16):
    self.size = -1
    self.capacity = capacity
    self.queue = [None] * capacity

  def parent(self, i):
    return i // 2

  def left_child(self, i):
    return 2 * i + 1

  def right_child(self, i):
    return 2 * i + 2

  def shift_up(self, i):
    parent = self.parent(i)
    if parent >= 0 and self.queue[parent] < self.queue[i]:
      self.queue[parent], self.queue[i] = self.queue[i], self.queue[parent]
      self.shift_up(parent)

  def shift_down(self, i):
    left = self.left_child(i)
    right = self.right_child(i)
    max_index = i
    if left <= self.size and self.queue[left] > self.queue[max_index]:
      max_index = left

    if right <= self.size and self.queue[right] > self.queue[max_index]:
      max_index = right

    if max_index != i:
      self.queue[max_index], self.queue[i] = self.queue[i], self.queue[max_index]

  def insert(self, p):
    if self.size + 1 == self.capacity:
      return Exception('Heap is Full')
    self.size += 1
    self.queue[self.size] = p
    self.shift_up(self.size)

  def extract_max(self):
    result = self.queue[0]
    self.queue[0], self.queue[self.size] = self.queue[self.size], self.queue[0]
    self.size -= 1
    self.shift_down(0)
    return result

  def peek_max(self):
    return self.queue[self.size]

  def change_priority(self, i, p):
    _old = self.queue[i]
    self.queue[i] = p
    if p > _old:
      self.shift_up(i)
    else:
      self.shift_down(i)
