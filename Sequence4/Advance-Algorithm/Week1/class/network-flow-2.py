from collections import deque

class Edge:
  def __init__(self, fr, to, capacity, flow):
    self.fr = fr
    self.to = to
    self.capacity = capacity
    self.flow = flow

class FlowGraph:
  def __init__(self, n, m):
    self.graph = [[]] * (n + 1)
    self.edges = [] * ((m + 1) * 2)
  
  def add_edge(self, fr, to, capacity):
    forward_edge = Edge(fr, to, capacity, 0)
    backward_edge = Edge(to, fr, 0, 0)
    self.graph[fr].append(len(self.edges))
    self.edges.append(forward_edge)
    self.graph[to].append(len(self.edges))
    self.edges.append(forward_edge)

  def get_id(self, fr):
    return self.graph[fr]

  def get_edges(self, id):
    return self.edges[id]

  def __str__(self):
    return str(self.graph) + str(self.edges)
  

def bfs(G, s, t, parent):
  Q = deque()
  visited = set()
  Q.append(s)
  while len(Q) > 0:
    vertex = Q.popleft()
    if vertex not in visited:
      visited.add(vertex)
      D = G.get_all_vertex(vertex)
      for u, v, w in D:
        Q.append(v)
        parent[v] = vertex
  print(parent)
  # return True if t in visited else False




def ford_fulkerson(G, s, t):
  parent = {}
  bfs(G, s, t, parent) 
  print(parent)
  # while True:
  #   path_flow = float("inf")
  #   sink = t
  #   while sink != source:
  #     path_flow = min(path_flow, G.vertexes[parent[sink]].connections[sink] - G.vertexes[parent[sink]].reverse[sink])

    


     


def main():
  F = FlowGraph(5, 7)
  edges  = [[1, 2, 2], [2, 5, 5], [1, 3, 6], [3, 4, 2], [4, 5, 1], [3, 2, 3], [2, 4, 1]]
  for u, v, w in edges:
    print(u, v, w)
    F.add_edge(u, v, w)

  

  print(F)
  # ford_fulkerson(g, 1, 5)

if __name__ == "__main__":
  main()


"""
5 7
1 2 2
2 5 5
1 3 6
3 4 2
4 5 1
3 2 3
2 4 1
"""