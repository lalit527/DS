from graph import Graph
from collections import deque

def dfs_rec(G, start, visited = None):
  if visited is None:
    visited = set()
  visited.add(start)
  D = G.get_vertex(start)
  S = set([key.data for key in D.keys()])
  for i in S - visited:
    dfs_rec(G, i, visited)
    
  return visited

def dfs_itr(G, start):
  visited = set()
  stack = deque()
  stack.append(start)
  while len(stack) > 0:
    u = stack.pop()
    if u not in visited:
      visited.add(u)
      D = G.get_vertex(u)
      if D is not None:
        for v, w in D.items(): 
          stack.append(v.data)
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
  print(dfs_itr(G, 'A'))

if __name__ == "__main__":
  main()
