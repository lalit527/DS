from graph import Graph
from collections import deque

def bfs(G, start):
  visited = set()
  queue = deque()
  queue.append(start)
  while len(queue) > 0:
    u = queue.popleft()
    if u not in visited:
      visited.add(u)
      child = G.get_vertex(u)
      if child is not None:
        for key, val in child.items():
          queue.append(key.data)
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
  print(bfs(G, 'A'))

if __name__ == "__main__":
  main()
