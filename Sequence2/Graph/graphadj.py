class Vertex:
  def __init__(self, key):
    self.key = key
    self.connections = {}

  def addNeighbour(self, nb, weight = 1):
    self.connections[nb] = weight
  
class Graph:
  def __init__(self):
    self.vertexList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices += 1
    vertex = Vertex(key)
    self.vertexList[key] = vertex
    return newVertex

  def addEdge(self, f, t, weight):
    if f not in self.vertexList:
     begin = self.addVertex(f) 
    if t not in self.vertexList:
      end = self.vertexList(t)
    
    self.vertexList[f].addNeighbour(self.vertexList[t], weight)

  def getVertices(self):
    return self.vertexList.keys()
