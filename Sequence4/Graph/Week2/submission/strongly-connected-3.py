#Uses python3

import sys
import sys, threading
from collections import deque
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

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

  def init_vertex(self, n):
    self.size = n
    count = 0
    self.vertexes = dict.fromkeys(range(1,n),)

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
  
  def transponse(self):
    g = DirectedGraph()
    for key in self.vertexes.keys():
      for v in self.get_vertex(key):
        # print('key', key, v.data)
        g.add_edge(v.data, key)
    return g

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def dfs(G, vertex, visited, stack):
  visited.add(vertex)
  D = G.get_vertex(vertex)
  if D is not None:
    for v in D:
      if v.data not in visited:
        dfs(G, v.data, visited, stack)
  # print(visited, vertex)
  stack.append(vertex)    


def toposort(G):
  visited = set()
  stack = deque()
  for vertex in G.vertexes.keys():
    if vertex not in visited:
      dfs(G, vertex, visited, stack)
  # print(stack)
  # stack.reverse()
  return stack

def strongly_connected(G):
  stack = toposort(G)
  G_t = G.transponse()
  # print(stack)
  # print(G_t)
  cc = 0
  visited = set()
  while len(stack) > 0:
    v = stack.pop()
    if v not in visited:
      dfs_rec(G_t, v, visited)
      cc += 1
      # print("")
  return cc

def dfs_rec(G, vertex, visited):
  visited.add(vertex)
  # print(vertex, end="")
  D = G.get_vertex(vertex)
  if D is not None:
    for v in D:
      if v.data not in visited:
        dfs_rec(G, v.data, visited)

def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    G = DirectedGraph()
    for i in range(1, n + 1):
      G.add_vertex(i)
    for edge in edges:
      G.add_edge(edge[0], edge[1])
    print(strongly_connected(G))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    # print(number_of_strongly_connected_components(adj))
