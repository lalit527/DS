class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}
  
  def add_neighbours(self, nb, weight = 1):
    self.connections[nb] = weight

  def get_connections(self):
    return self.connections

  def __str__(self):
    return str(self.data) + ' connected to' + str([x.data for x in self.connections])

class Graph:
  def __init__(self):
    self.vertices = {}
    self.size = 0
  
  def add_vertex(self, data):
    self.size += 1
    v = Vertex(data)
    self.vertices[data] = v
  
  def add_edge(self, fr, to):
    if fr not in self.vertices:
      self.add_vertex(fr)
      self.size += 1
    
    if to not in self.vertices:
      self.add_vertex(to)
      self.size += 1
    
    self.vertices[fr].add_neighbours(self.vertices[to])
    
  def get_connection(self, v):
    if v in self.vertices:
      return self.vertices[v].get_connections()

  def __str__(self):
    result = ""
    for key, value in self.vertices.items():
      result += str(value) + '\n'
    return result

def main():
  G = Graph()
  G.add_vertex('A')
  G.add_vertex('B')
  G.add_vertex('C')
  G.add_vertex('D')
  G.add_vertex('E')
  G.add_edge('A', 'B')
  G.add_edge('B', 'C')
  G.add_edge('B', 'D')
  G.add_edge('A', 'E')
  print(G)

if __name__ == "__main__":
  main()