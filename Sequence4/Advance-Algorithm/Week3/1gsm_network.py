# python3
class Edge:
  def __init__(self):
    self.connections = []

  def add(self, to):
    self.connections.append(to)

class GSM_Network_Solver:
  def __init__(self, n, m, edges, K):
    self.vertexes = n
    self.edge_size = m
    self.edges = edges
    self.K = K
  
  def add_edges(self, fr, to):
    if fr in self.edges:
      val = self.edges[fr]
      val.append(to)
    else:
      self.edges[fr] = [to]
  
  def print_SAT_formula(self):
    C = self.K * self.edge_size + self.vertexes
    V = self.vertexes * self.K
    cnt = 1

    print("{0} {1}".format(C, V))

    for i in range(1, self.vertexes + 1):
      print("{0} {1} {2} 0".format(cnt, cnt+1, cnt+2))
      cnt += 3
    
    for edge in self.edges:
      print("{0} {1} 0".format(-((edge[0]-1)*self.K+1), -((edge[1]-1)*self.K+1)))
      print("{0} {1} 0".format(-((edge[0]-1)*self.K+2), -((edge[1]-1)*self.K+2)))
      print("{0} {1} 0".format(-((edge[0]-1)*self.K+3), -((edge[1]-1)*self.K+3)))

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    print("3 2")
    print("1 2 0")
    print("-1 -2 0")
    print("1 -2 0")



def main():
  n, m = map(int, input().split())
  edges = [ list(map(int, input().split())) for i in range(m) ]
  K = 3 # choices of color
  G = GSM_Network_Solver(n, m, edges, K)
  G.print_SAT_formula()
  # for edge in edges:
  #   G.add_edges(edge[0], edge[1])
  # for key, value in G.edges.items():
  #   print(key, value)
  

  # printEquisatisfiableSatFormula()


if __name__ == '__main__':
  main()
