class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def addNeighbour(self, nb, weight = 0):
        self.connections[nb] = weight
    
    def getConnections(self):
        return self.connections.keys()

    def getId(self):
        return self.id
    
    def getWeight(self, nb):
        return self.connections[nb]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connections])

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertexList:
            nv = self.addVertex(f)
        if t not in self.vertexList:
            nv = self.addVertex(t)

        self.vertexList[f].addNeighbour(self.vertexList[t], cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList)

    def __contains__(self, n):
        return n in self.vertexList

g = Graph()
for i in range(6):
    g.addVertex(i)


print(g.vertexList)