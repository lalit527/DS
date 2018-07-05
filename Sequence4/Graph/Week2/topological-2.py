#Uses python3

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

def dfs(G, vertex, visited, stack):
  visited.add(vertex)
  D = G.get_vertex(vertex)
  S = set([i.data for i in D.keys()])
  for v in S - visited:
    dfs(G, v, visited, stack)
  if vertex not in stack:
    stack.appendleft(vertex)    


def toposort(G):
  visited = set()
  stack = deque()
  for vertex in set(G.vertexes.keys()) - visited:
      dfs(G, vertex, visited, stack)
  # print(stack)
  # stack.reverse()
  return stack

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
    print(*toposort(G))
    # adj = [[] for _ in range(n)]
    # for (a, b) in edges:
    #     adj[a - 1].append(b - 1)
    # order = toposort(adj)
    # for x in order:
    #     print(x + 1, end=' ')

