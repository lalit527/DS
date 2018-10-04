class Node:
  def __init__(self, data):
    self.data = data
    self.parent = None
    self.rank = 0
  
  def __str__(self):
    return str(self.data) + " and parent is " + str(self.parent.data if self.parent else None)

  def __repr__(self):
    return self.__str__()

class DisjointSet:
  def __init__(self):
    self.map = {}

  def make_set(self, data):
    node = Node(data)
    node.parent = node
    self.map[data] = node

  def find_set(self, data):
    return self._find_set(self.map[data])
  
  def _find_set(self, node):
    parent = node.parent
    if parent == node:
      return parent
    node.parent = self._find_set(node.parent)
    return node.parent

  def union(self, data1, data2):
    node1 = self.map[data1]
    node2 = self.map[data2]

    parent1 = self._find_set(node1)
    parent2 = self._find_set(node2)

    if parent1.data == parent2.data:
      return
    
    if parent1.rank >= parent2.rank:
      if parent1.rank == parent2.rank:
        parent1.rank += parent2.rank
      parent2.parent = parent1
    else:
      parent1.parent = parent2

  def __str__(self):
    result = ""
    for key, value in self.map.items():
      result += 'value is ' + str(value) + '\n'
    return result


def main():
  ds = DisjointSet()
  ds.make_set(1)
  ds.make_set(2)
  ds.make_set(3)
  ds.make_set(4)
  ds.make_set(5)
  ds.make_set(6)
  ds.make_set(7)

  ds.union(1,2)
  ds.union(2,3)
  ds.union(4,5)
  ds.union(6,7)
  ds.union(5,6)
  ds.union(3,7)

  print(ds)

  for i in range(1,8):
    print(ds.find_set(i))

  print(ds)

if __name__ == '__main__':
  main()