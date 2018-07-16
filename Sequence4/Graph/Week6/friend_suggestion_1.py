#!/usr/bin/python3

import sys
import heapq
import random
import time

"""
class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search

    def clear(self):
    # Reinitialize the data structures for the next query after the previous query.
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[v] = False;
        del self.workset[0:len(self.workset)]

    def visit(self, q, side, v, dist):
    # Try to relax the distance to node v from direction side by value dist.
        # Implement this method yourself
        pass

    def query(self, adj, cost, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)
        # Implement the rest of the algorithm yourself
        return -1
"""

class PriorityEntry(object):

  def __init__(self, priority, data):
      self.data = data
      self.priority = priority

  def __lt__(self, other):
      return self.priority < other.priority
  
  def __eq__(self, other): 
    return self.data == other.data

  def __str__(self):
    return str(self.data) + "-" + str(self.priority)


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

  def get_all_connections(self):
    return [(self.data, key.data, value) for key, value in self.connections.items()]

  def __str__(self):
    return ' connected to: ' + str(self.connections)

class DirectedGraph:
  def __init__(self, size):
    self.vertexes = [Vertex()] * (size + 1)
    self.size = size

  def add_vertex(self, data):
    v = Vertex(data)
    self.vertexes[data] = v

  def add_edge(self, fr, to, wt):
    if self.vertexes[fr].data is None:
      self.add_vertex(fr)

    if self.vertexes[to].data is None:
      self.add_vertex(to)
    # self.vertexes[fr].data = fr
    # self.vertexes[to].data = to
    
    self.vertexes[fr].add_neighbours(to, wt)

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return {}

  def get_all_vertex(self, v):
    return self.vertexes[v].get_connections()

    
  def all_edges(self):
    result = [value.get_all_connections() for key, value in self.vertexes.items()]
    return [item for sublist in result for item in sublist]

  def __str__(self):
    result = ""
    for key, value in enumerate(self.vertexes):
      result += str(key) + str(value) + '\n'
    return result

def readl():
    return map(int, sys.stdin.readline().split())

def bidirectional(G, G_r, size, s, t):
  _max = float('inf')
  # dist = {}
  # dist_r = {}
  # prev = {}
  # prev_r = {}
  H = []
  H_r = []
  dist = [_max] * (size + 1) 
  dist_r = [_max] * (size + 1)
  prev = []
  prev_r = [] 
  seen = [False] * (size + 1)
  seen_r = [False] * (size + 1)

  proc = []
  proc_r = []
 
  dist[s] = 0
  dist_r[t] = 0
  heapq.heappush(H, (0, s))
  heapq.heappush(H_r, (0, t))
  while len(H) > 0 and len(H_r) > 0:
    v = heapq.heappop(H)
    process(v[1], G, dist, prev, proc, H, seen)
    if seen_r[v[1]]:
      return shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r)
    
    v_r = heapq.heappop(H_r)
    process(v_r[1], G_r, dist_r, prev_r, proc_r, H_r, seen_r)
    if seen[v_r[1]]:
      return shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r)
   
  return -1

# def process(u, G, dist, prev, proc, H):
#   D = G.get_all_vertex(u)
#   if D is not None:
#     for v, w in D.items():
#       relax(u, v, w, dist, prev, H)
#     proc[u] = True

def process(u, G, dist, prev, proc, H, seen):
  for v, w in G.get_all_vertex(u).items():
    relax(u, v, w, dist, prev, H)
  proc.append(u)
  seen[u] = True

def relax(u, v, w, dist, prev, H):
  if dist[v] > dist[u] + w:
    dist[v] = dist[u] + w
    heapq.heappush(H, (dist[v], v))

def shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r):
  distance = float('inf')
  ubest = None
  for u in proc + proc_r:
    if dist[u] + dist_r[u] < distance:
      ubest = u
      distance = dist[u] + dist_r[u]
  return distance
  # last = ubest
  # while last != s:
  #   path.append(last)
  #   last = prev[last]
  # path = list(reversed(path))
  # last = ubest
  # while last != t:
  #   last = prev_r[last]
  #   path.append(last)
  

def main():
  start = time.time()
  n = 100000
  m = 200000
  G = DirectedGraph(n)
  G_r = DirectedGraph(n)
  # for i in range(1, n + 1):
  #   G.add_vertex(i)
  for _ in range(m):
    u = random.randint(1, n)
    v = random.randint(1, n)
    c = random.randint(1, 1000)
    G.add_edge(u, v, c)
    G_r.add_edge(v, u, c)
  start2 = time.time()
  print('G_Allc', start2 - start)
  t = 10000
  # print(G)
  # print(G_r)
  
  for _ in range(t):
    s = random.randint(1, n)
    t = random.randint(1, n)
    if s == t:
      print(0)
    else:
      print(bidirectional(G, G_r, n, s, t))

  end = time.time()
  print(end - start2)


if __name__ == '__main__':
  # main()
  
    n,m = readl()
    # adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    # cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    G = DirectedGraph(n)
    G_r = DirectedGraph(n)
    # for i in range(1, n + 1):
    #   G.add_vertex(i)
    for e in range(m):
        u,v,c = readl()
        G.add_edge(u, v, c)
        G_r.add_edge(v, u, c)
        # adj[0][u-1].append(v-1)
        # cost[0][u-1].append(c)
        # adj[1][v-1].append(u-1)
        # cost[1][v-1].append(c)

    t, = readl()
    # bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        if s == t:
          print(0)
        else:
          print(bidirectional(G, G_r, n, s, t))
        # count += 1
        # if count == 4:
        #   print(G)
        #   print(G_r)
        #   print(n, m)
        #   print(s, t)

        # print(s, t)
        # print(bidij.query(adj, cost, s-1, t-1))
