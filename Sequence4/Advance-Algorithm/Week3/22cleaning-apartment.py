# python3
import itertools

class HamiltonSAT:
  def __init__(self, n, m):
    self.vertexes = n
    self.edges = m
    self.clauses = []
    self.matrix = [[False for j in range(n)] for i in range(n)]
    cnt = 1
    self.data = [[(i+j) for j in range(n)] for i in range(1, n*n, n)]
    self.count = 0
    # print(self.data)

  def print_SAT_formula(self):
    n = self.vertexes
    nrange = range(n)
    self.count = 0

    def each_vertex_belog_path():
      for (i, j) in itertools.product(nrange, repeat=2):
        self.clauses.append(str(self.data[i][j]) + " ")
        if j == n - 1:
          self.count += 1
          self.clauses.append("0\n")
    
    def each_vertex_only_once():
      for (i, j) in itertools.product(nrange, repeat=2):
        for k in range(i+1, n):
          self.count += 1
          self.clauses.append(str(-self.data[i][j]) + " ") 
          self.clauses.append(str(-self.data[k][j]) + " ") 
          self.clauses.append(str("0\n"))
    def each_path_occupied():
      for (i, j) in itertools.product(nrange, repeat=2):
        # print('hkehbhjke', i, j)
        self.clauses.append(str(self.data[j][i]) + " ")
        if j == n - 1:
          self.count += 1
          self.clauses.append("0\n")

    def vetrex_diff_pos():
      for (i, j) in itertools.product(nrange, repeat=2):
        for k in range(j+1, n):
          self.count += 1
          self.clauses.append(str(-self.data[i][j]) + " ")
          self.clauses.append(str(-self.data[i][k]) + " ")
          self.clauses.append("0\n")
    
    def nonadjacent_vertices_path():
      for (i, j) in itertools.product(nrange, repeat=2):
        if not self.matrix[i][j] and j != i:
          for k in range(n - 1):
            self.count += 1
            self.clauses.append(str(-self.data[i][k]) + " ")
            self.clauses.append(str(-self.data[j][k + 1]) + " ")
            self.clauses.append("0\n")
    # print("1 %d", self.count)
    each_vertex_belog_path()
    # print("2 %d", self.count)
    each_vertex_only_once()
    # print("3 %d", self.count)
    each_path_occupied()
    # print("4 %d", self.count)
    vetrex_diff_pos()
    # print("5 %d", self.count)
    nonadjacent_vertices_path()
    # print("6 %d", self.count)
    print("{0} {1}\n{2!s}".format(self.count, self.vertexes * self.vertexes, "".join(self.clauses)))

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
