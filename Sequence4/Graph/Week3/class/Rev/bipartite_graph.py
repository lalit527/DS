from collections import deque

class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}

  def add_neighbours(self, nb):
    self.connections[nb] = 1

  def get_connections(self):
    return [(v.data, w) for v, w in self.connections.items()]

  def __str__(self):
    return str(self.data) + ' connected to: ' + str([x.data for x in self.connections])

class DirectedGraph:
  def __init__(self):
    self.vertexes = {}
    self.size = 0

  def add_vertex(self, data):
    self.size += 1
    v = Vertex(data)
    self.vertexes[data] = v

  def add_edge(self, fr, to):
    if fr not in self.vertexes:
      self.add_vertex(fr)
      self.size += 1
    
    if to not in self.vertexes:
      self.add_vertex(to)
      self.size += 1
    
    self.vertexes[fr].add_neighbours(self.vertexes[to])

  def get_vertex(self, v):
    if v in self.vertexes:
      return self.vertexes[v].get_connections()
    return None

  def all_vertexes(self):
    return [(v, w.data) for v, w in self.vertexes.items()]
    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def bipartite(G, source):
  color = {}
  queue = deque()
  for v, w in G.all_vertexes():
    color[v] = -1
  color[source] = 1
  queue.append(source)
  while len(Q) > 0:
    u = queue.popleft()
    for v, w in G.get_vertex(u):
      if color[v] == color[u]:
        return 0
      elif color[v] == -1:
        queue.append(v)
        color[v] = 1 - color[v]
  return 1
 
def main():
  G = DirectedGraph()
  G.add_vertex('A')
  G.add_vertex('B')
  G.add_vertex('C')
  G.add_vertex('D')
  G.add_vertex('E')
  G.add_edge('A', 'B')
  G.add_edge('B', 'C')
  G.add_edge('B', 'D')
  G.add_edge('A', 'E')
  G.add_edge('C', 'D')
  G.add_edge('D', 'E')
  prev = bfs(G, 'A')
  print(reconstruct_path('A', 'C', prev))

if __name__ == "__main__":
  main()