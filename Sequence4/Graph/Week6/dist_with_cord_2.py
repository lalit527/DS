#!/usr/bin/python3

import sys
import queue
import math
import heapq
import time
import random

# class AStar:
#     def __init__(self, n, adj, cost, x, y):
#         # See the explanations of these fields in the starter for friend_suggestion        
#         self.n = n;
#         self.adj = adj
#         self.cost = cost
#         self.inf = n*10**6
#         self.d = [self.inf]*n
#         self.visited = [False]*n
#         self.workset = []
#         # Coordinates of the nodes
#         self.x = x
#         self.y = y

#     # See the explanation of this method in the starter for friend_suggestion
#     def clear(self):
#         for v in self.workset:
#             self.d[v] = self.inf
#             self.visited[v] = False;
#         del self.workset[0:len(self.workset)]

#     # See the explanation of this method in the starter for friend_suggestion
#     def visit(self, q, p, v, dist, measure):
#         # Implement this method yourself
#         pass

#     # Returns the distance from s to t in the graph
#     def query(self, s, t):
#         self.clear()
#         q = queue.PriorityQueue()
#         # Implement the rest of the algorithm yourself
#         return -1

class Vertex:
  def __init__(self, data=None):
    self.data = data
    self.connections = {}

  def add_neighbours(self, nb, wt):
    try:
      if self.connections[nb] and self.connections[nb] < wt:
        return
    except:
      self.connections[nb] = wt

  def get_connections(self):
    return self.connections

  def __str__(self):
    return str(self.data) + ' connected to: ' + str(self.connections)

class DirectedGraph:
  def __init__(self, size):
    self.vertexes = [0]
    self.size = size

  def add_vertex(self, data, points):
    v = Vertex(points)
    self.vertexes.append(v)

  def add_edge(self, fr, to, wt):
    if self.vertexes[fr].data is None:
      self.add_vertex(fr)

    if self.vertexes[to].data is None:
      self.add_vertex(to)
    # self.vertexes[fr].data = fr
    # self.vertexes[to].data = to
    
    self.vertexes[fr].add_neighbours(to, wt)

  def get_all_vertex(self, v):
    return self.vertexes[v].get_connections()

  def __str__(self):
    result = ""
    for key, value in enumerate(self.vertexes):
      result += str(key) + str(value) + '\n'
    return result

def readl():
    return map(int, sys.stdin.readline().split())

def resonstruct_path(prev, current):
  current = current[1]
  total_path = [current]
  while current in prev:
    current = prev[current]
    if current is not None:
      total_path.append(current)
  return total_path

def astar(G, s, t):
  open_set = []
  # prev = {}
  # dist = {}
  # dist_h = {}
  dist = [float('inf')] * (G.size+1)
  dist_h = [float('inf')] * (G.size+1)
  prev = [None] * (G.size+1)
  closed_set = [False] * (G.size+1)
  # for u in range(1, G.size+1):
  #   dist[u] = float('inf')
  #   dist_h[u] = float('inf')
  #   prev[u] = None
  heapq.heappush(open_set, (0, s))
  dist[s] = 0
  dist_h[s] = heuristic_cost(G, s, t)
  # print(dist)
  # print(dist_h)
  while len(open_set) > 0:
    current = heapq.heappop(open_set)
    if current[1] == t:
      return dist[t]
      # return resonstruct_path(prev, current)
    closed_set[current[1]] = True
    u = current[1]
    for v, w in G.get_all_vertex(u).items():
      # print('ok', u, v, w)
      if closed_set[v]:
        continue
      
      # print('fuck', u, v, w)
      # print(dist)
      if dist[v] > dist[u] + w:
        # print('why')
        dist[v] = dist[u] + w
        prev[v] = u
        dist_h[v] = dist[v] + heuristic_cost(G, v, t)
        heapq.heappush(open_set, (dist[v], v))
  
  return -1

def heuristic_cost(G, a, b):
  # print(a, G.vertexes[a].data, b, G.vertexes[b].data)
  x1 = G.vertexes[a].data[0]
  y1 = G.vertexes[a].data[1]
  x2 = G.vertexes[b].data[0]
  y2 = G.vertexes[b].data[1]  
  result = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
  return result

def main():
  start = time.time()
  n = 10000
  m = 30000
  G = DirectedGraph(n)
  for i in range(n):
    a = random.randint(-1000, 1000)
    b = random.randint(-1000, 1000)
    G.add_vertex(i, (a, b))
  for _ in range(m):
    u = random.randint(1, n)
    v = random.randint(1, n)
    c = random.randint(1, 100)
    G.add_edge(u, v, c)
  start2 = time.time()
  print('G_Allc', start2 - start)
  t = 1000
  # print(G)
  # print(G_r)
  
  for _ in range(t):
    s = random.randint(1, n)
    t = random.randint(1, n)
    if s == t:
      print(0)
    else:
      print(astar(G, s, t))

  end = time.time()
  print(end - start2)

if __name__ == '__main__':
  # main()
    n,m = readl()
    G = DirectedGraph(n)
    # x = [0 for _ in range(n)]
    # y = [0 for _ in range(n)]
    # adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        # x[i] = a
        # y[i] = b
        G.add_vertex(i, (a, b))
    for e in range(m):
        u,v,c = readl()
        G.add_edge(u, v, c)
        # adj[u-1].append(v-1)
        # cost[u-1].append(c)
    # print(G)
    t, = readl()
    # astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        if s == t:
          print(0)
        else:
          print(astar(G, s, t))
        # print()
