"""Pending for bistar"""

from graph import DirectedGraph
import heapq

def resonstruct_path(prev, current):
  current = current[1]
  total_path = [current]
  while current in prev:
    current = prev[current]
    if current is not None:
      total_path.append(current)
  return total_path

def bi_a_star(G, s, t):
  G_r = G.transpose()
  closed_set = {}
  open_set = []
  prev = {}
  dist = {}
  dist_h = {}
  for u in G.vertexes:
    dist[u] = float('inf')
    dist_h[u] = float('inf')
    prev[u] = None
  heapq.heappush(open_set, (0, s))
  dist[s] = 0
  dist_h[s] = heuristic_cost(s, t)
  while len(open_set) > 0:
    # Need to change
    current = heapq.heappop(open_set)
    if current[1] == t:
      print(dist)
      print(dist_h)
      print(prev)
      return resonstruct_path(prev, current)
    # Need to change
    # closed_set.add(current)

    for u, v, w in G.get_all_vertex(current[1]):
      if v in closed_set:
        continue
      if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u
        dist_h[v] = dist[v] + heuristic_cost(v, t)
        heapq.heappush(open_set, (dist[v], v))
  
  print(dist)
  print(dist_h)
  print(prev)

def heuristic_cost(a, b):
  return int(abs(b - a))

def main():
  n = 10
  edges = [((1, 2), 5)]
  g = DirectedGraph()
  for i in range(9):
    g.add_vertex(i)
  g.add_edge(0, 1, 4)
  g.add_edge(0, 7, 8)
  g.add_edge(1, 2, 8)
  g.add_edge(1, 7, 11)

  g.add_edge(2, 3, 7)
  g.add_edge(2, 8, 2)
  g.add_edge(2, 5, 4)
  g.add_edge(3, 4, 9)
  
  g.add_edge(3, 5, 14)
  g.add_edge(4, 5, 10)
  g.add_edge(5, 6, 2)
  g.add_edge(6, 7, 1)
  g.add_edge(6, 8, 6)
  g.add_edge(7, 8, 7)

  print(a_star(g, 0, 8))
  
if __name__ == "__main__":
  main()