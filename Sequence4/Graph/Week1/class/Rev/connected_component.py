from graph import Graph
from collections import deque

def dfs_rec(G, start):
  visited = set()
  vertex_cc = {}
  cc = 1
  for v in G.all_vertexes():
    if v not in visited:
      explore(G, v, visited, cc, vertex_cc)
      cc += 1
  return (vertex_cc)

def explore(G, v, visited, cc, vertex_cc):
  visited.add(v)
  vertex_cc[v] = cc
  D = G.get_vertex(v)
  S = set([key.data for key in D.keys()])
  for i in S - visited:
    explore(G, i, visited, cc, vertex_cc)



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
  print(dfs_rec(G, 'A'))

if __name__ == "__main__":
  main()
