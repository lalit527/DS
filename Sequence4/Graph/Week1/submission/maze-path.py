#Uses python3

import sys

class Vertex:
  def __init__(self, key):
    self.key = key
    self.connections = {}
    self.cc = None
  
  def add_neighbours(self, nb):
    self.connections[nb] = 1

  def get_connections(self):
    return self.connections
  
  def __str__(self):
    return str(self.key) + ' connected to: ' + str([x.key for x in self.connections])


class Graph:
  def __init__(self):
    self.vertexes = {}
    self.size = 0
  
  def add_vertex(self, key):
    self.size += 1
    v = Vertex(key)
    self.vertexes[key] = v

  def add_edge(self, fr, to):
    if fr not in self.vertexes:
      self.add_vertex(fr)
      self.size += 1
    
    if to not in self.vertexes:
      self.add_vertex(to)
      self.size += 1
    
    self.vertexes[fr].add_neighbours(self.vertexes[to])
    self.vertexes[to].add_neighbours(self.vertexes[fr])

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def all_vertexes(self):
    return list(self.vertexes.keys())

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def explore(G, v, visited, cc):
  visited.add(v)
  D = G.get_vertex(v)
  S = set([i.key for i in D.keys()])
  if len(S) > 0:
    for i in S - visited:
      explore(G, i, visited, cc)
    
def dfs(G):
  V = G.all_vertexes()
  visited = set()
  cc = 0
  for v in V:
    if v not in visited:
      # print('nv', v)
      explore(G, v, visited, cc)
      cc = cc + 1
  # print(V, cc)
  return cc

def number_of_components(adj):
  print(adj)
  result = 0
  #write your code here
  return result

if __name__ == '__main__':
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n, m = data[0:2]
  data = data[2:]
  edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
  # print(edges)
  G = Graph()
  for i in range(1, n + 1):
    G.add_vertex(i)
  for edge in edges:
    G.add_edge(edge[0], edge[1])
  # print(G)
  print(dfs(G))
  # adj = [[] for _ in range(n)]
  # for (a, b) in edges:
  #   adj[a - 1].append(b - 1)
  #   adj[b - 1].append(a - 1)
  # print(number_of_components(adj))
