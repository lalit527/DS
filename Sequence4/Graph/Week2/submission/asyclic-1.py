#Uses python3

import sys

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
    
    if to not in self.vertexes:
      self.add_vertex(to)
    
    self.vertexes[fr].add_neighbours(self.vertexes[to])

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def __is_cyclic__(G, vertex, visited, rec_stack):
  visited.add(vertex)
  rec_stack.add(vertex)
  D = G.get_vertex(vertex)
  for nb in D.keys():
    if nb.data not in visited:
      if __is_cyclic__(G, nb.data, visited, rec_stack):
        return 1
    elif nb.data in rec_stack:
      return 1
  
  rec_stack.remove(vertex)
  return 0

def is_cyclic(G):
  visited = set()
  rec_stack = set()
  for vertex in G.vertexes:
    if vertex not in visited:
      if __is_cyclic__(G, vertex, visited, rec_stack):
        return 1
  return 0


def acyclic(adj):
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # print(n, m)
    G = DirectedGraph()
    for i in range(1, n+1):
      G.add_vertex(i)
    for edge in edges:
      G.add_edge(edge[0], edge[1])
    print(is_cyclic(G))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    # print(is_cyclic(adj))
