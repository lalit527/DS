from graph import Graph, Vertex
from collections import deque

def dfs(G, start):
  visited = set()
  stack = deque()
  stack.append(start)

  while len(stack) > 0:
    v = stack.pop()
    if v not in visited:
      visited.add(v)
      child = G.get_vertex(v)
      if child is not None:
        for key, val in child.items():
          stack.append(key.data)
  return visited

def dfs_rec(G, start, visited = None):
  if visited is None:
    visited = set()
  visited.add(start)
  D = G.get_vertex(start)
  S = set([key.data for key in D.keys()])
  for i in S - visited:
    dfs_rec(G, i, visited)
    
  return visited



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
  S = dfs_rec(G, 'A')
  print(S)

if __name__ == "__main__":
  main()