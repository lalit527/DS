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

    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def shortest_path(G, source, dest):
  dist = {}
  prev = {}
  for v in G.vertexes.keys():
    prev[v] = None
    dist[v] = float('inf')
  dist[source] = 0
  Q = deque()
  Q.append(source)
  while len(Q) > 0:
    v = Q.popleft()
    D = G.get_vertex(v)
    if D is not None:
      for i in D.keys():
        print('v', v, i.data)
        if dist[i.data] == float('inf'):
          Q.append(i.data)
          dist[i.data] = dist[v] + 1
          prev[i.data] = v
  if dist[dest] == float('inf'):
    return -1
  else:
    return dist[dest]

def reconstruct_path(source, dest, prev):
  result = []
  while dest != source:
    result.append(dest)
    dest = prev[dest]
  result.append(source)
  result.reverse()
  return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    source, dest = data[(m) * 2:]
    G = Graph()
    for i in range(1, n+1):
      G.add_vertex(i)
    for edge in edges:
      G.add_edge(edge[0], edge[1])
    p = shortest_path(G, source, dest)
    # print(G)
    print(p)
    # if dest not in p or p[dest] is None:
    #   print(-1)
    # else:
    #   result = reconstruct_path(source, dest, p)
    #   print(len(result) - 1) 
    # print(edges)
    # print(n , m)
    # print(source, dest)
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    #     adj[b - 1].append(a - 1)
    # s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    # print(distance(adj, s, t))
