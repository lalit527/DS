#Uses python3
import sys
import math
class Node:
  def __init__(self, data):
    self.data = data
    self.parent = None
    self.rank = 0

  def __str__(self):
    return str(self.data) + " and parent is " + str(self.parent.data if self.parent else None)

  def __repr__(self):
    return self.__str__()

  
class DisjointSet:
  def __init__(self):
    self.map = {}
  
  def make_set(self, data):
    node = Node(data)
    node.parent = node
    self.map[data] = node

  def find_set(self, data):
    return self._find_set(self.map[data])
  
  def _find_set(self, node):
    parent = node.parent
    if parent == node:
      return parent
    node.parent = self._find_set(node.parent)
    return node.parent

  def union(self, data1, data2):
    node1 = self.map[data1]
    node2 = self.map[data2]

    parent1 = self._find_set(node1)
    parent2 = self._find_set(node2)

    if parent1.data == parent2.data:
      return

    if parent1.rank >= parent2.rank:
      if parent1.rank == parent2.rank:
        parent1.rank += parent2.rank
      parent2.parent = parent1
    else:
      parent1.parent = parent2

  def __str__(self):
    result = ""
    for key, value in self.map.items():
      result += 'value is ' + str(value) + '\n'
    return result


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

def minimum_distance(x, y):
    result = 0.
    #write your code here
    return result


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# def prim(G):
#   cost = {}
#   parent = {}
#   u = None
#   P = PriorityQueue()
#   for v in G.vertexes:
#     if u is None:
#       u = v
#     cost[v] = float('inf')
#     P.add(float('inf'), v)
#     parent[v] = None
#   cost[u] = 0
#   P.change_priority(u, 0)
#   W = 0
#   while not P.isEmpty():
#     v_ele = P.get_min()
#     print(v_ele)
#     vertex = v_ele.data
#     for u, v, w in G.get_all_vertex(vertex):
#       print('fk', u, v, w)
#       if P.check_ele(v) and cost[v] > cost[u] + w:
#         W += w
#         cost[v] = cost[u] + w
#         parent[v] = u
#         P.change_priority(v, cost[v])
#   print(cost)
#   print(parent)
#   print(W)

def kruskal(G):
  S = DisjointSet()
  for v in G.vertexes:
    S.make_set(v)
  X = set()
  result = []
  E = G.all_edges()
  E = sorted(E, key = lambda item: item[2])
  union_sum = 0
  for u, v, w in E:
    if S.find_set(u) != S.find_set(v):
      union_sum += 1
      X.add(u)
      X.add(v)
      result.append((u, v))
    S.union(u, v)
    if union_sum > n - k:
      return w
  return -1
  #     print(u, v, w)
  #     break
  # print(X)
  # print(result)
  # _sum = 0
  # for point1, point2 in result:
  #   _sum += distance(point1[0], point2[0], point1[1], point2[1])
  # # print(_sum)
  # return _sum

def distance(x1, x2, y1, y2):
  # x1 = point1.x
  # x2 = point2.x
  # y1 = point1.y
  # y2 = point2.y
  d = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
  return round(d, 12)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    G = DirectedGraph()
    # for i in range(n):
    #   G.add_vertex(Point(x[i], y[i]))

    for i in range(n):
      for j in range(i+1, n):
        # if i == j:
        #   continue
        w = distance(x[i], x[j], y[i], y[j])
        G.add_edge((x[i], y[i]), (x[j], y[j]), w)
    # print(G)
    print("{0:.9f}".format(kruskal(G)))
