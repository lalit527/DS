from graph import DirectedGraph
from collections import deque
from toposort import topo_sort

def invert_graph(G):
  _G = DirectedGraph()
  for u in G.all_vertexes():
    for v, w in G.get_vertex(u):
      _G.add_edge(v, u, w)
  return _G

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
  print(invert_graph(G))

if __name__ == "__main__":
  main()