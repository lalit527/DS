from collections import deque

class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}
    self.reverse = {}

  def add_neighbours(self, nb, wt):
    self.connections[nb] = wt

  def add_r_neighbours(self, nb, wt):
    self.reverse[nb] = wt

  def get_connections(self):
    return self.connections

  def get_all_connections(self):
    return [(self.data, key.data, value) for key, value in self.connections.items()]

  def __str__(self):
    return str(self.data) + ' connected to: ' + str([{key.data: value} for key, value in self.connections.items()]) + ' reverse connected to: ' + str([{key.data: value} for key, value in self.reverse.items()])

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
    self.vertexes[fr].add_r_neighbours(self.vertexes[to], 0)

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def get_all_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_all_connections()
    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

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
  g = DirectedGraph()
  for i in range(1, 6):
    g.add_vertex(i)
  g.add_edge(1, 2, 2)
  g.add_edge(2, 5, 5)
  g.add_edge(1, 3, 6)
  g.add_edge(3, 4, 2)
  g.add_edge(4, 5, 1)
  g.add_edge(3, 2, 3)
  g.add_edge(2, 4, 2)
  

  print(g)
  ford_fulkerson(g, 1, 5)

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