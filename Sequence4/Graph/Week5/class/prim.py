from graph import DirectedGraph
from priorityqueue import PriorityQueue

def prim(G):
  cost = {}
  parent = {}
  u = None
  P = PriorityQueue()
  for v in G.vertexes:
    if u is None:
      u = v
    cost[v] = float('inf')
    P.add(float('inf'), v)
    parent[v] = None

  cost[u] = 0
  P.change_priority(u, 0)
  for i in P.Q:
    print(i)
  while not P.isEmpty():
    print('wtf')
    v_ele = P.get_min()
    vertex = v_ele.data
    print('minimum', v_ele)
    for u, v, w in G.get_all_vertex(vertex):
      print(u, v, w)
      if P.check_ele(v) and cost[v] > cost[u] + w:
        cost[v] = cost[u] + w
        parent[v] = u
        P.change_priority(v, cost[v])
  print(cost)
  print(parent)

  

def main():
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

  print(g)
  prim(g)

if __name__ == '__main__':
  main()

  