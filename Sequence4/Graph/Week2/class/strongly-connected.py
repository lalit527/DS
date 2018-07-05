from collections import deque

class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}

  def add_neighbours(self, nb):
    self.connections[nb] = 1

  def get_connections(self):
    return self.connections

  def __str__(self):
    return str(self.data) + ' connected to: ' + str([x.data for x in self.connections])

class DirectedGraph:
  def __init__(self):
    self.vertexes = {}
    self.size = 0

  def add_vertex(self, data):
    self.size += 1
    v = Vertex(data)
    self.vertexes[data] = v

  def add_edge(self, fr, to):
    if fr not in self.vertexes:
      self.add_vertex(fr)
      self.size += 1
    
    if to not in self.vertexes:
      self.add_vertex(to)
      self.size += 1
    
    self.vertexes[fr].add_neighbours(self.vertexes[to])

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def _topo_sort(self, vertex, visited, stack):
    visited.add(vertex)
    D = self.get_vertex(vertex)
    S = set([i.data for i in D.keys()])
    for i in S - visited:
      self._topo_sort(i, visited, stack)
    
    stack.append(vertex)

  def topo_sort(self):
    visited = set()
    stack = deque()
    for vertex in self.vertexes:
      if vertex not in visited:
        self._topo_sort(vertex, visited, stack)
      
    return stack

  def transponse(self):
    g = DirectedGraph()
    for key in self.vertexes.keys():
      for v in self.get_vertex(key):
        # print('key', key, v.data)
        g.add_edge(v.data, key)
    return g
  
  def __isCyclic__(self, v, visited, rec_stack):
    visited.add(v)
    rec_stack.add(v)
    D = self.get_vertex(v)
    for nb in D.keys():
      if nb.data not in visited:
        print('nbnv', nb.data, visited)
        if self.__isCyclic__(nb.data, visited, rec_stack):
          return True
      elif nb.data in rec_stack:
        return True
    
    rec_stack.remove(v)
    return False

  def isCyclic(self):
    visited = set()
    rec_stack = set()
    for v in self.vertexes:
      if v not in visited:
        if self.__isCyclic__(v, visited, rec_stack):
          return True
    return False
    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def strongly_connected(G):
  stack = G.topo_sort()
  print(stack)
  G_p = G.transponse()
  visisted = set()
  while len(stack) > 0:
    v = stack.pop()
    if v not in visisted:
      dfs_rec(G_p, v, visisted)

def dfs_rec(G, start, visited = None):
  if visited is None:
    visited = set()
  visited.add(start)
  print(start)
  D = G.get_vertex(start)
  S = set([key.data for key in D.keys()])
  for i in S - visited:
    dfs_rec(G, i, visited)
    
  return visited



def main():
  G = DirectedGraph()
  G.add_vertex('A')
  G.add_vertex('B')
  G.add_vertex('C')
  G.add_vertex('D')
  G.add_vertex('E')
  G.add_edge('A', 'B')
  G.add_edge('B', 'C')
  G.add_edge('B', 'D')
  G.add_edge('A', 'E')
  G.add_edge('C', 'D')
  G.add_edge('D', 'E')
  G.add_edge('D', 'A')
  # strongly_connected(G)
  print(G)
  print(G.isCyclic())

if __name__ == "__main__":
  main()