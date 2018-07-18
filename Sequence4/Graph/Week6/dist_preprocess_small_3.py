#!/usr/bin/python3


import sys
import queue
import heapq


# Maximum allowed edge length
maxlen = 2 * 10**19

class Shortcut:
  def __init__(self, fr, to, d):
    self.fr = fr
    self.to = to
    self.d = d

class NodePriority:
  def __init__(self, d, vertex):
    self.d = d
    self.vertex = vertex

  def __lt__(self, other):
    return self.d < other.d
  
  def __gt__(self, other):
    return self.d > other.d
  
  def __eq__(self, other):
    return self.d == other.d
  

class Vertex:
  def __init__(self, data=None):
    self.data = data
    self.connections = {}
    self.indirect = {}
    

  def add_neighbours(self, nb, wt):
    try:
      if self.connections[nb] and self.connections[nb] < wt:
        return
    except:
      self.connections[nb] = wt
  
  def add_out_neighbours(self, nb, wt):
    try:
      if self.indirect[nb] and self.indirect[nb] < wt:
        return
    except:
      self.indirect[nb] = wt

  def get_connections(self):
    return self.connections
  
  def get_reverse_connections(self):
    return self.indirect

  def __str__(self):
    return str(self.data) + ' connected to: ' + str(self.connections) + ' reverse connection to: ' + str(self.indirect)

