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

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
      
    def __str__(self):
      result = ''
      for edge in self.edges:
        result += str(edge) + '\n'
      return result


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def bfs(G, s, t, parent):
  Q = deque()
  Q.append(s)
  for i in range(graph.size()):
    parent[i] = -1
  while len(Q) > 0:
    vertex = Q.popleft()
    for id in G.get_ids(vertex):
      e = G.get_edge(id)
      if parent[e.v] == -1 and e.capacity > e.flow and e.v != s:
        parent[e.v] = id
        Q.append(e.v)


def max_flow(graph, from_, to):
    flow = 0
    parent = [None] * graph.size()
    bfs(graph, from_, to, parent) 
    while parent[to] != -1:
      bfs(graph, from_, to, parent)
      if parent[to] != -1:
        min_flow = float('inf')
        _from = parent[to]
        while _from != -1:
          min_flow = min(min_flow, graph.get_edge(_from).capacity - graph.get_edge(_from).flow)
          _from = parent[graph.get_edge(_from).u]

        _from = parent[to]
        while _from != -1:
          graph.add_flow(_from, min_flow)
          _from = parent[graph.get_edge(_from).u]

        flow += min_flow

    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
