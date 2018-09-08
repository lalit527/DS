from graph import Graph
from collections import deque

def dfs(G, start, visited = None):
  if visited is None:
    visited = set()
  visited.add(start)
  D = G.get_connection(start)
  S = set([key.data for key in D.keys()])
  for v in S - visited:
    dfs(G, v, visited)
  
  return visited


def dfs_itr(G, start):
  visited = set()
  S = deque()
  S.append(start)
  while len(S) > 0:
    u = S.pop()
    if u not in visited:
      visited.add(u)
      D = G.get_connection(u)
      vertices = set([key.data for key in D.keys()])
      for v in vertices:
        S.append(v)
  return visited


def bfs(G, start):
  visited = set()
  Q = deque()
  Q.append(start)
  while len(Q) > 0:
    u = Q.popleft()
    if u not in visited:
      visited.add(u)
      D = G.get_connection(u)
      vertices = set([key.data for key in D.keys()])
      for v in vertices:
        Q.append(v)

  return visited

def _topo_sort(G, vertex, visited, stack):
  visited.add(vertex)
  D = G.get_connection(vertex)
  S = set([i.data for i in D.keys()])
  for i in S - visited:
    _topo_sort(G, i, visited, stack)
  
  stack.append(vertex)

def topo_sort(G):
  visited = set()
  stack = deque()
  for vertex in G.vertices:
    if vertex not in visited:
      _topo_sort(G, vertex, visited, stack)
    
  print(stack)

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
  # S = bfs(G, 'A')
  # print(S)
  topo_sort(G)

if __name__ == "__main__":
  main()