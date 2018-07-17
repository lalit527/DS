#!/usr/bin/python3


import sys
import queue


# Maximum allowed edge length
maxlen = 2 * 10**6


# class DistPreprocessSmall:
#     def __init__(self, n, adj, cost):
#         # See description of these parameters in the starter for friend_suggestion
#         self.n = n
#         self.INFINITY = n * maxlen
#         self.adj = adj
#         self.cost = cost
#         self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
#         self.visited = [False] * n
#         self.visited = []
#         self.q = queue.PriorityQueue()
#         # Levels of nodes for node ordering heuristics
#         self.level = [0] * n
#         # Positions of nodes in the node ordering
#         self.rank = [0] * n

#         # Implement preprocessing here
#         pass

#     def mark_visited(self, x):
#         if not self.visited[x]:
#             self.visited[x] = True
#             self.visited.append(x)

#     def add_arc(self, u, v, c):
#         def update(adj, cost, u, v, c):
#             for i in range(len(adj[u])):
#                 if adj[u][i] == v:
#                     cost[u][i] = min(cost[u][i], c)
#                     return
#             adj[u].append(v)
#             cost[u].append(c)

#         update(self.adj[0], self.cost[0], u, v, c)
#         update(self.adj[1], self.cost[1], v, u, c)

#     # Makes shortcuts for contracting node v
#     def shortcut(self, v):
#         # Implement this method yourself

#         # Compute the node importance in the end
#         shortcut_count = 0
#         neighbors = 0
#         shortcut_cover = 0
#         level = 0
#         # Compute correctly the values for the above heuristics before computing the node importance
#         importance = (shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])) + neighbors + shortcut_cover + level
#         return importance, shortcuts, level

#     # See description of this method in the starter for friend_suggestion
#     def clear():
#         for v in self.visited:
#             self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
#             self.visited[v] = False;
#         del self.visited[:]

#     # See description of this method in the starter for friend_suggestion
#     def visit(side, v, dist):
#         # Implement this method yourself
#         pass

#     # Returns the distance from s to t in the graph
#     def query(self, s, t):
#         q = [queue.PriorityQueue(), queue.PriorityQueue()]
#         estimate = self.INFINITY
#         visit(0, s, 0)
#         visit(1, t, 0)
#         # Implement the rest of the algorithm yourself

#         return -1 if estimate == self.INFINITY else estimate

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
  
  def add_neighbours(self, nb, wt):
    try:
      if self.indirect[nb] and self.indirect[nb] < wt:
        return
    except:
      self.indirect[nb] = wt

  def get_connections(self):
    return self.connections

  def __str__(self):
    return str(self.data) + ' connected to: ' + str(self.connections) + ' reverse connection to: ' + str(self.indirect)

class DirectedGraph:
  def __init__(self, size):
    self.vertexes = [Vertex()] * (size + 1)
    self.size = size

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
    return self.vertexes[v].get_connections()

  def __str__(self):
    result = ""
    for key, value in enumerate(self.vertexes):
      result += str(key) + str(value) + '\n'
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
    G.add_out_edge(u, v, c)
    G_r.add_edge(v, u, c)
      # adj[0][u-1].append(v-1)
      # cost[0][u-1].append(c)
      # adj[1][v-1].append(u-1)
      # cost[1][v-1].append(c)
  print(G)
  # ch = DistPreprocessSmall(n, adj, cost)
  print("Ready")
  sys.stdout.flush()
  # t, = readl()
  # for i in range(t):
  #     s, t = readl()
  #     print(ch.query(s-1, t-1))