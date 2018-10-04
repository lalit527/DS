class Vertex:
  def __init__(self, data):
    self.data = data
    self.connections = {}

  def add_neighbours(self, nb, weight):
    self.connections[nb] = weight

  def get_neighbours(self):
    return self.connections

  def __str__(self):
    return str(self.data) + ' connected to: ' + str([x.data for x in self.connections])


class DirectedGraph:
  def __init__(self):
    self.vertexes = {}
  
  def add_vertex(self, v):
    vertex = Vertex(v)
    self.vertexes[v] = vertex
  
  def add_edge(self, fr, to, wt = 1):
    try:
      self.vertexes[fr]
    except KeyError:
      self.add_vertex(fr)

    try:
      self.vertexes[to]
    except KeyError:
      self.add_vertex(to)

    self.vertexes[fr].add_neighbours(self.vertexes[to], wt)
    
  def get_vertex(self, v):
    try:
     return self.vertexes[v].get_neighbours()
    except KeyError:
      return None

  def all_vertexes(self):
    return self.vertexes.keys()

  def __str__(self):
    result = ""
    for key, value in self.vertexes.items():
      result += str(value) + '\n'
    return result 
    

def main():
  G = DirectedGraph()
  G.add_vertex('A')
  G.add_vertex('B')
  G.add_vertex('C')
  G.add_vertex('D')
  G.add_vertex('E')
  G.add_edge('A', 'B', 1)
  G.add_edge('B', 'C', 2)
  G.add_edge('B', 'D', 3)
  G.add_edge('A', 'E', 4)
  print(G)

if __name__ == "__main__":
  main()