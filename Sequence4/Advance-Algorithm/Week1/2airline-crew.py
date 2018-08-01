# python3

from collections import deque

class Edge:
  def __init__(self, u, v, capacity):
    self.u = u
    self.v = v
    self.capacity = capacity
    self.flow = 0

  def __str__(self):
    return str(self.u) + '->' + str(self.v) + '->' + str(self.capacity) + '->' + str(self.flow)

class FlowGraph:
  def __init__(self, n, m, f):
    self.edges = []
    self.graph = [[] for _ in range(n)]
    self.flights = f

  def add_edge(self, from_, to, capacity):
    forward_edge = Edge(from_, to, capacity)
    backward_edge = Edge(to, from_, 0)
    self.graph[from_].append(len(self.edges))
    self.edges.append(forward_edge)
    self.graph[to].append(len(self.edges))
    self.edges.append(backward_edge)

  def size(self):
    return len(self.graph)

  def get_edge(self, id):
    return self.edges[id]

  def get_ids(self, from_):
    return self.graph[from_]

  def add_flow(self, id, flow):
    self.edges[id].flow += flow
    self.edges[id ^ 1].flow -= flow

  def __str__(self):
    result = ''
    for edge in self.edges:
      result += str(edge) + '\n'
    return result

def bfs(graph, s, t, parent):
  Q = deque()
  Q.append(s)
  parent[:] = [-1] * len(parent)
  while len(Q) > 0:
    current = Q.popleft()
    for id in graph.get_ids(current):
      e = graph.get_edge(id)
      if parent[e.v] == -1 and e.capacity > e.flow and e.v != s:
        parent[e.v] = id
        Q.append(e.v)

def max_flow(graph, s, t):
  flow = 0
  parent = [None] * graph.size()
  bfs(graph, s, t, parent)
  while parent[t] != -1:
    bfs(graph, s, t, parent)
    if parent[t] != -1:
      min_flow = float('inf')
      start = parent[t]
      while start != -1:
        min_flow = min(min_flow, graph.get_edge(start).capacity - graph.get_edge(start).flow)
        start = parent[graph.get_edge(start).u]

      start = parent[t]
      while start != -1:
        graph.add_flow(start, min_flow)
        start = parent[graph.get_edge(start).u]

      flow += min_flow
  
  return flow

def response(graph, flights):
  for i in range(flights):
    job = -1
    for id in graph.get_ids(i + 1):
      e = graph.get_edge(id)
      if e.flow == 1:
        job = e.v - flights
        break
    print(job, end = ' ')
  print('')



def read_data():
    flight, crew = map(int, input().split())
    graph = FlowGraph(flight + crew + 2, flight + crew + 2, flight)

    for i in range(flight):
      graph.add_edge(0, i + 1, 1)

    # adj = [None] * vertex_count
    # for i in range(vertex_count):
    #   for j in range(edge_count):
    # print(adj)

    for i in range(1, flight + 1):
      adj = list(map(int, input().split()))
      for j in range(len(adj)):
        bit = adj[j]
        if bit == 1:
          graph.add_edge(i, flight + j + 1, 1)

    for i in range(flight + 1, flight + crew + 1):
      graph.add_edge(i, flight + crew + 1, 1)

    # for _ in range(edge_count):
    #     u, v, capacity = map(int, input().split())
    #     graph.add_edge(u - 1, v - 1, capacity)
    return graph

if __name__ == '__main__':
    graph = read_data()
    print(graph)
    print(max_flow(graph, 0, graph.size() - 1))
    response(graph, graph.flights)