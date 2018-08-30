# uses python3

import sys 
import queue

class Edge:
  def __init__(self, u, v, lower_bound, capacity):
    self.u = u
    self.v = v
    self.lower_bound = lower_bound
    self.capacity = capacity
    self.diff = capacity - lower_bound
    self.flow = 0

class FlowGraph:
  def __init__(self, n):
    self.edges = []
    self.graph = [[] for _ in range(n + 2)]
    self.dv = [0] * (n + 2)
    self.DD = 0

  def add_edge(self, fr, to, lower_bound, capacity):
    forward_edge = Edge(fr, to, lower_bound, capacity)
    backward_edge = Edge(to, fr, 0, 0)
    self.graph[fr].append(len(self.edges))
    self.edges.append(forward_edge)
    self.graph[to].append(len(self.edges))
    self.edges.append(backward_edge)
    self.dv[fr] += lower_bound
    self.dv[to] -= lower_bound

  def construct(self, id, flow):
    self.edges[id].flow += flow
    self.edges[id ^ 1].flow -= flow
    self.edges[id].diff -= flow
    self.edges[id ^ 1].diff += flow

  def get_ids(self, fr):
    return self.graph[fr]

  def size(self):
    return len(self.graph)

  def get_edge(self, id):
    return self.edges[id]



class Circulation:
  def __init__(self):
    graph, n, m = self.read_input()
    flow, flows = self.find_circulation(graph, n, m)
    self.write(flow, flows)
  
  def read_input(self):
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
      u, v, lower_bound, capacity = map(int, input().split())
      graph.add_edge(u-1, v-1, lower_bound, capacity)

    for v in range(vertex_count):
      if graph.dv[v] < 0:
        graph.add_edge(vertex_count, v, 0, -graph.dv[v])
      if graph.dv[v] > 0:
        graph.add_edge(v, vertex_count + 1, 0, graph.dv[v])
        graph.DD += graph.dv[v]
    
    return graph, vertex_count, edge_count
  
  def bfs(self, graph, fr, to):
    X = float('inf')
    has_path = False
    n = graph.size()
    dist = [float('inf')] * n
    path = []
    parent = [(None, None)] * n
    q = queue.Queue()
    dist[fr] = 0
    q.put(fr)
    while not q.empty():
      cur_from_node = q.get()
      for id in graph.get_ids(cur_from_node):
        cur_edge = graph.get_edge(id)
        if float('inf') == dist[cur_edge.v] and cur_edge.diff > 0:
          dist[cur_edge.v] = dist[cur_from_node] + 1
          parent[cur_edge.v] = (cur_from_node, id)
          q.put(cur_edge.v)
          if cur_edge.v == to:
            while True:
              path.insert(0, id)
              cur_X = graph.get_edge(id).diff
              X = min(cur_X, X)
              if cur_from_node == fr:
                break
              cur_from_node, id = parent[cur_from_node]
            has_path = True
            return has_path, path, X
    return has_path, path, X

  def max_flow(self, graph, fr, to):
    flow = 0
    while True:
      has_path, path, X = self.bfs(graph, fr, to)
      if not has_path:
        return flow
      for id in path:
        graph.construct(id, X)
      flow += X

    return flow

  def find_circulation(self, graph, n, m):
    flow = self.max_flow(graph, n, n + 1)
    flows = [0] * m
    if flow != graph.DD:
      return False, flows
    else:
      for i in range(m):
        forward_edge = graph.edges[i * 2]
        flows[i] = forward_edge.flow + forward_edge.lower_bound
      return True, flows

  def write(self, flow, flows):
    if not flow:
      print('NO')
    else:
      print('YES')
      print('\n'.join(map(str, flows)))
 


if __name__ == "__main__":
  Circulation()