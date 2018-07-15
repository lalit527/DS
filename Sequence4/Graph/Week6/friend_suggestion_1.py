#!/usr/bin/python3

import sys
import heapq
import random

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
    return {}

  def get_all_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_all_connections()

    
  def all_edges(self):
    result = [value.get_all_connections() for key, value in self.vertexes.items()]
    return [item for sublist in result for item in sublist]

  def transpose(self):
    g = DirectedGraph()
    for vertex in self.vertexes:
      for u, v, w in self.get_all_vertex(vertex):
        g.add_edge(v, u, w)
    return g
    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def readl():
    return map(int, sys.stdin.readline().split())

def bidirectional(G, G_r, s, t):
  _max = float('inf')
  dist = {}
  dist_r = {}
  prev = {}
  prev_r = {}
  H = []
  H_r = []
  for u in G.vertexes:
    dist[u] = _max
    dist_r[u] = _max
    prev[u] = None
    prev_r[u] = None
  
  dist[s] = 0
  dist_r[t] = 0
  proc = []
  proc_r = []
  heapq.heappush(H, PriorityEntry(0, s))
  heapq.heappush(H_r, PriorityEntry(0, t))
  while len(H) > 0 and len(H_r) > 0:
    v = heapq.heappop(H)
    process(v.data, G, dist, prev, proc, H)
    if v.data in proc_r:
      return shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r)
    
    v_r = heapq.heappop(H_r)
    process(v_r.data, G_r, dist_r, prev_r, proc_r, H_r)
    if v_r.data in proc:
      return shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r)
   
  return (-1, [])

def process(u, G, dist, prev, proc, H):
  D = G.get_all_vertex(u)
  if D is not None:
    for u, v, w in D:
      relax(u, v, w, dist, prev, H)
    proc.append(u)

def relax(u, v, w, dist, prev, H):
  if dist[v] > dist[u] + w:
    dist[v] = dist[u] + w
    prev[v] = u
    d = PriorityEntry(dist[v], v)
    try:
      i = H.index(d)
    except ValueError:
      i = -1
    if i > -1:
      H[i] = d
      heapq.heapify(H)
    else:
      heapq.heappush(H, d)

def shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r):
  distance = float('inf')
  ubest = None
  for u in proc + proc_r:
    if dist[u] + dist_r[u] < distance:
      ubest = u
      distance = dist[u] + dist_r[u]
  path = []
  last = ubest
  while last != s:
    path.append(last)
    last = prev[last]
  path = list(reversed(path))
  last = ubest
  while last != t:
    last = prev_r[last]
    path.append(last)
  return (distance, path)

def main():
  n = 10
  m = 10
  G = DirectedGraph()
  for i in range(1, n + 1):
    G.add_vertex(i)
  for _ in range(m):
    u = random.randint(1, n)
    v = random.randint(1, n)
    c = random.randint(1, 20)
    G.add_edge(u, v, c)
  t = 10
  G_r = G.transpose()
  print(G)
  print(G_r)
  for _ in range(t):
    s = random.randint(1, n)
    t = random.randint(1, n)
    print(bidirectional(G, G_r, s, t)[0])

if __name__ == '__main__':
  main()
  """
    n,m = readl()
    # adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    # cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    G = DirectedGraph()
    for i in range(1, n + 1):
      G.add_vertex(i)
    for e in range(m):
        u,v,c = readl()
        G.add_edge(u, v, c)
        # adj[0][u-1].append(v-1)
        # cost[0][u-1].append(c)
        # adj[1][v-1].append(u-1)
        # cost[1][v-1].append(c)
    t, = readl()
    G_r = G.transpose()
    print(G)
    print(G_r)
    # bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidirectional(G, G_r, s, t)[0])
        # count += 1
        # if count == 4:
        #   print(G)
        #   print(G_r)
        #   print(n, m)
        #   print(s, t)

        # print(s, t)
        # print(bidij.query(adj, cost, s-1, t-1))

    """
