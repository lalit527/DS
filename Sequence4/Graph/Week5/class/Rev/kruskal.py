from graph import DirectedGraph, Vertex
from disjointset import DisjointSet, Node

def kruskal(G):
  S = DisjointSet()
  for v in G.vertexes:
    S.make_set(v)
  X = set()
  result = []
  E = G.add_edge()
  E = sorted(E, key = lambda x: x[2])
  for u, v, w in E:
    if S.find_set(u) != S.find_set(v):
      X.add(u)
      X.add(v)
      result.append((u, v))
    S.union(u, v)

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
  kruskal(g)

if __name__ == '__main__':
  main()
