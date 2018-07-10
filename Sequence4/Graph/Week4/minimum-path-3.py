#Uses python3

import sys
import queue

class DirectedGraph:
  def __init__(self):
    self.vertexes = {}
    self.all_edges = []
    self.size = 0

  def add_vertex(self, data):
    self.size += 1
    self.vertexes[data] = []

  def add_edge(self, fr, to, wt):
    if fr not in self.vertexes:
      self.add_vertex(fr)
      self.size += 1
    
    if to not in self.vertexes:
      self.add_vertex(to)
      self.size += 1
    
    self.vertexes[fr].append((to, wt))
    self.all_edges.append((fr, to, wt))

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v]
    return None

  def get_all_vertex(self, v):
    return self.vertexes.keys()
  
  def all_edges(self):
    return self.add_edge

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(key) + "edges" + str(value) + '\n'
    return result


def bellman(G, source):
  int_max = float('inf')
  dist = {}
  prev = {}
  for u in G.vertexes:
    dist[u] = int_max
    prev[u] = None
  dist[source] = 0
  q = queue.Queue()
  for i in range(len(G.vertexes)):
    for u, v, w in G.all_edges:
      if dist[u] != int_max and dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u
        if i == len(G.vertexes) - 1:
          q.put(v)
          
  visited = [0] * len(G.vertexes)
  shortest = [1] * len(G.vertexes)
  while not q.empty():
    u = q.get()
    visited[u] = 1
    if u != source:
      shortest[u] = 0
    for v in G.get_vertex(u):
      print(v)
      if visited[v[0]] == 0:
        q.put(v[0])
        visited[v[0]] = 1
        shortest[v[0]]
  print(dist)
  print(prev)
  print(visited)
  print(shortest)

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
    for i in range(1, n + 1):
      G.add_vertex(i)
    for edge, w in edges:
      G.add_edge(edge[0], edge[1], w)
    bellman(G, data[0])
    print(data[0])
    # print(G.all_edges)
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

