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
  
  def all_edges(self):
    result = [value.get_all_connections() for key, value in self.vertexes.items()]
    return [item for sublist in result for item in sublist]

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def bellman(G, source):
  dist = {}
  prev = {}
  H = []
  for u in G.vertexes:
    dist[u] = float('inf')
    prev[u] = None
  dist[source] = 0

  print(G.all_edges())
  for i in range(len(G.vertexes)):
    for u, v, w in G.all_edges():
      if dist[u] != float('inf') and dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u

  for u, v, w in G.all_edges:
    if dist[u] != float('inf') and dist[u] + w < dist[v]:
      print "Graph contains negetive cycle"
      return
  print(dist)
  print(prev)
    

def main():
  g = DirectedGraph()
  for i in range(9):
    g.add_vertex(i)
  g.add_edge(0, 1, 4)
  g.add_edge(0, 7, 8)
  g.add_edge(1, 2, 8)
  g.add_edge(1, 7, 11)

  g.add_edge(2, 3, 7)
  g.add_edge(2, 8, 2)
  g.add_edge(2, 5, 4)
  g.add_edge(3, 4, 9)
  
  g.add_edge(3, 5, 14)
  g.add_edge(4, 5, 10)
  g.add_edge(5, 6, 2)
  g.add_edge(6, 7, 1)
  g.add_edge(6, 8, 6)
  g.add_edge(7, 8, 7)

  print(g)
  bellman(g, 0)

if __name__ == "__main__":
  main()
  # G = DirectedGraph()
  # for i in range(1, 9):
  #   G.add_vertex(i)
  # G.add_edge(1, 2, 4)
  # G.add_edge(1, 8, 8)
  # G.add_edge(2, 3, 8)
  # G.add_edge(2, 8, 11)
  # G.add_edge(3, 4, 7)
  # G.add_edge(3, 9, 2)
  # G.add_edge(3, 6, 4)
  # G.add_edge(4, 5, 9)

  # G.add_edge(4, 6, 14)
  # G.add_edge(5, 6, 10)
  # G.add_edge(6, 7, 2)
  # G.add_edge(7, 8, 1)
  # G.add_edge(7, 9, 6)
  # G.add_edge(8, 9, 7)
  # print(G)
  # dijksta(G, 1)