import heapq

class PriorityEntry(object):

  def __init__(self, priority, data):
      self.data = data
      self.priority = priority

  def __lt__(self, other):
      return self.priority < other.priority
  
  def __eq__(self, other): 
    return self.data == other.data

  def __str__(self):
    return str(self.data) + "-" + str(self.priority)

H = []
heapq.heappush(H, PriorityEntry(7, 'data'))
heapq.heappush(H, PriorityEntry(5, 'data2'))
d = PriorityEntry(1, 'data')
i = H.index(d)
if i > -1:
  H[i] = d
  print('Hello')
  heapq.heapify(H)


for i in H:
  print(i)

print(heapq.heappop(H))
