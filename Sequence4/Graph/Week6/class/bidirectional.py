from graph import DirectedGraph
import heapq

def bidirectional(G, s, t):
  G_r = G.transpose()
  print(G)
  print(G_r)
  dist = {}
  dist_r = {}
  prev = {}
  prev_r = {}
  H = []
  H_r = []
  for u in G.vertexes:
    dist[u] = 10 ** 19
    dist_r[u] = 10 ** 19
    prev[u] = None
    prev_r[u] = None

  dist[s] = 0
  dist_r[t] = 0
  proc = []
  proc_r = []
  heapq.heappush(H, (0, s))
  heapq.heappush(H_r, (0, t))
  # heapq.heapify([(value, key) for key, value in dist.items()])
  # heapq.heapify((value, key) for key, value in dist_r.items()])
  count = 0
  print(dist)
  print(dist_r)
  while True:
    # if len(H) > 0:
    # [(value, key) for key, value in dist.items()]
      v = heapq.heappop(H)
      process(v[1], G, dist, prev, proc, H)
      if v[1] in proc_r:
        return shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r)
    # if len(H_r) > 0:
      # v_r = heapq.heappop(dist_r)
      # l = [(value, key) for key, value in dist_r.items()]
      # print(l)
      v_r = heapq.heappop(H_r)
      print('v_r', v_r)
      process(v_r[1], G_r, dist_r, prev_r, proc_r, H_r)
      if v_r[1] in proc:
        return shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r)
      count += 1
      if count == 10:
        break
  print(prev)
  print(prev_r)
  print(dist)
  print(dist_r)
  print(proc)
  print(proc_r)

def process(u, G, dist, prev, proc, H):
  D = G.get_all_vertex(u)
  print(u, H, D)
  if D is not None:
    for u, v, w in D:
      relax(u, v, w, dist, prev, H)
    proc.append(u)

def relax(u, v, w, dist, prev, H):
  if dist[v] > dist[u] + w:
    dist[v] = dist[u] + w
    prev[v] = u
    heapq.heappush(H, (dist[v], v))

def shortestpath(s, dist, prev, proc, t, dist_r, prev_r, proc_r):
  distance = float('inf')
  ubest = None
  for u in proc + proc_r:
    if dist[u] + dist_r[u] < distance:
      ubest = u
      distance = dist[u] + dist_r[u]
  path = []
  last = ubest
  while last != s:
    path.append(last)
    last = prev[last]
  path = list(reversed(path))
  last = ubest
  while last != t:
    last = prev_r[last]
    path.append(last)
  return(distance, path)

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

  print(bidirectional(g, 0, 8))
  
if __name__ == "__main__":
  main()