from graph import Graph, Vertex
from collections import deque

def bfs(G, start):
  visited = set()
  queue = deque()
  queue.append(start)
  while len(queue) > 0:
    v = queue.popleft()
    if v not in visited:
      visited.add(v)
      D = G.get_vertex(v)
      for i in D:
        queue.append(i.data)
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
  S = bfs(G, 'A')
  print(S)

if __name__ == "__main__":
  main()