class DirectedGraph:
  def __init__(self, size):
    self.vertexes = [Vertex()] * (size + 1)
    self.size = (size + 1)
    self.INFINITY = (size + 1) * maxlen
    self.bidistance = [self.INFINITY] * (size + 1)
    self.bidistance_r = [self.INFINITY] * (size + 1)
    self.visited = [False] * (size + 1)
    self.visited_r = [False] * (size + 1)
    # Levels of nodes for node ordering heuristics
    self.level = [0] * (size + 1)
    # Positions of nodes in the node ordering
    self.rank = [self.INFINITY] * (size + 1)
    self.shortcut = []
    self.is_shortcut_req = False
    self.max_outgoing = [-1] * (size + 1)
    self.min_outgoing = [self.INFINITY] * (size + 1)
    self.workset = []
    self.dist = [self.INFINITY] * (size + 1)

    for i in range(1, self.size):
      self.max_outgoing[i] = max(self.vertexes[i].connections.keys()) if len(self.vertexes[i].connections.keys()) else 0
      self.min_outgoing[i] = min(self.vertexes[i].connections.keys()) if len(self.vertexes[i].connections.keys()) else self.INFINITY

  def clear(self):
    for v in self.workset:
      self.bidistance[v] = self.bidistance_r[v] = self.INFINITY
      self.visited[v] = self.visited_r[v] = False
    
    self.workset = []

  def add_vertex(self, data):
    v = Vertex(data)
    self.vertexes[data] = v

  def add_out_edge(self, fr, to, wt):
    self.vertexes[fr].add_out_neighbours(to, wt)

  def add_edge(self, fr, to, wt):
    if self.vertexes[fr].data is None:
      self.add_vertex(fr)

    if self.vertexes[to].data is None:
      self.add_vertex(to)
    # self.vertexes[fr].data = fr
    # self.vertexes[to].data = to
    
    self.vertexes[fr].add_neighbours(to, wt)

  def get_all_vertex(self, v):
    return self.vertexes[v].get_connections().items()

  def get_all_vertex_rev(self, v):
    return self.vertexes[v].get_reverse_connections().items()

  def process(self, u, Q):
    for v, w in self.get_all_vertex(u):
      print('F', u, v, w)
      if self.bidistance[v] > self.bidistance[u] + w:
        self.bidistance[v] = self.bidistance[u] + w
        Q.put(NodePriority(self.bidistance[v], v))

  def process_r(self, u, Q):
    for v, w in self.get_all_vertex_rev(u):
      print('B', u, v, w)
      if self.bidistance_r[v] > self.bidistance_r[u] + w:
        self.bidistance_r[v] = self.bidistance_r[u] + w
        Q.put(NodePriority(self.bidistance_r[v], v))

  def query_dijkstra(self, s, t):
    self.clear()
    estimate = self.INFINITY
    Q = queue.PriorityQueue()
    Q_r = queue.PriorityQueue()
    Q.put(NodePriority(0, s))
    Q_r.put(NodePriority(0, t))
    self.bidistance[s] = 0
    self.bidistance_r[t] = 0
    print(self.bidistance)
    print(self.bidistance_r)
    while not Q.empty() or not Q_r.empty():
      if not Q.empty():
        u = Q.get().vertex

        if self.bidistance[u] <= estimate:
          self.process(u, Q)

        self.workset.append(u)
        self.visited[u] = True

        if self.visited_r[u] and self.bidistance[u] + self.bidistance_r[u] < estimate:
          estimate = self.bidistance[u] + self.bidistance_r[u]

      if not Q_r.empty():
        u = Q_r.get().vertex

        if self.bidistance_r[u] <= estimate:
          self.process_r(u, Q_r)

        self.workset.append(u)
        self.visited_r[u] = True

        if self.visited[u] and self.bidistance[u] + self.bidistance_r[u] < estimate:
          estimate = self.bidistance[u] + self.bidistance_r[u]

    return -1 if estimate == self.INFINITY else estimate

  def witness_search(self, s, t, limit):
    self.clear()
    Q = queue.PriorityQueue()
    Q.put(NodePriority(0, s))
    self.workset.append(s)
    self.dist[s] = 0
    hops = 3

    while hops and not Q.empty():
      u = Q.get().vertex
      if limit <= self.dist[u]:
        break

      for v, w in self.get_all_vertex(u):
        if self.rank[v] < self.rank[t] or v == t:
          continue
        
        if self.dist[v] > self.dist[u] + w:
          self.dist[v] = self.dist[u] + w
          Q.put(NodePriority(self.dist[v], v))
          self.workset.append(v)
      
      hops -= 1

  def contract_nb_level(self, u):
    num = 0
    level = 0

    for v, w in self.get_all_vertex(u):
      if self.rank[v] != self.INFINITY:
        num += 1
        if self.level[v] > level:
          level = self.level[v]

    for v, w in self.get_all_vertex_rev(u):
      if self.rank[v] != self.INFINITY:
        num += 1
        if self.level[v] > level:
          level = self.level[v] 

    return num + (level + 1) // 2

  def update_node(self, u):
    for v, w in self.get_all_vertex(u):
      if self.level[v] < self.level[u] + 1:
        self.level[v] = self.level[u] + 1

    for v, w in self.get_all_vertex_rev(u):
      if self.level[v] < self.level[u] + 1:
        self.level[v] = self.level[u] + 1

  def contract(self, u):
    _max = self.max_outgoing[u]
    _min = self.min_outgoing[u]

    num_sc = 0
    sc_cov = set()

    for v, w in self.get_all_vertex_rev(u):
      print('1', u, v, w)
      print(self.rank)
      if self.rank[v] < self.rank[u]:
        continue
      
      limit = w + _max - _min
      self.witness_search(v, u, limit)

      for e, l in self.get_all_vertex(u):
        print('2', u, e, l)
        print(self.rank)
        is_shortcut_req = True
        if self.rank[e] < self.rank[u]:
          continue

        for a, c in self.get_all_vertex_rev(e):
          print('3', u, e, a, c)
          print(self.rank)
          if self.rank[a] < self.rank[u] or a == u:
            continue
          
          if w + l  >= self.dist[a] + c:
            is_shortcut_req = False
            break

        if is_shortcut_req:
          num_sc += 1
          sc_cov.add(e)
          sc_cov.add(v)

          if self.is_shortcut_req:
            print("Life is Fucked", v,e,u)
            self.shortcut.append(Shortcut(v, e, w + l))

        for work in self.workset:
          self.dist[work] = self.INFINITY
        self.workset = []

    return 2 * (num_sc - len(self.vertexes[u].indirect) - len(self.vertexes[u].connections)) + self.contract_nb_level(u) + len(sc_cov)
        
  def add_shortcut(self):
    for sc in self.shortcut:
      if self.max_outgoing[sc.fr] < sc.d:
        self.max_outgoing[sc.fr] = sc.d

      if self.min_outgoing[sc.fr] > sc.d:
        self.min_outgoing[sc.fr] = sc.d
      
      print('shortcut', sc.fr, sc.to, sc.d)
      self.add_edge(sc.fr, sc.to, sc.d)
      self.add_out_edge(sc.to, sc.fr, sc.d)
      
  def remove_edges(self):
    for i in range(1, self.size):
      for v, w in list(self.get_all_vertex(i)):
        if self.rank[i] > self.rank[v]:
          del self.vertexes[i].connections[v]

      for v, w in list(self.get_all_vertex_rev(i)):
        if self.rank[i] > self.rank[v]:
          del self.vertexes[i].indirect[v]

  def preprocess(self):
    Q = queue.PriorityQueue()
    for v in range(1, self.size):
      c = self.contract(v)
      Q.put(NodePriority(c, v))
      print('Fuck', c, v)


    rank_count = 0
    self.is_shortcut_req = True

    while Q.qsize() > 1:
      v = Q.get()
      c = self.contract(v.vertex)
      v.d = c
      print('fuck2', c)

      u = Q.get()

      if v.d <= u.d:
        self.add_shortcut()
        self.rank[v.vertex] = rank_count
        self.update_node(v.vertex)
      else:
        Q.put(v)
      
      Q.put(u)
      rank_count += 1
      self.shortcuts = []
    
    # self.remove_edges()

  def __str__(self):
    result = ""
    for key, value in enumerate(self.vertexes):
      result += str(value) + '\n'
    return result

def readl():
  return map(int, sys.stdin.readline().split())





if __name__ == '__main__':
  n,m = readl()

  # adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
  # cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
  G = DirectedGraph(n)
  G_r = DirectedGraph(n)
  for e in range(m):
    u,v,c = readl()
    G.add_edge(u, v, c)
    G.add_out_edge(v, u, c)
    G_r.add_edge(v, u, c)
      # adj[0][u-1].append(v-1)
      # cost[0][u-1].append(c)
      # adj[1][v-1].append(u-1)
      # cost[1][v-1].append(c)
  print(G)
  G.preprocess()
  print("Ready")
  print(G)
  sys.stdout.flush()
  t, = readl()
  for i in range(t):
      s, t = readl()
      print(G.query_dijkstra(s, t))