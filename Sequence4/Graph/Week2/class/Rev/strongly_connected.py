from graph import DirectedGraph
from collections import deque
from toposort import topo_sort

def invert_graph(G):
  _G = DirectedGraph()
  for u in G.all_vertexes():
    connections = [(u.data, v) for u, v in G.get_vertex(u).items()]
    for v, w in connections:
      _G.add_edge(v, u, w)
  return _G

def dfs_rec(G, start, visited):
  visited.add(start)
  connections = set([(u.data, v) for u, v in G.get_vertex(start).items()])
  for v, w in connections - visited:
    dfs_rec(G, v, visited)


def strongly_connected(G):
  stack = topo_sort(G)
  G_t = invert_graph(G)
  visited = set()
  while len(stack) > 0:
    v = stack.pop()
    if v not in visited:
      dfs_rec(G_t, v, visited)


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
  print(strongly_connected(G))

if __name__ == "__main__":
  main()