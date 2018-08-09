# python3
import itertools

class HamiltonSAT:
  def __init__(self, n, m):
    self.vertexes = n
    self.edges = m
    self.clauses = ""
    self.matrix = [[False for j in range(n)] for i in range(n)]
    self.data = [[None for j in range(n)] for i in range(n)]
    self.count = 0
    cnt = 1
    for (i, j) in itertools.product(range(n), repeat=2):
        self.data[i][j] = cnt
        cnt += 1

  def print_SAT_formula(self):
    n = self.vertexes
    nrange = range(n)
    self.count = 0
    def each_vertex_belog_path():
      for (i, j) in itertools.product(nrange, repeat=2):
        self.clauses += str(self.data[i][j]) + " "
        if j == n - 1:
          self.count += 1
          self.clauses += "0\n"
    
    def each_vertex_only_once():
      for (i, j) in itertools.product(nrange, repeat=2):
        for k in range(i+1, n):
          self.count += 1
          self.clauses += str(-self.data[i][j]) + " " + str(-self.data[k][j]) + " 0\n"

    def each_path_occupied():
      for (i, j) in itertools.product(nrange, repeat=2):
        # print('hkehbhjke', i, j)
        self.clauses += str(self.data[j][i]) + " "
        if j == n - 1:
          self.count += 1
          self.clauses += "0\n"

    def each_vertex_only_once():
      for (i, j) in itertools.product(nrange, repeat=2):
        for k in range(j+1, n):
          self.count += 1
          self.clauses += str(-self.data[i][j]) + " " + str(-self.data[i][k]) + " 0\n"
    
    def nonadjacent_vertices_path():
      for (i, j) in itertools.product(nrange, repeat=2):
        if not self.matrix[i][j] and j != i:
          for k in range(n - 1):
            self.count += 1
            self.clauses += str(-self.data[i][k]) + " " + str(-self.data[j][k + 1]) + " 0\n"

    each_vertex_belog_path()
    each_vertex_only_once()
    each_path_occupied()
    each_vertex_only_once()
    nonadjacent_vertices_path()
    print("{0} {1}".format(self.count, self.vertexes * self.vertexes))
    print(self.clauses)

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
  G = HamiltonSAT(n, m)
  for i, j in edges:
    G.matrix[i-1][j-1] = True
    G.matrix[j-1][i-1] = True
  G.print_SAT_formula()
  
  

  # printEquisatisfiableSatFormula()


if __name__ == '__main__':
  main()
