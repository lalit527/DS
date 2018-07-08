#Uses python3

import sys
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

class Graph:
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
    self.vertexes[to].add_neighbours(self.vertexes[fr])

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def reach(adj, x, y):
  print(adj, x, y)
  return 0

def dfs(G, x, y, visited):
  visited.add(x)
  if x == y:
    return True
  D = G.get_vertex(x)
  S = set([key.data for key in D.keys()])
  for i in S - visited:
    dfs(G, i, y, visited)
  return False

if __name__ == '__main__':
  input = sys.stdin.read()
  G = Graph()
  data = list(map(int, input.split()))
  n, m = data[0:2]
  print('ok', n, m)
  data = data[2:]
  print('data', data)
  print('set', set(data))
  edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
  for edge in edges:
    G.add_edge(edge[0], edge[1])
  print(G)
  x, y = data[2 * m:]
  visited = set()
  # print('done', x, y)
  # adj = [[] for _ in range(n)]
  # x, y = x - 1, y - 1
  # for (a, b) in edges:
  #   adj[a - 1].append(b - 1)
  #   adj[b - 1].append(a - 1)
  dfs(G, x, y, visited)
  r = all(i in visited for i in [x, y])
  print(int(r))
