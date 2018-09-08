import queue
from main.directed_graph import Graph

def check_path(G, start, end):
  if start == end:
    return True
  Q = queue.Queue()
  visited = set()
  Q.put(start)
  while not Q.empty():
    u = Q.get()
    
    if u not in visited:
      visited.add(u)
      D = G.get_connection(u)
      vertices = set([key.data for key in D.keys()])
      for v in vertices:
        if v == end:
          return True
        Q.put(v)
  return False

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
  G.add_edge('B', 'E')
  G.add_edge('A', 'E')
  print(check_path(G, 'B', 'E'))

if __name__ == "__main__":
  main()