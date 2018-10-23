from graph import DirectedGraph
from collections import deque


def dfs(G, vertex, visited, stack):
  visited.add(vertex)
  D = G.get_vertex(vertex)
  if D is not None:
    for v in D:
      if v.data not in visited:
        dfs(G, v.data, visited, stack)
  stack.appendleft(vertex)

def topo_sort(G):
  visited = set()
  stack = deque()
  for vertex in  G.all_vertexes():
    if vertex not in visited:
      dfs(G, vertex, visited, stack)
  return stack



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
  print(topo_sort(G))

if __name__ == "__main__":
  main()
