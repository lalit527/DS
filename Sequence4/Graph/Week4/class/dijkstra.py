from heapq import heappush, heappop

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
    return None

  def get_all_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_all_connections()
    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def dijksta(G, source):
  dist = {}
  prev = {}
  H = []
  for u in G.vertexes:
    dist[u] = float('inf')
    prev[u] = None
  dist[source] = 0
  heappush(H, (0, source))
  
  while len(H) > 0:
    (w, u) = heappop(H)
    D = G.get_all_vertex(u)
    print(u, w, dist)
    for edge in D:
      print(edge)
      if dist[edge[1]] > dist[u] + edge[2]:
        dist[edge[1]] = dist[u] + edge[2]
        prev[edge[1]] = u
        heappush(H, (edge[2], edge[1]))
  print(dist)
  print(prev)


if __name__ == "__main__":
  G = DirectedGraph()
  for i in range(1, 6):
    G.add_vertex(i)
  G.add_edge(1, 2, 5)
  G.add_edge(2, 3, 7)
  G.add_edge(1, 3, 4)
  G.add_edge(3, 4, 9)
  print(G)
  dijksta(G, 1)