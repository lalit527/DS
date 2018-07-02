# python3

import sys



def getParent(table):
    # find parent and compress path
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    
    return True


    
    # merge(destination - 1, source - 1)
    # print(ans)
    
class Node:
  def __init__(self, data, size, parent = None, rank = 0):
    self.data = data
    self.parent = parent
    self.rank = rank
    self.size = size

class DisjointSet:
  def __init__(self):
    self.map = {}
    self.max_size = float('-inf')

  def make_set(self, data, size):
    node = Node(data, size)
    node.parent = node
    self.map[data] = node
    if self.max_size < size:
      self.max_size = size
  
  def union(self, data1, data2):
    node1 = self.map[data1]
    node2 = self.map[data2]

    parent1 = self.find_set_util(node1)
    parent2 = self.find_set_util(node2)

    if parent1.data == parent2.data:
      return
    size = self.max_size
    if parent1.rank >= parent2.rank:
      if parent1.rank == parent2.rank:
        parent1.rank += 1
      parent2.parent = parent1
      parent1.size += parent2.size
      size = parent1.size
      parent2.size = -999
    else:
      parent1.parent = parent2
      parent2.size += parent1.size
      parent1.size = -999
      size = parent2.size
    
    if self.max_size < size:
      self.max_size = size
  
  def find_set(self, data):
    return self.find_set_util(self.map[data])

  def find_set_util(self, node):
    parent = node.parent
    if parent == node:
      return parent
    node.parent = self.find_set_util(node.parent)
    return node.parent
  
  def check(self):
    print(self.map)

def main():
  n, m = map(int, sys.stdin.readline().split())
  lines = list(map(int, sys.stdin.readline().split()))
  ds = DisjointSet()
  for i in range(1, n+1):
    ds.make_set(i, lines[i - 1])

  for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ds.union(destination, source)
    print(ds.max_size)
if __name__ == "__main__":
  main()