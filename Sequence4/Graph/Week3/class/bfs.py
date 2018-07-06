from collections import deque

class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}

  def add_neighbours(self, nb):
    self.connections[nb] = 1

  def get_connections(self):
    return self.connections

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

    
  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result

def bfs(G, source):
  dist = {}
  for v in G.vertexes.keys():
    dist[v] = float('inf')
  dist[source] = 0
  visited = set()
  Q = deque()
  Q.append(source)
  while len(Q) > 0:
    v = Q.popleft()
    visited.add(v)
    print(v)
    D = G.get_vertex(v)
    # print(D)
    if D is not None:
      for i in D.keys():
        if i.data not in visited:
          Q.append(i.data)
          dist[i.data] = dist[v] + 1
  print(dist)


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
  bfs(G, 'A')
  print(G)

if __name__ == "__main__":
  main()