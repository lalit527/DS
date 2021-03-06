#Uses python3

import sys
import queue

from heapq import heappush, heappop

class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}

  def add_neighbours(self, nb, wt):
    self.connections[nb] = wt

  def get_connections(self):
    return self.connections

  def get_all_connections(self):
    return [(self.data, key.data, value) for key, value in self.connections.items()]

  def __str__(self):
    return str(self.data) + ' connected to: ' + str([{key.data: value} for key, value in self.connections.items()])

class DirectedGraph:
  def __init__(self):
    self.vertexes = {}
    self.size = 0

  def add_vertex(self, data):
    self.size += 1
    v = Vertex(data)
    self.vertexes[data] = v

  def add_edge(self, fr, to, wt):
    if fr not in self.vertexes:
      self.add_vertex(fr)
      self.size += 1
    
    if to not in self.vertexes:
      self.add_vertex(to)
      self.size += 1
    
    self.vertexes[fr].add_neighbours(self.vertexes[to], wt)

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def get_all_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_all_connections()
    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def dijksta(G, source):
  dist = {}
  prev = {}
  H = []
  for u in G.vertexes:
    dist[u] = float('inf')
    prev[u] = None
  dist[source] = 0
  heappush(H, (0, source))
  
  while len(H) > 0:
    (w, u) = heappop(H)
    D = G.get_all_vertex(u)
    for edge in D:
      if dist[edge[1]] > dist[u] + edge[2]:
        dist[edge[1]] = dist[u] + edge[2]
        prev[edge[1]] = u
        heappush(H, (edge[2], edge[1]))
  return dist


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    G = DirectedGraph()
    for i in range(1, n+1):
      G.add_vertex(i)
    for edge, w in edges:
      G.add_edge(edge[0], edge[1], w)
    result = dijksta(G, data[0])
    print(result[data[1]] if result[data[1]] != float('inf') else -1)
    # print(n, m)
    # print(edges)
    # adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    # for ((a, b), w) in edges:
    #     adj[a - 1].append(b - 1)
    #     cost[a - 1].append(w)
    # s = data[0]
    # s -= 1
    # distance = [10**19] * n
    # reachable = [0] * n
    # shortest = [1] * n
    # shortet_paths(adj, cost, s, distance, reachable, shortest)
    # for x in range(n):
    #     if reachable[x] == 0:
    #         print('*')
    #     elif shortest[x] == 0:
    #         print('-')
    #     else:
    #         print(distance[x])

